#!/usr/bin/env python3
"""Ask the model being evaluated one prompt per item and write its answers.

BenchGen runs this inside the container, with:

    /app/input_data/        this bundle's phase/input_data
    /app/ingested_program/  model.py, written by the platform at run time
    /app/output/            where predictions go, read by the scoring program
    /app/program/           this folder

You usually do not need to change this file. It builds a prompt from each
item and records what came back. Put your judgement in scoring.py instead:
this side only collects answers, it never decides whether they are right.

The model is whatever the user launched the run with. The platform writes
/app/ingested_program/model.py itself from its universal template, so the
only contract is: import it, construct it, call call_llm(prompt) -> str.
"""
import json
import os
import sys
import traceback

INPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else '/app/input_data'
OUTPUT_DIR = sys.argv[2] if len(sys.argv) > 2 else '/app/output'
SUBMISSION_DIR = sys.argv[4] if len(sys.argv) > 4 else '/app/ingested_program'


def load_model():
    """The platform's model.py exposes one class under several names."""
    sys.path.insert(0, SUBMISSION_DIR)
    import model as model_module

    for name in ('Model', 'TurkishLanguageModel', 'GSM8KModel', 'MMLUModel'):
        cls = getattr(model_module, name, None)
        if cls is not None:
            return cls()
    raise RuntimeError('model.py exposes no known model class')


def load_items():
    """Every item the phase's input_data holds, in file order."""
    items = []
    for name in sorted(os.listdir(INPUT_DIR)):
        if not name.endswith('.json'):
            continue
        with open(os.path.join(INPUT_DIR, name), encoding='utf-8') as handle:
            payload = json.load(handle)
        items.extend(payload if isinstance(payload, list) else payload.get('data', []))
    return items


def build_prompt(item):
    """What the model is asked. Change this when your items need more context."""
    parts = [str(item.get('question', '')).strip()]
    if item.get('context'):
        parts.insert(0, str(item['context']).strip())
    if item.get('tools'):
        # Tool-call style items: show the model what it may call.
        parts.append('Available tools:\n' + json.dumps(item['tools'], ensure_ascii=False, indent=2))
    if item.get('instruction'):
        parts.append(str(item['instruction']).strip())
    return '\n\n'.join(part for part in parts if part)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    model = load_model()
    items = load_items()
    print(f'[ingestion] {len(items)} items', flush=True)

    predictions = []
    for index, item in enumerate(items):
        answer, error = '', None
        prompt = build_prompt(item)
        try:
            answer = model.call_llm(prompt) or ''
        except Exception as exc:  # one bad item must not lose the whole run
            error = f'{type(exc).__name__}: {exc}'
            traceback.print_exc()
        predictions.append({
            'id': item.get('id', index),
            'prediction': answer.strip() if isinstance(answer, str) else str(answer),
            'error': error,
            # The scoring program never sees the questions, only the answers.
            # Recording them here is what lets it write per-question results.
            'prompt': prompt,
            'group': str(item.get('group') or ''),
        })
        if (index + 1) % 10 == 0:
            print(f'[ingestion] {index + 1}/{len(items)}', flush=True)

    with open(os.path.join(OUTPUT_DIR, 'predictions.json'), 'w', encoding='utf-8') as handle:
        json.dump(predictions, handle, ensure_ascii=False, indent=2)
    print(f'[ingestion] wrote {len(predictions)} predictions', flush=True)


if __name__ == '__main__':
    main()
