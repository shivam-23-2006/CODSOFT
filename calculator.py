def calculator():
    print("\nWelcome to the Friendly Calculator! 😊")
    print("I can help you with basic operations like addition, subtraction, multiplication, and division.")
    
    while True:
        print("\nWhat would you like to do today?")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")

        # Get the user's choice
        choice = input("\nPlease enter your choice (1/2/3/4/5): ").strip()
        
        if choice == "5":
            print("\nThanks for using the calculator. Have a great day! 🌟")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("\nOops! That doesn't look like a valid choice. Please try again.")
            continue

        # Get numbers from the user
        try:
            num1 = float(input("\nEnter the first number: ").strip())
            num2 = float(input("Enter the second number: ").strip())
        except ValueError:
            print("\nThat doesn't seem to be a number. Let's try again!")
            continue

        # Perform the selected operation
        if choice == "1":
            print(f"\nThe sum of {num1} and {num2} is: {num1 + num2}")
        elif choice == "2":
            print(f"\nThe difference between {num1} and {num2} is: {num1 - num2}")
        elif choice == "3":
            print(f"\nThe product of {num1} and {num2} is: {num1 * num2}")
        elif choice == "4":
            if num2 == 0:
                print("\nOops! Division by zero is not allowed. Please try again with a different number.")
            else:
                print(f"\nThe result of dividing {num1} by {num2} is: {num1 / num2:.2f}")
        else:
            print("\nSomething went wrong. Let's start over!")

calculator()
