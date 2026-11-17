# Day-01: Python Fundamentals

## Topics Covered

- Variables
- Data Types
- Variable Declaration and Assignment
- `print()` Function
- `type()` Function
- Comments
- Dynamic Typing
- String Concatenation and Multiple Arguments in `print()`

---

## 1. Variables in Python

A variable is a name used to store or refer to a value in a program.

Example:

```python
name = "Akshat Johri"
age = 21
height = 5.10
learningPython = True
course = "AI Learning"
```

Here:
- `name` stores a string.
- `age` stores an integer.
- `height` stores a floating-point number.
- `learningPython` stores a Boolean value.
- `course` stores a string.

The `=` operator is called the assignment operator. It assigns a value to a variable name.

## 2. Data Types in Python

A data type defines the kind of value an object represents.

The basic Python data types covered today are:

| Data Type | Description | Example |
|---|---|---|
| `int` | Integer numbers | `21` |
| `float` | Decimal numbers | `5.10` |
| `str` | Text or strings | `"Python"` |
| `bool` | Boolean values | `True`, `False` |

### Important observations

- Values written inside quotation marks are treated as strings.
- Numbers without decimal points are generally integers.
- Numbers with decimal points are floating-point numbers.
- Boolean values must be written as `True` or `False`, with capital first letters.

Examples:

```python
age = 21       # int
age = "21"     # str
height = 5.10  # float
isLearning = True  # bool
```

Although `21` and `"21"` look similar, Python treats them as different data types.

## 3. The print() Function

The `print()` function displays information in the output.

Example:

```python
print("Hello Python")
print("Age:", age)
```

There are two ways to display a variable alongside text.

### Method 1: String concatenation

```python
print("Name: " + name)
```

The `+` operator joins two strings.

If we want to concatenate a number with a string, we need to convert the number into a string first:

```python
print("Age: " + str(age))
```

### Method 2: Passing multiple arguments

```python
print("Age:", age)
print("Height:", height)
print("Learning Python:", learningPython)
```

The comma separates arguments passed to `print()`.

Python displays these arguments with a space between them by default. This method also allows us to print different data types without manually converting them into strings.

## 4. The type() Function

The `type()` function tells us the data type of a value or object.

Example:

```python
name = "Akshat Johri"
age = 21
height = 5.10
learningPython = True

print(type(name))
print(type(age))
print(type(height))
print(type(learningPython))
```

Expected output:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

This function is useful when checking what kind of data a variable currently refers to.

## 5. Comments in Python

Comments are notes written in code for developers.

Python ignores comments during normal program execution.

A single-line comment starts with `#`.

Example:

```python
# This is a comment
name = "Akshat Johri"

# Display the student's name
print(name)
```

Comments help make code easier to understand and maintain.

## 6. Dynamic Typing in Python

Python is a dynamically typed language.

This means a variable name can refer to objects of different data types at different points during program execution.

Example:

```python
x = 10
print(type(x))

x = "Hello"
print(type(x))

x = 10.5
print(type(x))
```

Output:

```text
<class 'int'>
<class 'str'>
<class 'float'>
```

The type changes because the name `x` is reassigned to different objects.

**Important:** In Python, the type belongs to the object, not permanently to the variable name.

## 7. Day-01 Practical Implementation

The practical exercise was to create a Student Profile Generator.

The program:
1. Declares variables for student information.
2. Prints a student profile.
3. Displays the data type of each variable.
4. Uses comments to organize the code.

The implementation is available in `practice.py` in this folder.

---

## Key Takeaways

- Variables are names that refer to values.
- Python supports different built-in data types, including `int`, `float`, `str`, and `bool`.
- `print()` displays values.
- `type()` identifies an object's data type.
- Comments begin with `#`.
- Quotation marks make a value a string.
- `print()` can accept multiple arguments separated by commas.
- Python supports dynamic typing, allowing a variable name to be reassigned to objects of different types.

## Day-01 Status

**Completed:** Basic variables, data types, printing, comments, type checking, and introductory dynamic typing.

**Next:** Continue with the next concepts in the Python learning playlist.
