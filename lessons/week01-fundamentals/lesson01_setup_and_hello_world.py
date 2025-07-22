"""
LESSON 1: Python Setup and Hello World
=====================================

Welcome to your first Python lesson! In this lesson, you'll learn:
1. Understanding Python and why it's popular
2. Writing your first Python program
3. Understanding Python syntax basics
4. Running Python code in different ways

Let's start your Python journey! 🚀
"""

# ============================================================================
# PART 1: WHAT IS PYTHON?
# ============================================================================

"""
Python is a high-level, interpreted programming language created by Guido van Rossum
and first released in 1991. It's known for:

✅ Simple and readable syntax
✅ Versatile - used for web development, data science, AI, automation, etc.
✅ Large community and extensive libraries
✅ Cross-platform compatibility
✅ Great for beginners and professionals alike

Python follows the philosophy: "Simple is better than complex"
"""

# ============================================================================
# PART 2: YOUR FIRST PYTHON PROGRAM
# ============================================================================

# This is a comment - Python ignores everything after the # symbol
print("Hello, World!")  # This prints text to the screen

# You can print multiple things
print("Welcome to Python!")
print("Let's start coding!")

# ============================================================================
# PART 3: BASIC OUTPUT WITH PRINT()
# ============================================================================

# The print() function displays output to the console
print("This is a simple message")

# You can print numbers too
print(42)
print(3.14159)

# Print multiple items separated by spaces
print("My name is", "Python", "and I'm", 32, "years old")

# Print with custom separators
print("Apple", "Banana", "Orange", sep=" - ")

# Print without a newline at the end
print("This is on one line", end=" ")
print("and this continues on the same line")

# ============================================================================
# PART 4: BASIC INPUT WITH INPUT()
# ============================================================================

# Get input from the user (uncomment to try - commented out for batch running)
# name = input("What's your name? ")
# print("Hello,", name, "!")

# age = input("How old are you? ")
# print("You are", age, "years old!")

# ============================================================================
# PART 5: PYTHON AS A CALCULATOR
# ============================================================================

print("\n=== Python as a Calculator ===")

# Basic arithmetic operations
print("Addition: 5 + 3 =", 5 + 3)
print("Subtraction: 10 - 4 =", 10 - 4)
print("Multiplication: 6 * 7 =", 6 * 7)
print("Division: 15 / 4 =", 15 / 4)
print("Integer Division: 15 // 4 =", 15 // 4)
print("Remainder (Modulo): 15 % 4 =", 15 % 4)
print("Exponentiation: 2 ** 8 =", 2 ** 8)

# ============================================================================
# EXERCISES FOR YOU TO TRY
# ============================================================================

print("\n=== EXERCISES ===")
print("Try these exercises by modifying the code below:")

# Exercise 1: Personal Introduction
print("\n1. Create a personal introduction")
# TODO: Print your name, age, and favorite hobby
# Example: print("Hi! I'm [Your Name], I'm [Age] years old, and I love [Hobby]")

# Exercise 2: Simple Math
print("\n2. Calculate the area of a rectangle")
length = 10
width = 5
# TODO: Calculate and print the area (length * width)

# Exercise 3: Temperature Conversion
print("\n3. Convert Celsius to Fahrenheit")
celsius = 25
# TODO: Convert celsius to fahrenheit using the formula: (celsius * 9/5) + 32
# Print both the celsius and fahrenheit values

# ============================================================================
# IMPORTANT PYTHON CONCEPTS FROM THIS LESSON
# ============================================================================

"""
KEY CONCEPTS LEARNED:

1. COMMENTS: Use # for single-line comments, ''' or \"\"\" for multi-line

2. PRINT FUNCTION: 
   - print("text") displays text
   - print(variable) displays variable value
   - print("text", variable) displays both

3. BASIC OPERATORS:
   + (addition)
   - (subtraction)
   * (multiplication)
   / (division - gives decimal result)
   // (integer division - gives whole number)
   % (modulo - gives remainder)
   ** (exponentiation - power)

4. PYTHON PHILOSOPHY: Code should be readable and simple

NEXT LESSON: We'll learn about variables and data types!
"""

# Run this file to see the output!
if __name__ == "__main__":
    print("\n🎉 Congratulations! You've completed your first Python lesson!")
    print("Next: Learn about variables and data types in lesson02_variables.py")