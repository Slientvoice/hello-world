"""
WEEK 1 PROJECT: Personal Calculator
==================================

This project combines everything you've learned in Week 1:
- Variables and data types
- User input and output
- Arithmetic operations
- Control structures (if/else)
- String formatting

Build a personal calculator that can perform basic operations
and provide a friendly user experience!
"""

def main():
    print("🧮 Welcome to Your Personal Calculator! 🧮")
    print("=" * 50)
    
    # Get user's name for personalization
    name = input("What's your name? ")
    print(f"\nHello, {name}! Let's do some calculations together! 🚀")
    
    # Main calculator loop
    while True:
        print("\n" + "=" * 50)
        print("CALCULATOR MENU")
        print("=" * 50)
        print("1. Basic Calculator")
        print("2. Area Calculator")
        print("3. Temperature Converter")
        print("4. Tip Calculator")
        print("5. Age Calculator")
        print("6. Exit")
        print("=" * 50)
        
        choice = input(f"\n{name}, what would you like to do? (1-6): ")
        
        if choice == "1":
            basic_calculator()
        elif choice == "2":
            area_calculator()
        elif choice == "3":
            temperature_converter()
        elif choice == "4":
            tip_calculator()
        elif choice == "5":
            age_calculator()
        elif choice == "6":
            print(f"\nThanks for using the calculator, {name}! 👋")
            print("Keep practicing Python! 🐍")
            break
        else:
            print("❌ Invalid choice! Please select 1-6.")

def basic_calculator():
    """Perform basic arithmetic operations"""
    print("\n🔢 BASIC CALCULATOR")
    print("-" * 20)
    
    try:
        # Get numbers from user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Show available operations
        print("\nOperations:")
        print("+ : Addition")
        print("- : Subtraction")
        print("* : Multiplication")
        print("/ : Division")
        print("** : Power")
        print("% : Remainder")
        
        operation = input("\nChoose operation (+, -, *, /, **, %): ")
        
        # Perform calculation based on operation
        if operation == "+":
            result = num1 + num2
            print(f"\n✅ {num1} + {num2} = {result}")
        elif operation == "-":
            result = num1 - num2
            print(f"\n✅ {num1} - {num2} = {result}")
        elif operation == "*":
            result = num1 * num2
            print(f"\n✅ {num1} × {num2} = {result}")
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
                print(f"\n✅ {num1} ÷ {num2} = {result}")
            else:
                print("\n❌ Error: Cannot divide by zero!")
        elif operation == "**":
            result = num1 ** num2
            print(f"\n✅ {num1} ^ {num2} = {result}")
        elif operation == "%":
            if num2 != 0:
                result = num1 % num2
                print(f"\n✅ {num1} % {num2} = {result}")
            else:
                print("\n❌ Error: Cannot find remainder with zero!")
        else:
            print("\n❌ Invalid operation!")
            
    except ValueError:
        print("\n❌ Error: Please enter valid numbers!")

def area_calculator():
    """Calculate areas of different shapes"""
    print("\n📐 AREA CALCULATOR")
    print("-" * 18)
    
    print("Choose a shape:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")
    
    shape = input("Enter choice (1-3): ")
    
    try:
        if shape == "1":
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            area = length * width
            print(f"\n✅ Rectangle area: {area} square units")
            
        elif shape == "2":
            radius = float(input("Enter radius: "))
            pi = 3.14159
            area = pi * radius ** 2
            print(f"\n✅ Circle area: {area:.2f} square units")
            
        elif shape == "3":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            area = 0.5 * base * height
            print(f"\n✅ Triangle area: {area} square units")
            
        else:
            print("\n❌ Invalid shape choice!")
            
    except ValueError:
        print("\n❌ Error: Please enter valid numbers!")

