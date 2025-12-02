# Exercise 05 — First standalone program python

`building.py` analyzes the text you supply either as a command-line argument or via an interactive prompt. The script counts the total number of characters, upper-case letters, lower-case letters, punctuation marks, spaces (including the final carriage return entered by the user), and digits.

## Behavior

- When invoked with exactly one argument, the script uses that argument as the text to analyze.
- When invoked with no arguments or with an empty argument string, the script prints `What is the text to count?` and reads a single line from the user. (The carriage return is treated as a space, matching the exercise example.)
- When more than one argument is provided, it prints `AssertionError: more than one argument is provided` and exits without counting.
- The script always prints the results in this exact order:
  1. `The text contains X characters:`
  2. `Y upper letters`
  3. `Z lower letters`
  4. `P punctuation marks`
  5. `Q spaces`
  6. `D digits`

## Usage

```
python ex05\building.py "Python 3.0, released in 2008, was a major revision..."
```

Output example (the numbers will depend on the exact text):

```
The text contains 171 characters:
2 upper letters
121 lower letters
7 punctuation marks
26 spaces
15 digits
```

```
python ex05\building.py
What is the text to count?
Hello World!
The text contains 13 characters:
2 upper letters
8 lower letters
1 punctuation marks
2 spaces
0 digits
```
