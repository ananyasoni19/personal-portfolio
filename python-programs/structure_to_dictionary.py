"""
Structure to Dictionary
Converts a simple list of key-value pairs into a Python dictionary.
Also shows how to build a dictionary from two parallel lists (keys and values).
"""


def pairs_to_dictionary(pairs):
    """
    Convert a list of (key, value) pairs into a dictionary.
    Example: [("name", "Ananya"), ("skill", "Python")]
          -> {"name": "Ananya", "skill": "Python"}
    """
    # The input must be a list (or tuple) of pairs
    if not isinstance(pairs, (list, tuple)):
        print("Invalid input. Expected a list or tuple of (key, value) pairs.")
        return None

    result = {}
    for item in pairs:
        # Each item must be a pair with exactly two parts
        if not isinstance(item, (list, tuple)) or len(item) != 2:
            print(f"Skipping invalid pair: {item}")
            continue
        key, value = item
        try:
            result[key] = value
        except TypeError:
            # Dictionary keys must be hashable (e.g. str, int) — not lists
            print(f"Skipping unhashable key: {key}")
            continue
    return result


def lists_to_dictionary(keys, values):
    """
    Build a dictionary from two lists of the same length.
    Example: keys=["a", "b"], values=[1, 2] -> {"a": 1, "b": 2}
    """
    # Both arguments must be lists (or tuples)
    if not isinstance(keys, (list, tuple)) or not isinstance(values, (list, tuple)):
        print("Invalid input. Both keys and values must be lists or tuples.")
        return None

    if len(keys) != len(values):
        print("Invalid input. The keys list and values list must have the same length.")
        return None

    result = {}
    # Walk both lists by index and pair each key with its value
    for i in range(len(keys)):
        try:
            result[keys[i]] = values[i]
        except TypeError:
            print(f"Skipping unhashable key: {keys[i]}")
            continue
    return result


def main():
    # --- Demo 1: list of pairs -> dictionary ---
    student_pairs = [
        ("name", "Ananya"),
        ("course", "Computer Science"),
        ("language", "Python"),
        ("invalid_item",),  # deliberately incomplete — will be skipped
    ]

    print("Demo 1: Convert list of pairs to a dictionary")
    student_dict = pairs_to_dictionary(student_pairs)
    if student_dict is not None:
        print(student_dict)
    print()

    # --- Demo 2: two lists -> dictionary ---
    keys = ["C", "C++", "Python"]
    values = ["basic", "basic", "basics"]

    print("Demo 2: Convert two lists into a dictionary")
    skills_dict = lists_to_dictionary(keys, values)
    if skills_dict is not None:
        print(skills_dict)
    print()

    # --- Demo 3: invalid lengths ---
    print("Demo 3: Mismatched list lengths (invalid input)")
    lists_to_dictionary(["one", "two"], ["only_one_value"])
    print()

    # --- Demo 4: wrong structure type ---
    print("Demo 4: Wrong input type (invalid input)")
    pairs_to_dictionary("not a list")
    lists_to_dictionary("C", ["basic"])


if __name__ == "__main__":
    main()
