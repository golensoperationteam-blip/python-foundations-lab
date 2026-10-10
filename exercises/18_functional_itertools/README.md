# Exercise 18: Functional Itertools and Data Manipulation

## Objective
Compose iterable pipelines and functional reductions to analyze model token usage.

## Functions
- count_tokens chains batches and counts every token.
- group_models_by_provider sorts copied records, then groups adjacent provider values with itertools.groupby.
- running_token_consumption uses functools.reduce to produce cumulative totals.

## Concepts
chain concatenates iterables, groupby groups consecutive equal keys (so data is sorted first), and reduce folds values into an accumulator.

## Run
python -m pytest exercises/18_functional_itertools/test_solution.py
