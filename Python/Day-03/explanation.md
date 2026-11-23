# Day 03 – Operators, Conditional Statements & While Loops

## 1. Operators in Python

Operators are special symbols or keywords used to perform operations on variables and values.

### 1.1 Arithmetic Operators

Arithmetic operators perform mathematical calculations.

| Operator | Meaning | Example | Output |
|---|---|---|---|
| `+` | Addition | `10 + 5` | `15` |
| `-` | Subtraction | `10 - 5` | `5` |
| `*` | Multiplication | `10 * 5` | `50` |
| `/` | Division | `10 / 5` | `2.0` |
| `//` | Floor division | `11 // 5` | `2` |
| `%` | Modulus | `11 % 5` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

**Important differences:**

- `/` returns the division result as a float.
- `//` returns the floor of the division result.
- `%` returns the remainder.
- `**` calculates the power of a number.

Example:

```python
a = 10
b = 3

print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

Note: Floor division rounds towards negative infinity. For example, `-7 // 2` gives `-4`.

### 1.2 Comparison Operators

Comparison operators compare two values and return a Boolean result (`True` or `False`).

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

Example:

```python
age = 21

print(age == 21)  # True
print(age > 18)   # True
print(age < 18)   # False
```

**Remember:**

- `=` is an assignment operator.
- `==` is a comparison operator.

### 1.3 Logical Operators

Logical operators combine or reverse conditions.

| Operator | Meaning |
|---|---|
| `and` | True when both conditions are True |
| `or` | True when at least one condition is True |
| `not` | Reverses the Boolean result |

Example:

```python
age = 21
has_id = True

print(age >= 18 and has_id)  # True
print(age >= 18 or has_id)   # True
print(not has_id)            # False
```

**Use case:** Voting eligibility can require both an eligible age and valid identification.

### 1.4 Assignment Operators

Assignment operators assign or update variable values.

| Operator | Example | Equivalent operation |
|---|---|---|
| `=` | `x = 10` | Assign 10 |
| `+=` | `x += 5` | `x = x + 5` |
| `-=` | `x -= 5` | `x = x - 5` |
| `*=` | `x *= 2` | `x = x * 2` |
| `/=` | `x /= 2` | `x = x / 2` |
| `//=` | `x //= 2` | `x = x // 2` |
| `%=` | `x %= 2` | `x = x % 2` |
| `**=` | `x **= 2` | `x = x ** 2` |

Example:

```python
x = 10
x += 5

print(x)  # 15
```

### 1.5 Membership Operators

Membership operators check whether an element exists inside a sequence or collection.

- `in`
- `not in`

Example:

```python
name = "Akshat"

print("A" in name)       # True
print("Z" not in name)   # True
```

### 1.6 Identity Operators

Identity operators check whether two variables refer to the same object in memory.

- `is`
- `is not`

Example:

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == c)  # True
print(a is c)  # False
print(a is b)  # True
```

**Important difference:**

- `==` checks whether values are equal.
- `is` checks whether two references point to the same object.

Use `is None` when checking whether a value is `None`.

---

## 2. Conditional Statements

Conditional statements allow a program to make decisions based on conditions.

### 2.1 if Statement

The `if` statement executes a block of code only when its condition is True.

```python
age = 21

if age >= 18:
    print("You are eligible")
```

### 2.2 if-else Statement

The `else` block executes when the `if` condition is False.

```python
age = 16

if age >= 18:
    print("Eligible")
else:
    print("Not eligible")
```

### 2.3 if-elif-else Statement

Used when multiple conditions need to be checked.

Example: Grade calculator.

```python
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")
```

Python checks conditions from top to bottom. Once a condition is True, its block executes and the remaining branches are skipped.

### 2.4 Condition Validation

Always validate input before applying business logic.

```python
marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade A")
else:
    print("Grade B or below")
```

This prevents invalid inputs from receiving incorrect results.

---

## 3. Indentation in Python

Indentation means the spaces at the beginning of a line.

Python uses indentation to define code blocks.

Example:

```python
age = 21

