
while True:
    first_number = int(input("Enter the first number: "))
    operator = input("Choose the operator (+, -, /, *, %): ")
    second_number = int(input("Enter the second number: "))

    if operator == '+':
        print("Result:", first_number + second_number)
    elif operator == '-':
        print("Result:", first_number - second_number)
    elif operator == '/':
        if second_number == 0:
            print("Error: Cannot divide by zero.")
        else:
            print("Result:", first_number / second_number)
    elif operator == '*':
        print("Result:", first_number * second_number)
    elif operator == '%':
        if second_number == 0:
            print("Error: Cannot modulo by zero.")
        else:
            print("Result:", first_number % second_number)
    else:
        print("Invalid operator entered.")

    choice = input("Do you want to calculate again? (yes/No): ").strip().lower()
    if choice != 'han':
        print("Calculator exited.")
        break
