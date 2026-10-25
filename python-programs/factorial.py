"""
Factorial Calculator
Asks the user for a non-negative integer and prints its factorial.
Example: 5! = 5 × 4 × 3 × 2 × 1 = 120
"""


def factorial(n):
    """Return n! for a non-negative integer n."""
    # 0! and 1! are both defined as 1
    if n == 0 or n == 1:
        return 1

    result = 1
    # Multiply all numbers from 2 up to n
    for i in range(2, n + 1):
        result = result * i
    return result


def main():
    try:
        user_input = input("Enter a non-negative integer: ").strip()
    except EOFError:
        # Happens if input is closed unexpectedly
        print("Invalid input. No number was provided.")
        return

    # Reject empty text, letters, decimals, and negatives
    # (str.isdigit() is True only for digits 0-9)
    if user_input == "":
        print("Invalid input. Please enter a non-negative whole number (0, 1, 2, ...).")
        return

    if not user_input.isdigit():
        print("Invalid input. Please enter a non-negative whole number (0, 1, 2, ...).")
        return

    number = int(user_input)
    print(f"{number}! = {factorial(number)}")


if __name__ == "__main__":
    main()
