# Exercise 04 — What is it ?

`whatis.py` checks the argument passed on the command line, validates that it is a single integer, then prints whether that number is even or odd.

## Script behavior

- If more than one argument is provided, it prints `AssertionError: more than one argument is provided`.
- If the argument is not a valid integer (optionally signed), it prints `AssertionError: argument is not an integer`.
- If the argument is a valid integer, it prints `I'm Even.` or `I'm Odd.` depending on its parity.
- The script always exits after printing, no additional output is produced.

## Usage

From the repository root run:

```
python ex04\whatis.py <integer>
```

Examples:

```
python ex04\whatis.py 42
> I'm Even.

python ex04\whatis.py -5
> I'm Odd.
```

Use any signed or unsigned integer as input. Invalid inputs or missing arguments trigger the `AssertionError` messages described above.
