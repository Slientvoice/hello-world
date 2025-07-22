"""
PYTHON QUICK REFERENCE GUIDE
============================

A comprehensive cheat sheet for Python fundamentals.
Keep this handy as you progress through your Python journey!
"""

# ============================================================================
# BASIC SYNTAX
# ============================================================================

# Comments
# This is a single-line comment
"""
This is a
multi-line comment
"""

# Printing output
print("Hello, World!")
print("Value:", 42)
print("Multiple", "values", sep="-")

# Getting input
# name = input("Enter your name: ")

# ============================================================================
# VARIABLES AND DATA TYPES
# ============================================================================

# Variable assignment
name = "Alice"          # String
age = 25               # Integer
height = 5.6           # Float
is_student = True      # Boolean
nothing = None         # None type

# Type checking
print(type(name))           # <class 'str'>
print(isinstance(age, int)) # True

# Type conversion
str_num = "123"
int_num = int(str_num)      # String to integer
float_num = float(str_num)  # String to float
str_age = str(age)          # Integer to string

# ============================================================================
# OPERATORS
# ============================================================================

# Arithmetic operators
result = 10 + 5    # Addition (15)
result = 10 - 5    # Subtraction (5)
result = 10 * 5    # Multiplication (50)
result = 10 / 5    # Division (2.0)
result = 10 // 3   # Floor division (3)
result = 10 % 3    # Modulo/remainder (1)
result = 10 ** 2   # Exponentiation (100)

# Comparison operators
10 == 5    # Equal to (False)
10 != 5    # Not equal to (True)
10 > 5     # Greater than (True)
10 < 5     # Less than (False)
10 >= 5    # Greater than or equal (True)
10 <= 5    # Less than or equal (False)

# Logical operators
True and False   # False
True or False    # True
not True        # False

# Assignment operators
x = 5
x += 3    # x = x + 3 (8)
x -= 2    # x = x - 2 (6)
x *= 2    # x = x * 2 (12)
x /= 3    # x = x / 3 (4.0)

# ============================================================================
# STRINGS
# ============================================================================

# String creation
text = "Hello"
text = 'Hello'
text = """Multi-line
string"""

# String operations
text = "Python"
print(len(text))           # Length: 6
print(text.upper())        # PYTHON
print(text.lower())        # python
print(text.replace("P", "J"))  # Jython

# String formatting
name = "Alice"
age = 25
# F-strings (preferred)
message = f"Hi {name}, you are {age} years old"
# Format method
message = "Hi {}, you are {} years old".format(name, age)
# % formatting (old style)
message = "Hi %s, you are %d years old" % (name, age)

# String indexing and slicing
text = "Python"
print(text[0])      # P (first character)
print(text[-1])     # n (last character)
print(text[1:4])    # yth (slice from index 1 to 3)
print(text[:3])     # Pyt (first 3 characters)
print(text[3:])     # hon (from index 3 to end)

# ============================================================================
# CONTROL STRUCTURES
# ============================================================================

# If statements
age = 18
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# For loops
# Range
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8
    print(i)

# Iterate over string
for char in "Hello":
    print(char)

# Iterate over list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# Enumerate (get index and value)
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# While loops
count = 0
while count < 3:
    print(count)
    count += 1

# Loop control
for i in range(10):
    if i == 3:
        continue    # Skip this iteration
    if i == 7:
        break      # Exit the loop
    print(i)

# ============================================================================
# DATA STRUCTURES
# ============================================================================

# Lists (mutable, ordered)
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# List operations
numbers.append(6)           # Add to end
numbers.insert(0, 0)        # Insert at index
numbers.remove(3)           # Remove first occurrence
popped = numbers.pop()      # Remove and return last item
numbers.sort()              # Sort in place
numbers.reverse()           # Reverse in place

# List indexing and slicing (same as strings)
print(numbers[0])           # First item
print(numbers[-1])          # Last item
print(numbers[1:3])         # Slice

# Tuples (immutable, ordered)
coordinates = (10, 20)
rgb = (255, 128, 0)

