# Prompt the user to enter a valid operator
while True:
    operator = input('Enter any operator (+, -, *, /): ')
    if operator in ['+', '-', '*', '/']:
        break  # Exit the loop when a valid operator is entered
    else:
        print("Invalid operator. Please try again.")

# Input numbers

while True:
    try:
        # Attempt to convert input to a float
        num1 = float(input("Enter number 1: "))
        break  # Exit the loop if successful
    except ValueError:
        # If conversion fails, prompt again
        print("Invalid input. Please enter a valid number.")


while True:
    try:
        # Attempt to convert input to a float
        num2 = float(input("Enter number 2: "))
        break  # Exit the loop if successful
    except ValueError:
        # If conversion fails, prompt again
        print("Invalid input. Please enter a valid number.")



# Perform the operation
if operator == '+':
    print(f'Result is: {round(num1 + num2, 2)}')
elif operator == '-':
    print(f'Result is: {num1 - num2}')
elif operator == '*':
    print(f'Result is: {num1 * num2}')
elif operator == '/':
    if num2 != 0:  # Check for division by zero
        print(f'Result is: {num1 / num2}')
    else:
        print("Error: Division by zero is not allowed.")
        while True:
         if num2 != 0:
             break
         else:  
          print(float(input("enter num2 ")))




  