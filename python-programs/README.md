# Python Programs Collection

A small beginner-friendly set of Python programs. Each file is independent and can be run on its own.

## Requirements

- **Python 3.8 or newer** (any recent Python 3 version is fine)
- No extra packages — only the Python standard library

Check your version:

```bash
python --version
```

On some systems you may need `python3` instead of `python`.

---

## 1. `factorial.py`

**Purpose:** Calculates the factorial of a non-negative integer (for example, `5! = 120`).

**What it does:**
- Asks you to type a number
- Rejects empty input, letters, decimals, and negative numbers
- Prints the factorial result

**How to run (exact steps):**

1. Open a terminal.
2. Change to this folder:

```bash
cd python-programs
```

3. Start the program:

```bash
python factorial.py
```

4. When prompted, type a whole number (example: `5`) and press Enter.

**Example session:**

```text
Enter a non-negative integer: 5
5! = 120
```

---

## 2. `fibonacci.py`

**Purpose:** Prints the first *n* numbers of the Fibonacci sequence (`0, 1, 1, 2, 3, 5, ...`).

**What it does:**
- Asks how many terms you want
- Rejects empty input, letters, decimals, negatives, and zero
- Prints the sequence as a comma-separated list

**How to run (exact steps):**

1. Open a terminal.
2. Change to this folder:

```bash
cd python-programs
```

3. Start the program:

```bash
python fibonacci.py
```

4. When prompted, type how many terms you want (example: `7`) and press Enter.

**Example session:**

```text
How many Fibonacci terms do you want? 7
Fibonacci sequence:
0, 1, 1, 2, 3, 5, 8
```

---

## 3. `structure_to_dictionary.py`

**Purpose:** Shows how to convert simple structures into a Python dictionary:
1. A list of `(key, value)` pairs → dictionary
2. Two parallel lists (keys and values) → dictionary

**What it does:**
- Skips incomplete pairs
- Reports an error when list lengths do not match
- Reports an error when the input type is wrong
- Runs a short demo automatically (no typing required)

**How to run (exact steps):**

1. Open a terminal.
2. Change to this folder:

```bash
cd python-programs
```

3. Start the program:

```bash
python structure_to_dictionary.py
```

4. Read the printed demo output. No extra input is needed.

---

## If `python` is not found

Use `python3` instead:

```bash
python3 factorial.py
python3 fibonacci.py
python3 structure_to_dictionary.py
```

## Tips

- For `factorial.py` and `fibonacci.py`, type a whole number and press Enter.
- Read the comments inside each `.py` file — they explain the steps in plain language.
