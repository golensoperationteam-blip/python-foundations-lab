import string


def count_words(
    text: str,
    case_sensitive: bool = False,
    remove_punctuation: bool = True,
) -> dict[str, int]:
    """Return deterministic word frequencies for a text string.

    When punctuation is removed, ASCII punctuation characters are replaced
    with spaces so adjacent words remain separate. When punctuation is
    preserved, whitespace-separated tokens keep their original punctuation.
    """
    if not text.strip():
        return {}

    if remove_punctuation:
        translation_table = str.maketrans(
            {character: " " for character in string.punctuation}
        )
        tokens = text.translate(translation_table).split()
    else:
        tokens = text.split()

    if not case_sensitive:
        tokens = [token.lower() for token in tokens]

    counts: dict[str, int] = {}
    for token in tokens:
        counts[token] = counts.get(token, 0) + 1

    return counts


if __name__ == "__main__":
    sample_sentence = "Python is fun, and Python is practical!"
    result = count_words(sample_sentence)
    print("Word frequency:")
    print(f"Input: {sample_sentence}")
    print(f"Result: {result}")
