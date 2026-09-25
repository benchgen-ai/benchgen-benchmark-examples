# Cat Care Basics (Open Answers)

An example benchmark, small on purpose. It asks three open questions about looking after a
cat and scores each answer on the key points it mentions, not on matching a phrase.

## How an answer is scored

Every question has a short list of key points. An answer earns credit for each point it
covers, and alternatives are written with a pipe, so `flight|escape` accepts either word.
Two numbers reach the leaderboard: how many key points were covered, and whether all of
them were.

## What it is here for

This is the shape a custom-format benchmark takes on BenchGen: the questions, the answer
key, the program that asks the model and the program that scores it, all in one folder.
The platform can build a benchmark straight from this folder.
