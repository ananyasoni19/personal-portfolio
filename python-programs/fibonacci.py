"""
Fibonacci Sequence Generator
Asks the user how many terms to print, then shows the Fibonacci sequence.
Example for 7 terms: 0, 1, 1, 2, 3, 5, 8
"""


def fibonacci_sequence(count):
    """Return a list with the first `count` Fibonacci numbers."""
    # Special cases for very small counts
    if count <= 0:
        return []
    if count == 1:
        return [0]

    sequence = [0, 1]
    # Each new number is the sum of the previous two
    while len(sequence) < count:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence


def main():
    try:
        user_input = input("How many Fibonacci terms do you want? ").strip()
    except EOFError:
        # Happens if input is closed unexpectedly
        print("Invalid input. No number was provided.")
        return

    # Reject empty text, letters, decimals, and negative signs
    if user_input == "" or not user_input.isdigit():
        print("Invalid input. Please enter a positive whole number (1, 2, 3, ...).")
        return

    count = int(user_input)

    # 0 is a digit, but we need at least one term
    if count == 0:
        print("Invalid input. Please enter a number greater than 0.")
        return

    terms = fibonacci_sequence(count)
    # Join the numbers with commas for easy reading
    print("Fibonacci sequence:")
    print(", ".join(str(term) for term in terms))


if __name__ == "__main__":
    main()
