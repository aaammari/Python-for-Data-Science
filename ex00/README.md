# Exercise 00 — First Python Script

This exercise requires updating simple Python data structures so that they print the expected greetings when the script is executed.

## Task

1. Edit `Hello.py` so that the following data objects hold the intended values:
   - `ft_list`: `"Hello"` followed by `"World!"`
   - `ft_tuple`: `"Hello"` followed by the country name of your campus (e.g. `"France!"`)
   - `ft_set`: `"Hello"` followed by the city name of your campus (e.g. `"Paris!"`). Keep in mind that sets are unordered, so the output order is not deterministic.
   - `ft_dict`: `"Hello"` mapped to the name of your campus (e.g. `"42Paris!"`)
2. Print each structure as shown in the starter script. The script must remain readable and keep the same print order.

## Running the script

From the repository root, run:

```
python ex00\Hello.py
```

The output should look like:

```
['Hello', 'World!']
('Hello', 'France!')
{'Hello', 'Paris!'}
{'Hello': '42Paris!'}
```

(Replace the country/city/campus values with your own campus information.)
