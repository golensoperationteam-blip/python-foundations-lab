def build_profile(name, age, height):
    """Return a profile dictionary built from the supplied values."""
    return {
        "name": name,
        "age": age,
        "height": height,
        "is_adult": age >= 18,
    }


if __name__ == "__main__":
    print(build_profile("World", 18, 170.5))
