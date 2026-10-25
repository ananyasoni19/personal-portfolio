"""
Average calculator (contains bugs on purpose)

This program is meant to find the average of a list of numbers.
It currently has 2 simple bugs. Do not treat the result as correct.

The bugs are:
1. The loop does not visit every number in the list.
2. The total is divided by the wrong number.
"""


def calculate_average(numbers):
    """Return the average of a list of numbers. This version is buggy."""
    total = 0

    # BUG 1: range(len(numbers) - 1) stops one item too early.
    # The last number in the list is never added to total.
    for i in range(len(numbers)):
        total = total + numbers[i]

    # BUG 2: the total is divided by 5 instead of the real length of the list.
    # This only works if the list happens to have 5 numbers, and even then
    # BUG 1 still makes the answer wrong.
    average = total / len(numbers)
    return average


sample_scores = [10, 20, 30, 40, 50]
result = calculate_average(sample_scores)

print("List of numbers:", sample_scores)
print("Corrected average:", result)
print("Expected average if the code were correct: 30.0")
