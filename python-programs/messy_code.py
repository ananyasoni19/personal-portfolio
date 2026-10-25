"""
Messy code vs clean code
This file shows the same task twice: find the average of a list of numbers.

1. A messy version (harder to read)
2. A clean version (easier to read and reuse)
"""


# ---------------------------------------------------------------------------
# MESSY VERSION
# Problems: short/unclear names, repeated work, no function, magic numbers
# ---------------------------------------------------------------------------

a = [10, 20, 30, 40, 50]
# Adding each number by hand instead of using a loop
x = a[0] + a[1] + a[2] + a[3] + a[4]
# Dividing by 5 instead of using the real length of the list
y = x / 5
print("Messy version average:", y)


# ---------------------------------------------------------------------------
# CLEAN VERSION
# Improvements:
# - Meaningful names (numbers, total, average) so the code explains itself
# - A function so we can reuse the same logic with any list
# - A loop instead of listing every index
# - len(numbers) instead of hard-coding 5
# ---------------------------------------------------------------------------

def calculate_average(numbers):
    """Return the average of a list of numbers. Return 0 if the list is empty."""
    if len(numbers) == 0:
        print("Cannot calculate an average of an empty list.")
        return 0

    total = 0
    for number in numbers:
        total = total + number

    average = total / len(numbers)
    return average


sample_scores = [10, 20, 30, 40, 50]
clean_average = calculate_average(sample_scores)
print("Clean version average:", clean_average)
