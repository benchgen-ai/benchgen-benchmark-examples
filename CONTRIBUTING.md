# Contributing to Benchgen benchmark examples

Thanks for helping. This repository holds example benchmark bundles for [Benchgen](https://benchgen.com/?utm_source=github&utm_medium=contributing&utm_campaign=github-community&utm_content=examples). Each folder under `benchmarks/` is one complete benchmark that you can copy and adapt.

## Ways to help

| You want to | Do this |
|---|---|
| Ask a question | Start a [Discussion](https://github.com/benchgen-ai/benchgen-benchmark-examples/discussions) |
| Bring an evaluation problem | Use the **Bring your evaluation problem** form. The best ones become public benchmarks, credited to you |
| Propose a new benchmark | Use the **Propose a benchmark** form before writing code, so we can say whether it fits |
| Fix a mistake | Open a pull request. Small fixes need no issue |
| Pick a first task | Look for the `good first issue` label |

## Before you start

- Everything you submit is public. **Never include secrets, customer data or anything confidential.** Replace private data with synthetic examples.
- You must have the right to share the questions and answers you submit. Say where they come from and under which licence.
- By contributing you agree your work is released under the [Apache License 2.0](LICENSE), the licence of this repository.

## The shape of a benchmark bundle

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

Copy `benchmarks/cat-care-basics` and change it. `model.py` is injected by the platform when a run starts, so your bundle only has to meet the ingestion and scoring contract.

## A good benchmark

- **One clear thing it measures**, stated in `pages/overview.md`.
- **A scorer you can explain in two sentences.** If an answer can be right in more than one way, say how the scorer decides.
- **Questions and answers that are correct.** Check them. Wrong labels make a benchmark worse than none.
- **Small to start.** A few well-checked items beat hundreds of unchecked ones.
- **Honest limits.** Say what the benchmark does not cover.

## Try it on the platform (optional)

You can check a bundle without creating anything by adding `?dry_run=1` to the create-from-repository call. This needs a Benchgen account and API token, see the [API reference](https://benchgen.com/docs/api-reference/introduction?utm_source=github&utm_medium=contributing&utm_campaign=github-community&utm_content=api). There is no automated check on pull requests yet, so please run the file checklist in the pull request template yourself.

## Pull requests

1. Fork the repository and create a branch.
2. Change one thing per pull request.
3. Fill in the pull request template.
4. A maintainer will review it. We cannot promise how fast.

## Conduct and security

We follow the [Code of Conduct](CODE_OF_CONDUCT.md). Report security problems as described in [SECURITY.md](SECURITY.md), not in a public issue.
