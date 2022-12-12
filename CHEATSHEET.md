Open `input.txt` read-only as a file object named `input`:
`with open('input.txt', 'r') as input:` 

Populate a Python list with each line of the `input` file object:
`list = input.readlines()` 

Strip newlines from a line:
```
test_string = "\nI'm a string!\n"
test_string.strip('\n')
print(test_string)
I'm a string!
```

Use `splitlines()` to strip `\n` at the same time

For loop where `i` = the current line of the thing you're iterating through:
```
for i in array:
```

Cacluclate offsets (`ord()` for characters, for example)

List comprehensions (`i for i in list` type shit)

multiply all values in a set into a "supermodulo" and use modulo to "clamp" number sizes 