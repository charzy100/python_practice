num1, operator, num2 = input("Enter the 2 numbers separated by an operator:").split()
num1 = int(num1)
num2 = int(num2)
#MATHS OPERATORS
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotent = num1 / num2
remainder = num1 % num2
if operator == '+':
    print(f"{num1} {operator} {num2} = {sum}")
elif operator == '-':
    print(f"{num1} {operator} {num2} = {difference}")
elif operator == '*':
    print(f"{num1} {operator} {num2} = {product}")
elif operator == '/':
    print(f"{num1} {operator} {num2} = {quotent}")
elif operator == '%':
    print(f"{num1} {operator} {num2} = {remainder}")
else:
    print("Your entry is incorrect. Please try again later")

