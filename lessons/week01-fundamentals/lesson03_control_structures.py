"""
LESSON 3: Control Structures
===========================

In this lesson, you'll learn:
1. Making decisions with if/else statements
2. Comparison and logical operators
3. Repeating actions with loops (for and while)
4. Controlling loop flow (break and continue)
5. Nested structures

Control structures let your programs make decisions and repeat actions! 🔄
"""

# ============================================================================
# PART 1: IF/ELSE STATEMENTS - MAKING DECISIONS
# ============================================================================

print("=== Making Decisions with if/else ===")

# Basic if statement
age = 18
if age >= 18:
    print("You are an adult!")

# if/else statement
temperature = 75
if temperature > 80:
    print("It's hot outside!")
else:
    print("It's not too hot.")

# if/elif/else statement (multiple conditions)
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# ============================================================================
# PART 2: COMPARISON OPERATORS
# ============================================================================

print("\n=== Comparison Operators ===")

a = 10
b = 5

print(f"a = {a}, b = {b}")
print(f"a == b: {a == b}")  # Equal to
print(f"a != b: {a != b}")  # Not equal to
print(f"a > b: {a > b}")    # Greater than
print(f"a < b: {a < b}")    # Less than
print(f"a >= b: {a >= b}")  # Greater than or equal
print(f"a <= b: {a <= b}")  # Less than or equal

# ============================================================================
# PART 3: LOGICAL OPERATORS
# ============================================================================

print("\n=== Logical Operators ===")

# AND operator - both conditions must be True
age = 25
has_license = True
if age >= 18 and has_license:
    print("You can drive!")

# OR operator - at least one condition must be True
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")

# NOT operator - reverses the boolean value
is_raining = False
if not is_raining:
    print("Great weather for a walk!")

# Complex logical expressions
temperature = 72
is_sunny = True
if temperature > 70 and is_sunny and not is_raining:
    print("Perfect day for a picnic!")

# ============================================================================
# PART 4: FOR LOOPS - REPEATING ACTIONS
# ============================================================================

print("\n=== For Loops ===")

# Loop through a range of numbers
print("Counting from 1 to 5:")
for i in range(1, 6):  # range(start, stop) - stop is not included
    print(f"Count: {i}")

# Loop through a string
word = "Python"
print(f"\nLetters in '{word}':")
for letter in word:
    print(f"Letter: {letter}")

# Loop through a list
fruits = ["apple", "banana", "orange", "grape"]
print("\nFruits in my basket:")
for fruit in fruits:
    print(f"- {fruit}")

# Loop with enumerate (get index and value)
print("\nFruits with index:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# ============================================================================
# PART 5: WHILE LOOPS - REPEAT WHILE CONDITION IS TRUE
# ============================================================================

print("\n=== While Loops ===")

# Basic while loop
count = 1
print("Counting with while loop:")
while count <= 3:
    print(f"Count: {count}")
    count += 1  # Same as count = count + 1

# While loop with user input simulation
attempts = 0
max_attempts = 3
password = "secret"

print(f"\nPassword attempts (simulated):")
while attempts < max_attempts:
    attempts += 1
    # Simulating different password attempts
    if attempts == 1:
        guess = "wrong"
    elif attempts == 2:
        guess = "incorrect"
    else:
        guess = "secret"
    
    print(f"Attempt {attempts}: Trying password '{guess}'")
    
    if guess == password:
        print("Access granted!")
        break  # Exit the loop early
    else:
        print("Wrong password!")

# ============================================================================
# PART 6: LOOP CONTROL - BREAK AND CONTINUE
# ============================================================================

print("\n=== Loop Control: break and continue ===")

# Using break to exit early
print("Finding the first even number:")
for num in [1, 3, 5, 8, 9, 10]:
    if num % 2 == 0:  # If number is even
        print(f"Found even number: {num}")
        break  # Stop the loop
    print(f"Checking: {num} (odd)")

# Using continue to skip iterations
print("\nPrinting only positive numbers:")
numbers = [-2, -1, 0, 1, 2, 3]
for num in numbers:
    if num <= 0:
        continue  # Skip the rest of this iteration
    print(f"Positive: {num}")

# ============================================================================
# PART 7: NESTED STRUCTURES
# ============================================================================

print("\n=== Nested Structures ===")

# Nested if statements
age = 16
has_permit = True

if age >= 15:
    if has_permit:
        print("You can drive with supervision!")
    else:
        print("You need to get a learner's permit first.")
else:
    print("You're too young to drive.")

# Nested loops
print("\nMultiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"{i} x {j} = {result}")

# ============================================================================
# PART 8: PRACTICAL EXAMPLES
# ============================================================================

print("\n=== Practical Examples ===")

# Example 1: Number guessing game logic
secret_number = 7
guess = 5  # Simulated guess

if guess == secret_number:
    print("Congratulations! You guessed it!")
elif guess < secret_number:
    print("Too low! Try higher.")
else:
    print("Too high! Try lower.")

# Example 2: Grade calculator
grades = [85, 92, 78, 96, 88]
total = 0
count = 0

for grade in grades:
    total += grade
    count += 1

average = total / count
print(f"\nGrades: {grades}")
print(f"Average: {average:.1f}")

if average >= 90:
    print("Overall grade: A")
elif average >= 80:
    print("Overall grade: B")
else:
    print("Overall grade: C")

# ============================================================================
# EXERCISES FOR YOU TO TRY
# ============================================================================

print("\n=== EXERCISES ===")

# Exercise 1: Age classifier
print("\n1. Age Classifier")
# TODO: Write code that classifies age into categories:
# 0-12: Child, 13-19: Teenager, 20-59: Adult, 60+: Senior
user_age = 25  # Change this value to test

# Exercise 2: Even/Odd checker
print("\n2. Even/Odd Numbers")
# TODO: Print numbers 1-10, but label each as "even" or "odd"
# Example output: "1 is odd", "2 is even", etc.

# Exercise 3: Password strength checker
print("\n3. Password Strength")
# TODO: Check if a password is strong based on these criteria:
# - At least 8 characters long
# - Contains both letters and numbers
# Hint: Use len() for length, .isalpha() and .isdigit() for checking characters
test_password = "abc123xyz"

# Exercise 4: Sum of numbers
print("\n4. Sum Calculator")
# TODO: Calculate the sum of numbers from 1 to 100 using a loop

# Exercise 5: Pattern printing
print("\n5. Pattern Printing")
# TODO: Print this pattern using nested loops:
# *
# **
# ***
# ****
# *****

# ============================================================================
# KEY CONCEPTS SUMMARY
# ============================================================================

"""
KEY CONCEPTS LEARNED:

1. IF/ELSE STATEMENTS:
   - if condition: (execute if True)
   - elif condition: (else if)
   - else: (execute if all conditions are False)

2. COMPARISON OPERATORS:
   ==, !=, >, <, >=, <=

3. LOGICAL OPERATORS:
   - and (both must be True)
   - or (at least one must be True)
   - not (reverses boolean value)

4. FOR LOOPS:
   - for item in sequence:
   - range(start, stop, step)
   - enumerate() for index and value

5. WHILE LOOPS:
   - while condition:
   - Continues until condition becomes False

6. LOOP CONTROL:
   - break: Exit loop early
   - continue: Skip current iteration

7. NESTING:
   - You can put if statements inside loops
   - You can put loops inside if statements
   - You can nest loops inside loops

NEXT LESSON: Functions and scope!
"""

if __name__ == "__main__":
    print("\n🎉 Excellent! You've mastered control structures!")
    print("Next: Learn about functions in lesson04_functions.py")