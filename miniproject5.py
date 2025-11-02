num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

while True:
        # Prompt the user for input and display the menu
        print("\nChoose an operation:")
        print("'+' for Addition")
        print("'-' for Subtraction")
        print("'*' for Multiplication")
        print("'/' for Division")
        print("Type 'exit' to quit the program")

        operation = input("Enter your choice: ")

        # Check if the user wants to exit
        if operation == 'exit':
            print("Exiting calculator. Goodbye!")
            break
          
        
        # Use if/elif/else to perform the calculation
        if operation == '+':
            result = num1 + num2
            print(f"The result is: {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"The result is: {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"The result is: {result}")
        elif operation == '/':
            # Add error handling for division by zero
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The result is: {result}")
