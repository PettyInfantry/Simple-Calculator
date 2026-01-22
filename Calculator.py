def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return num1 / num2


def main():
    print("Simple Calculator")
    print("-----------------")
    print("Operations: +  -  *  /")
    print("Type 'q' as operation to quit\n")

    while True:
        try:
            # Get first number
            num1_input = input("Enter first number: ").strip()
            if num1_input.lower() == 'q':
                print("Goodbye!")
                break
            num1 = float(num1_input)

            # Get second number
            num2_input = input("Enter second number: ").strip()
            if num2_input.lower() == 'q':
                print("Goodbye!")
                break
            num2 = float(num2_input)

            # Get operation
            operation = input("Enter operation (+, -, *, /) or q to quit: ").strip()

            if operation.lower() == 'q':
                print("Goodbye!")
                break

            # Perform calculation
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operation! Please use +, -, *, or /")
                print("-" * 40)
                continue

            # Show result (with nice formatting)
            print(f"\n{num1} {operation} {num2} = {result}")
            print("-" * 40)

            # Ask if user wants to continue
            again = input("Another calculation? (y/n): ").strip().lower()
            if again != 'y':
                print("Thank you for using the calculator!")
                break

            print()  # empty line for readability

        except ValueError:
            print("Error: Please enter valid numbers!\n")
        except ZeroDivisionError as e:
            print(f"Error: {e}\n")
        except Exception as e:
            print(f"Unexpected error: {e}\n")


if __name__ == "__main__":
    main()