def temperature_converter():
    """Convert between Celsius and Fahrenheit"""
    print("\n🌡️  TEMPERATURE CONVERTER")
    print("-" * 24)
    
    print("Choose conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Enter choice (1-2): ")
    
    try:
        if choice == "1":
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"\n✅ {celsius}°C = {fahrenheit}°F")
            
            # Add some context
            if fahrenheit < 32:
                print("🧊 That's freezing!")
            elif fahrenheit < 50:
                print("🥶 That's cold!")
            elif fahrenheit < 70:
                print("😊 That's cool!")
            elif fahrenheit < 80:
                print("🌤️  That's pleasant!")
            elif fahrenheit < 90:
                print("☀️  That's warm!")
            else:
                print("🔥 That's hot!")
                
        elif choice == "2":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"\n✅ {fahrenheit}°F = {celsius:.1f}°C")
            
        else:
            print("\n❌ Invalid choice!")
            
    except ValueError:
        print("\n❌ Error: Please enter a valid number!")

def tip_calculator():
    """Calculate tip and total bill"""
    print("\n💰 TIP CALCULATOR")
    print("-" * 16)
    
    try:
        bill_amount = float(input("Enter bill amount: $"))
        tip_percentage = float(input("Enter tip percentage (e.g., 15 for 15%): "))
        
        tip_amount = bill_amount * (tip_percentage / 100)
        total_amount = bill_amount + tip_amount
        
        print(f"\n💵 Bill breakdown:")
        print(f"   Original bill: ${bill_amount:.2f}")
        print(f"   Tip ({tip_percentage}%): ${tip_amount:.2f}")
        print(f"   Total amount: ${total_amount:.2f}")
        
        # Calculate per person if splitting
        people = input("\nSplitting the bill? Enter number of people (or press Enter to skip): ")
        if people:
            try:
                num_people = int(people)
                per_person = total_amount / num_people
                print(f"   Per person: ${per_person:.2f}")
            except ValueError:
                print("❌ Invalid number of people!")
                
    except ValueError:
        print("\n❌ Error: Please enter valid numbers!")

def age_calculator():
    """Calculate age and provide fun facts"""
    print("\n🎂 AGE CALCULATOR")
    print("-" * 16)
    
    try:
        birth_year = int(input("Enter your birth year: "))
        current_year = 2024  # You can update this or use datetime module
        
        age = current_year - birth_year
        
        if age < 0:
            print("\n❌ Invalid birth year!")
            return
        
        print(f"\n✅ You are {age} years old!")
        
        # Fun calculations
        days = age * 365
        hours = days * 24
        minutes = hours * 60
        
        print(f"\n🎉 Fun facts about your age:")
        print(f"   You've lived approximately {days:,} days")
        print(f"   That's about {hours:,} hours")
        print(f"   Or roughly {minutes:,} minutes!")
        
        # Age category
        if age < 13:
            category = "child"
            emoji = "👶"
        elif age < 20:
            category = "teenager"
            emoji = "🧒"
        elif age < 60:
            category = "adult"
            emoji = "👨"
        else:
            category = "senior"
            emoji = "👴"
            
        print(f"   You're in the {category} category! {emoji}")
        
    except ValueError:
        print("\n❌ Error: Please enter a valid year!")

# Run the calculator
if __name__ == "__main__":
    main()

"""
🎯 LEARNING OBJECTIVES ACHIEVED:

✅ Variables and Data Types: Used strings, integers, floats, booleans
✅ User Input/Output: input() and print() with formatting
✅ Arithmetic Operations: All basic math operations
✅ Control Structures: if/elif/else statements and while loops
✅ String Formatting: F-strings for user-friendly output
✅ Error Handling: Basic try/except for invalid input
✅ Functions: Organized code into reusable functions

🚀 NEXT STEPS:
- Run this program and try all the features
- Modify it to add new calculators (e.g., loan calculator)
- Add more error checking and validation
- Experiment with the code to understand how it works

Great job completing your first Python project! 🎉
"""