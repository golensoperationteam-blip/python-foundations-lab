def analyze_numbers(numbers: list[int | float]) -> dict:
    """Return basic statistics and the even integer values in input order."""
    if not numbers:
        raise ValueError("numbers must not be empty")

    even_integers = [number for number in numbers if type(number) is int and number % 2 == 0]

    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "evens": even_integers,
    }


if __name__ == "__main__":
    sample_numbers = [4, -3, 2.5, 8, 7]
    result = analyze_numbers(sample_numbers)
    print("List analysis:")
    print(f"Input: {sample_numbers}")
    print(f"Result: {result}")
