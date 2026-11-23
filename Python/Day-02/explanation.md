# Day-02: User Input, Type Conversion & Literals

## Topics Covered

- Taking input from the user using `input()`
- Type conversion (type casting)
- `int()`, `float()`, `str()`, and `bool()`
- Checking data types using `type()`
- Python literals
- `None` and `NoneType`
- Basic calculations using user input

---

## 1. Taking Input from the User

In Python, the `input()` function is used to take information from the user while a program is running.

Example:

```python
name = input("Enter your name: ")
print("Welcome", name)
```

### How input() works

1. Python displays the message provided inside `input()`.
2. The program waits for the user to enter something.
3. The user enters a value and presses Enter.
4. Python returns the entered value.
5. The returned value can be stored in a variable.

### Important Point

The `input()` function always returns a string (`str`), even when the user enters a number.

Example:

```python
age = input("Enter your age: ")

print(type(age))
```

If the user enters `22`, the output will be:

```text
<class 'str'>
```

This happens because `input()` treats the entered information as text by default.

---

## 2. Type Conversion (Type Casting)

Type conversion means converting a value from one data type to another.

Python provides several built-in functions for type conversion.

| Function | Purpose | Example |
|---|---|---|
| `int()` | Converts into an integer | `int("22")` |
| `float()` | Converts into a float | `float("5.10")` |
| `str()` | Converts into a string | `str(22)` |
| `bool()` | Converts into a Boolean | `bool(1)` |

### Why is type conversion needed?

Since `input()` returns a string, mathematical calculations require us to convert numeric input into an appropriate numeric type.

Example:

```python
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
```

Here:
- `int()` converts the entered age into an integer.
- `float()` converts the entered height into a floating-point number.

### Example: Age Calculator

```python
age = int(input("Enter your age: "))

later_age = age + 5

print("Your age after five years:", later_age)
```

If the user enters `22`, the output will be:

```text
Your age after five years: 27
```

### Invalid Type Conversion

Not every value can be converted into every data type.

Example:

```python
age = int("22")      # Valid
age = int("Python")  # ValueError
```

Python raises a `ValueError` because `"Python"` cannot be interpreted as an integer.

---

## 3. Boolean Type Conversion

The `bool()` function converts a value into either `True` or `False`.

Examples:

```python
print(bool(1))       # True
print(bool(0))       # False
print(bool(""))      # False
print(bool("Hello")) # True
print(bool("False")) # True
```

### Important Observation

A non-empty string is considered truthy, even if its contents are `"False"`.

Similarly:
- `0` is falsy.
- An empty string is falsy.
- Non-zero numbers are truthy.
- Non-empty strings are truthy.

This behaviour is useful when working with conditions and Boolean logic.

---

## 4. Literals in Python

A literal is a value written directly in Python source code.

Example:

```python
price = 1500
name = "Akshat"
learning_python = True
completed_python = None
```

Here:

| Variable | Literal | Data Type |
|---|---|---|
| `price` | `1500` | `int` |
| `name` | `"Akshat"` | `str` |
| `learning_python` | `True` | `bool` |
| `completed_python` | `None` | `NoneType` |

### Types of Literals

| Literal Type | Examples |
|---|---|
| Integer | `10`, `100`, `-5` |
| Float | `10.5`, `5.10` |
| String | `"Python"`, `'Hello'` |
| Boolean | `True`, `False` |
| Special | `None` |
| Collection | `[1, 2, 3]`, `(1, 2)` |

### Difference Between Variables and Literals

- A variable is a name that refers to an object.
- A literal is a value written directly in the source code.

Example:

```python
price = 1500
```

- `price` is the variable name.
- `1500` is the integer literal.

---

## 5. Understanding None and NoneType

`None` is a special Python value that represents the absence of a value.

Example:

```python
completed_python = None

print(completed_python)
print(type(completed_python))
```

Output:

```text
None
<class 'NoneType'>
```

`None` is commonly used when a value is not available, has not been assigned meaningfully, or a function has no explicit return value.

---

## 6. Practical Implementation

### Personal Information Calculator

The Day-02 practical exercise involved creating a program that:

1. Takes the user's name as input.
2. Takes the user's age as input and converts it into an integer.
3. Takes the user's height as input and converts it into a float.
4. Takes the current course as input.
5. Calculates the user's age after five years.
6. Displays the data types of the entered values.
7. Creates additional variables using integer, string, Boolean, and `None` literals.
8. Prints the values and their corresponding data types.

The implementation is available in `practice.py` in this folder.

---

## 7. Key Takeaways

- `input()` is used to collect information from users.
- `input()` always returns a string by default.
- `int()` converts valid values into integers.
- `float()` converts valid values into floating-point numbers.
- `str()` converts values into strings.
- `bool()` converts values into Boolean values.
- Invalid conversions can raise a `ValueError`.
- Literals are values written directly in source code.
- `None` represents the absence of a value and has the type `NoneType`.
- Type conversion allows us to perform calculations using user-provided numeric input.

## Day-02 Status

**Topics Practised:** User input, type conversion, literals, Boolean conversion, and `None`.

**Next:** Continue with the next concepts in the Python learning playlist.
