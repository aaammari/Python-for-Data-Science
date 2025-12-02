# Exercise 02 — First function python

Implement the `all_thing_is_obj` function in `find_ft_type.py` so it prints descriptive lines for several object types before returning `42`.

## Task

1. Inside `all_thing_is_obj`, inspect the object’s type using `isinstance` checks (or equivalent).
2. Print the following strings based on the input:
   - Lists: `List : <class 'list'>`
   - Tuples: `Tuple : <class 'tuple'>`
   - Sets: `Set : <class 'set'>`
   - Dicts: `Dict : <class 'dict'>`
   - Strings: `<value> is in the kitchen : <class 'str'>` (where `<value>` is the string argument)
   - Other types: `Type not found`
3. Always return `42` from the function.

## Running the test script

From the repository root run:

```
python ex02\test.py
```

The script prints each type description followed by `42` for the final call. If the printed descriptions match the format above, the implementation is correct.
