"""
EXERCISE SOLUTIONS - Lessons 1 & 2
==================================

Here are the solutions to the exercises from your first two lessons.
Try to solve them yourself first, then check your answers here!
"""

print("=== LESSON 1 EXERCISE SOLUTIONS ===\n")

# Exercise 1: Personal Introduction
print("1. Personal Introduction")
print("Hi! I'm Alice, I'm 25 years old, and I love programming")
# Your solution might look different - that's perfectly fine!

# Exercise 2: Simple Math - Rectangle Area
print("\n2. Rectangle Area Calculation")
length = 10
width = 5
area = length * width
print(f"Rectangle with length {length} and width {width} has area: {area}")

# Exercise 3: Temperature Conversion
print("\n3. Temperature Conversion")
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")

print("\n" + "="*50)
print("=== LESSON 2 EXERCISE SOLUTIONS ===\n")

# Exercise 1: Personal Profile
print("1. Personal Profile")
my_name = "John"
my_age = 28
my_city = "New York"
my_favorite_color = "blue"

introduction = f"Hello! My name is {my_name}, I'm {my_age} years old, I live in {my_city}, and my favorite color is {my_favorite_color}."
print(introduction)

# Exercise 2: Variable Calculator
print("\n2. Variable Calculator")
num1 = 15
num2 = 4

print(f"Numbers: {num1} and {num2}")
print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
print(f"Division: {num1} / {num2} = {num1 / num2}")
print(f"Modulo: {num1} % {num2} = {num1 % num2}")

# Exercise 3: Type Conversions
print("\n3. Type Conversions")
# Convert "3.14" to a float
pi_string = "3.14"
pi_float = float(pi_string)
print(f"String '{pi_string}' converted to float: {pi_float}")

# Convert 42 to a string
answer = 42
answer_string = str(answer)
print(f"Integer {answer} converted to string: '{answer_string}'")

# Convert "True" to a boolean (tricky!)
# Note: bool("True") will always return True because any non-empty string is truthy
# To properly convert string "True"/"False" to boolean, you need:
bool_string = "True"
bool_value = bool_string == "True"  # or use eval() but it's not recommended
print(f"String '{bool_string}' converted to boolean: {bool_value}")

# Alternative method using eval (be careful with eval!)
# bool_value_alt = eval(bool_string.lower().capitalize())
# print(f"Alternative conversion: {bool_value_alt}")

# Exercise 4: String Manipulations
print("\n4. String Manipulations")
favorite_movie = "The Matrix"
print(f"Original: {favorite_movie}")
print(f"Uppercase: {favorite_movie.upper()}")
print(f"Lowercase: {favorite_movie.lower()}")
print(f"Length: {len(favorite_movie)} characters")

print("\n🎉 Great job working through these exercises!")
print("Remember: There are often multiple correct ways to solve a problem in Python!")