# Dictionaries (key-value pairs)
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Dictionary operations
print(person["name"])       # Access value
person["age"] = 26         # Update value
person["country"] = "USA"  # Add new key-value pair
del person["city"]         # Delete key-value pair

# Dictionary methods
print(person.keys())       # Get all keys
print(person.values())     # Get all values
print(person.items())      # Get all key-value pairs

# Sets (unique items, unordered)
unique_numbers = {1, 2, 3, 4, 5}
unique_numbers.add(6)      # Add item
unique_numbers.remove(3)   # Remove item

# ============================================================================
# FUNCTIONS
# ============================================================================

# Function definition
def greet(name):
    return f"Hello, {name}!"

# Function with default parameter
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}!"

# Function with multiple parameters
def calculate_area(length, width):
    return length * width

# Function calls
message = greet("Alice")
message = greet_with_title("Smith")
message = greet_with_title("Johnson", "Dr.")
area = calculate_area(10, 5)

# ============================================================================
# COMMON BUILT-IN FUNCTIONS
# ============================================================================

# Math functions
abs(-5)         # Absolute value: 5
min(1, 2, 3)    # Minimum: 1
max(1, 2, 3)    # Maximum: 3
sum([1, 2, 3])  # Sum: 6
round(3.7)      # Round: 4
len("hello")    # Length: 5

# Type functions
int("123")      # Convert to integer
float("3.14")   # Convert to float
str(123)        # Convert to string
list("hello")   # Convert to list: ['h', 'e', 'l', 'l', 'o']

# Useful functions
range(5)        # Generate sequence: 0, 1, 2, 3, 4
enumerate([1, 2, 3])  # Get index and value pairs
zip([1, 2], ['a', 'b'])  # Combine lists: [(1, 'a'), (2, 'b')]

# ============================================================================
# FILE OPERATIONS
# ============================================================================

# Reading files
with open("filename.txt", "r") as file:
    content = file.read()           # Read entire file
    lines = file.readlines()        # Read all lines as list

# Writing files
with open("filename.txt", "w") as file:
    file.write("Hello, World!")     # Write string
    file.writelines(["Line 1\n", "Line 2\n"])  # Write list of strings

# ============================================================================
# ERROR HANDLING
# ============================================================================

# Try-except blocks
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid value!")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No errors occurred")
finally:
    print("This always executes")

# ============================================================================
# LIST COMPREHENSIONS
# ============================================================================

# Basic list comprehension
squares = [x**2 for x in range(5)]        # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# ============================================================================
# USEFUL STRING METHODS
# ============================================================================

text = "  Hello, World!  "
text.strip()           # Remove whitespace: "Hello, World!"
text.split(",")        # Split into list: ["  Hello", " World!  "]
"_".join(["a", "b"])   # Join with separator: "a_b"
text.startswith("He")  # Check if starts with: False (due to spaces)
text.endswith("!")     # Check if ends with: False (due to spaces)
text.find("World")     # Find substring position: 9
text.count("l")        # Count occurrences: 3

# ============================================================================
# COMMON PATTERNS
# ============================================================================

# Check if variable exists and has value
if 'variable_name' in locals() and variable_name:
    print("Variable exists and is truthy")

# Multiple assignment
a, b, c = 1, 2, 3
a, b = b, a  # Swap values

# Check if list is empty
my_list = []
if not my_list:  # or: if len(my_list) == 0:
    print("List is empty")

# Iterate with index
for i, item in enumerate(['a', 'b', 'c']):
    print(f"{i}: {item}")

# ============================================================================
# DEBUGGING TIPS
# ============================================================================

# Print debugging
print(f"Debug: variable = {variable}")

# Check type and value
print(f"Type: {type(variable)}, Value: {variable}")

# Print with separator for clarity
print("="*50)
print("Debug information")
print("="*50)

"""
REMEMBER:
- Python is case-sensitive
- Indentation matters (use 4 spaces)
- Use descriptive variable names
- Follow PEP 8 style guide
- Practice regularly!
"""