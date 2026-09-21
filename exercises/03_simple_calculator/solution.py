def calculate(first, second, operation):
    """Return the arithmetic result for the requested operation."""
    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    elif operation == "*":
        return first * second
    elif operation == "/":
        if second == 0:
            raise ValueError("division by zero")
        return first / second
    else:
        raise ValueError("unsupported operation")


if __name__ == "__main__":
    print(calculate(10, 5, "+"))
