# How `cat-care-basics` is scored

This benchmark asks open questions and scores the key points an answer mentions.
It does not require the answer to repeat the reference wording exactly.

## Example: why do cats purr?

The question in `phase/input_data/items.json` is:

> Why do cats purr?

The reference data in `phase/reference_data/items.json` lists three key points:

1. Contentment, happiness, relaxation, or calm.
2. Healing, stress relief, pain, or comfort.
3. Vibration or frequency.

The pipe character in the reference data separates accepted alternatives. For
example, `content|happy|relax|calm` accepts any of those words.

A strong answer could be:

> Cats often purr when they feel content or calm. Purring can also help them
> cope with stress or pain, and it produces a vibration or frequency.

This answer covers all three key points, so it receives **3/3 points**, or
**100% keyword coverage**, and `all_keywords` is true.

A weak answer could be:

> Cats purr when they are happy.

This answer covers only the first key point. It receives **1/3 points**, or
**33.33% keyword coverage**, and `all_keywords` is false.

The scoring program in `scoring_program/scoring.py` normalizes case and spacing,
then checks whether each key point or one of its alternatives appears in the
answer. The same approach is used for the other two questions in the example.
