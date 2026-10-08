# Exercise 5: Word Counter

## Objective

Build a small word-frequency counter that turns a text string into a dictionary of word counts.

## Function Signature

```python
count_words(
    text: str,
    case_sensitive: bool = False,
    remove_punctuation: bool = True,
) -> dict[str, int]
```

## Default Behavior

By default, the function:
- Treats words case-insensitively by converting tokens to lowercase.
- Removes standard ASCII punctuation before tokenization.
- Preserves repeated words by incrementing their dictionary count.

## Case Sensitivity

- `case_sensitive=False`: `"Python"`, `"python"`, and `"PYTHON"` are counted as the same word.
- `case_sensitive=True`: the original letter casing is preserved, so those forms are separate dictionary keys.

## Punctuation Handling

With `remove_punctuation=True`, standard ASCII punctuation from Python's `string.punctuation` is replaced with spaces. Replacing punctuation with spaces keeps adjacent words separate, so `"hello,world"` becomes `"hello"` and `"world"`.

With `remove_punctuation=False`, the function uses a simple whitespace-based rule: each whitespace-separated token is preserved exactly, including punctuation attached to that token. For example, `"Hello, hello!"` becomes `{"Hello,": 1, "hello!": 1}` when case sensitivity is enabled.

## Empty Input

An empty string or a string containing only whitespace returns an empty dictionary:

```python
count_words("   ")
# {}
```

## Strings and Dictionaries

The exercise demonstrates two fundamental Python ideas:
- Strings provide the input text and support operations such as `.lower()`, `.split()`, and `.translate()`.
- Dictionaries store each token as a key and its frequency as an integer value.

## Basic Tokenization

Tokenization is deterministic and intentionally beginner-friendly:
1. Return `{}` when the input contains no non-whitespace characters.
2. Replace ASCII punctuation with spaces when punctuation removal is enabled.
3. Split the resulting text on whitespace.
4. Normalize case when requested.
5. Count each token in a dictionary.

## CLI Command

From the repository root:

```bash
python exercises/05_word_counter/solution.py
```

The CLI counts a sample sentence and prints the resulting frequency dictionary.

## Test Command

From the repository root:

```bash
python -m pytest exercises/05_word_counter/test_solution.py
```

## Example

Input:

```text
"Python is fun, and Python is practical!"
```

Output:

```python
{"python": 2, "is": 2, "fun": 1, "and": 1, "practical": 1}
```