if age >= 18:
    print("You are an adult")
    print("You can vote")

print("Program completed")
```

Here:

- Both statements inside the `if` block are indented.
- The final print statement is outside the `if` block.

**Important rules:**

1. Use four spaces as the standard indentation.
2. Statements belonging to the same block should have the same indentation.
3. A colon (`:`) introduces a block after statements such as `if`, `else`, `elif`, and `while`.
4. Incorrect indentation can cause an `IndentationError`.

Indentation is part of Python's syntax, not just formatting.

---

## 4. While Loops

A loop allows us to execute a block of code repeatedly.

A `while` loop continues executing as long as its condition remains True.

### 4.1 Basic Syntax

```python
while condition:
    # Code to execute
```

### 4.2 Example: Print Numbers from 1 to 5

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

Output:

```text
1
2
3
4
5
```

### 4.3 How a While Loop Works

1. Initialize a variable.
2. Check the condition.
3. If the condition is True, execute the loop body.
4. Update the variable.
5. Check the condition again.
6. Stop when the condition becomes False.

### 4.4 Infinite Loops

An infinite loop occurs when the loop condition never becomes False.

Example:

```python
i = 1

while i <= 5:
    print(i)
```

The value of `i` never changes, so the condition remains True forever.

Correct version:

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

Always make sure the loop has a way to reach its stopping condition.

---

## 5. Accumulator Concept

An accumulator is a variable used to store a running result, such as a sum or product.

Example: Calculate the sum of numbers from 1 to n.

```python
number = int(input("Enter a number: "))

i = 1
total = 0

while i <= number:
    total += i
    i += 1

print("Total:", total)
```

For input `5`:

| Iteration | Current number | Total |
|---|---:|---:|
| 1 | 1 | 1 |
| 2 | 2 | 3 |
| 3 | 3 | 6 |
| 4 | 4 | 10 |
| 5 | 5 | 15 |

**Why initialize `total = 0`?**

The accumulator needs an initial value before we start adding numbers.

Using `total += i` without initializing `total` causes an error because the variable has not been assigned a suitable starting value.

---

## 6. break and continue

These statements control loop execution.

### 6.1 break

`break` immediately terminates the loop.

```python
i = 1

while i <= 10:
    if i == 5:
        break

    print(i)
    i += 1
```

Output:

```text
1
2
3
4
```

### 6.2 continue

`continue` skips the remaining statements in the current iteration and moves to the next iteration.

```python
i = 0

while i < 5:
    i += 1

    if i == 3:
        continue

    print(i)
```

Output:

```text
1
2
4
5
```

**Difference:**

- `break` terminates the entire loop.
- `continue` skips only the current iteration.

---

## 7. Practical Exercises Completed

The following programs were practised during Day-03:

1. Calculator using arithmetic operators.
2. Voting eligibility using conditional statements and logical `and`.
3. Grade calculator using `if-elif-else`.
4. Printing numbers from 1 to n using a `while` loop.
5. Calculating the sum of numbers using an accumulator.
6. Printing even numbers from 1 to 50 using a `while` loop and modulus operator.

### Important edge cases to remember

- Division by zero causes `ZeroDivisionError`.
- Validate yes/no input instead of treating every other response as True.
- Validate marks between 0 and 100.
- Initialize accumulators before using them.
- Update loop counters to prevent infinite loops.

---

## 8. Day-03 Key Takeaways

By studying and practising these concepts, I explored:

- Arithmetic, comparison, logical, assignment, membership and identity operators.
- Difference between assignment (`=`) and comparison (`==`).
- Difference between equality (`==`) and identity (`is`).
- Conditional execution using `if`, `elif` and `else`.
- Importance of indentation in Python.
- Repeated execution using `while` loops.
- Infinite loops and loop termination.
- Accumulators for maintaining running totals.
- Loop control using `break` and `continue`.

**Next:** Continue with the next Python lesson and practise the concepts independently before moving forward.