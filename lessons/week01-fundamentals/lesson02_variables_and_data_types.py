"""
LESSON 2: Variables and Data Types
=================================

In this lesson, you'll learn:
1. What are variables and how to create them
2. Python's basic data types
3. Type conversion and checking
4. Variable naming conventions
5. Constants and best practices

Variables are containers that store data values! 📦
"""

# ============================================================================
# PART 1: UNDERSTANDING VARIABLES
# ============================================================================

"""
A variable is a named location in memory that stores a value.
Think of it as a labeled box where you can put different things.

In Python, you create variables by simply assigning a value:
variable_name = value
"""

# Creating variables
name = "Alice"
age = 25
height = 5.6
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)

# Variables can be reassigned
age = 26  # Alice had a birthday!
print("Updated age:", age)

# ============================================================================
# PART 2: PYTHON'S BASIC DATA TYPES
# ============================================================================

print("\n=== Basic Data Types ===")

# 1. STRINGS (str) - Text data
first_name = "John"
last_name = 'Doe'  # Single or double quotes both work
full_name = first_name + " " + last_name  # String concatenation
print("String example:", full_name)

# 2. INTEGERS (int) - Whole numbers
score = 95
negative_number = -10
big_number = 1000000
print("Integer examples:", score, negative_number, big_number)

# 3. FLOATS (float) - Decimal numbers
temperature = 98.6
pi = 3.14159
price = 19.99
print("Float examples:", temperature, pi, price)

# 4. BOOLEANS (bool) - True or False
is_sunny = True
is_raining = False
print("Boolean examples:", is_sunny, is_raining)

# 5. NONE TYPE - Represents absence of value
empty_value = None
print("None example:", empty_value)

# ============================================================================
# PART 3: CHECKING DATA TYPES
# ============================================================================

print("\n=== Checking Data Types ===")

# Use type() to check the type of a variable
print("Type of 'Hello':", type("Hello"))
print("Type of 42:", type(42))
print("Type of 3.14:", type(3.14))
print("Type of True:", type(True))
print("Type of None:", type(None))

# Use isinstance() to check if a variable is of a specific type
number = 100
print("Is 'number' an integer?", isinstance(number, int))
print("Is 'number' a string?", isinstance(number, str))

# ============================================================================
# PART 4: TYPE CONVERSION (CASTING)
# ============================================================================

print("\n=== Type Conversion ===")

# Converting between types
num_str = "123"
num_int = int(num_str)  # String to integer
print(f"String '{num_str}' converted to integer: {num_int}")

float_num = 45.67
int_from_float = int(float_num)  # Float to integer (truncates decimal)
print(f"Float {float_num} converted to integer: {int_from_float}")

# Integer to string
age = 25
age_str = str(age)
print(f"Integer {age} converted to string: '{age_str}'")

# String to float
price_str = "19.99"
price_float = float(price_str)
print(f"String '{price_str}' converted to float: {price_float}")

# Boolean conversions
print("int(True):", int(True))    # True becomes 1
print("int(False):", int(False))  # False becomes 0
print("bool(1):", bool(1))        # Non-zero becomes True
print("bool(0):", bool(0))        # Zero becomes False

# ============================================================================
# PART 5: VARIABLE NAMING CONVENTIONS
# ============================================================================

print("\n=== Variable Naming Best Practices ===")

# ✅ Good variable names (descriptive and clear)
user_name = "john_doe"
total_score = 95
is_logged_in = True
MAX_ATTEMPTS = 3  # Constants in ALL_CAPS

# ❌ Bad variable names (avoid these)
# x = "john_doe"  # Not descriptive
# 2name = "John"  # Can't start with number
# user-name = "John"  # Can't use hyphens
# class = "Math"  # Can't use Python keywords

print("Good naming examples:")
print("user_name:", user_name)
print("total_score:", total_score)
print("is_logged_in:", is_logged_in)
print("MAX_ATTEMPTS:", MAX_ATTEMPTS)

# ============================================================================
# PART 6: STRING OPERATIONS AND FORMATTING
# ============================================================================

print("\n=== String Operations ===")

# String methods
message = "Hello, Python World!"
print("Original:", message)
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Length:", len(message))
print("Replace:", message.replace("Python", "Amazing"))

# String formatting (f-strings) - Modern Python way
name = "Alice"
age = 30
# f-strings allow you to embed variables directly in strings
greeting = f"Hi, I'm {name} and I'm {age} years old!"
print("F-string:", greeting)

# Older formatting methods (good to know)
greeting_old = "Hi, I'm {} and I'm {} years old!".format(name, age)
print("Format method:", greeting_old)

# ============================================================================
# EXERCISES FOR YOU TO TRY
# ============================================================================

print("\n=== EXERCISES ===")

# Exercise 1: Personal Profile
print("\n1. Create your personal profile")
# TODO: Create variables for your name, age, city, and favorite color
# Use f-strings to create a nice introduction message

# Exercise 2: Calculator with Variables
print("\n2. Variable calculator")
# TODO: Create variables for two numbers and perform all basic operations
num1 = 15
num2 = 4
# Calculate: addition, subtraction, multiplication, division, and modulo

# Exercise 3: Type Conversions
print("\n3. Practice type conversions")
# TODO: Convert the following and print the results:
# - Convert "3.14" to a float
# - Convert 42 to a string
# - Convert "True" to a boolean (tricky!)

# Exercise 4: String Manipulations
print("\n4. String fun")
favorite_movie = "The Matrix"
# TODO: Print the movie name in uppercase, lowercase, and its length

# ============================================================================
# ADVANCED CONCEPTS (BONUS)
# ============================================================================

print("\n=== BONUS: Advanced Concepts ===")

# Multiple assignment
x, y, z = 1, 2, 3
print("Multiple assignment:", x, y, z)

# Swapping variables
a = 10
b = 20
print("Before swap: a =", a, "b =", b)
a, b = b, a  # Python's elegant way to swap
print("After swap: a =", a, "b =", b)

# Constants (by convention, use ALL_CAPS)
PI = 3.14159
GRAVITY = 9.81
MAX_SPEED = 100

# ============================================================================
# KEY CONCEPTS SUMMARY
# ============================================================================

"""
KEY CONCEPTS LEARNED:

1. VARIABLES: Named containers for storing data
   - Created by assignment: variable_name = value
   - Can be reassigned to new values

2. DATA TYPES:
   - str (string): Text data, use quotes
   - int (integer): Whole numbers
   - float: Decimal numbers
   - bool (boolean): True or False
   - None: Represents no value

3. TYPE CHECKING:
   - type(variable) shows the data type
   - isinstance(variable, type) checks if variable is of specific type

4. TYPE CONVERSION:
   - int(), float(), str(), bool() convert between types
   - Be careful with conversions that might fail

5. NAMING CONVENTIONS:
   - Use descriptive names: user_name not x
   - Use snake_case for variables
   - Use ALL_CAPS for constants
   - Don't use Python keywords

6. STRING FORMATTING:
   - f-strings: f"Hello {name}!" (modern way)
   - .format(): "Hello {}!".format(name) (older way)

NEXT LESSON: Control structures (if/else statements and loops)!
"""

if __name__ == "__main__":
    print("\n🎉 Great job! You've learned about variables and data types!")
    print("Next: Learn about control structures in lesson03_control_structures.py")