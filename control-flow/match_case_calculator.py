num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Choose the operation (+, -, *, /): ")

def calculate(num1, num2, operation):
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 == 0:
                return "Error: Division by zero"
            return num1 / num2

print('Results: ', calculate(num1, num2, operation))