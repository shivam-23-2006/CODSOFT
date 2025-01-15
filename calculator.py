def calculator():
    print("Simple Calculator")
    
    while True:
        print("\n1. Add (+)  2. Subtract (-)  3. Multiply (*)  4. Divide (/)  5. Exit")
        choice = input("Choose an operation (1/2/3/4/5): ").strip()
        
        if choice == "5":
            print("Goodbye!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if choice == "1":
            print(f"Result: {num1 + num2}")
        elif choice == "2":
            print(f"Result: {num1 - num2}")
        elif choice == "3":
            print(f"Result: {num1 * num2}")
        elif choice == "4":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {num1 / num2:.2f}")

calculator()
