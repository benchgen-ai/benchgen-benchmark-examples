# BenchGen benchmark examples

Example benchmark bundles for the [BenchGen](https://benchgen.com) platform, in the layout the
platform expects. Each folder under `benchmarks/` is one complete benchmark: the questions, the
answer key, the program that asks the model and the program that scores it.

## Building one on the platform

The platform can build a benchmark straight from a folder in this repository:

```bash
curl -X POST https://api.benchgen.com/api/competitions/create_from_repo/ \
  -H "Authorization: Bearer $BENCHGEN_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"repo": "https://github.com/benchgen-ai/benchgen-benchmark-examples",
       "path": "benchmarks/cat-care-basics"}'
```

Add `?dry_run=1` to check the bundle without creating anything. Full reference:
[create a benchmark from a repository](https://benchgen.com/docs/api-reference/introduction).

## What is in here

| Folder | Format | What it measures |
| --- | --- | --- |
| `benchmarks/cat-care-basics` | Open answers scored on key points | Three questions about cat care, scored on the points an answer covers rather than its wording |

## The layout

```
competition.yaml        title, description, tasks, phases, leaderboard columns
pages/overview.md       what the benchmark page shows
terms.md                the terms participants accept
logo.png                the image on the benchmark card
ingestion_program/      how the model is asked
scoring_program/        how an answer is scored
phase/input_data/       the questions
phase/reference_data/   the answers
```

`model.py` is injected by the platform at run time, so a bundle only has to meet the ingestion
and scoring contract.

## Contributing

Bring an evaluation problem, propose a benchmark, or pick a [good first issue](https://github.com/benchgen-ai/benchgen-benchmark-examples/labels/good%20first%20issue). Read [CONTRIBUTING.md](CONTRIBUTING.md) first. Questions go in [Discussions](https://github.com/benchgen-ai/benchgen-benchmark-examples/discussions).

## License

[Apache License 2.0](LICENSE).
