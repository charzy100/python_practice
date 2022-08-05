#!/usr/bin/python3
# This program accepts 2 integers from users and perform basic maths operations on them...
# Accepts the 2 integers from users and store them in variables called num1 & num2 and them split them with the split() function into various strings as entered by user...
num1, num2 = input("Enter the 2 numbers: ").split()

#cnvert the splitted inputs into integers to perform maths operations on them...
num1 = int(num1)
num2 = int(num2)

#MATHS OPERATIONS...
sum = num1 + num2
difference = num1 -  num2
product = num1 *  num2
quotient = num1 / num2
remainder = num1 % num2

print(f"You entered {num1} and {num2} as input and the maths operarions are as follows:")
print(f"{num1} + {num2} = {sum}")
print(f"{num1} - {num2} = {difference}")
print(f"{num1} x {num2} = {product}")
print(f"{num1} / {num2} = {quotient}")
print(f"The remainder when {num1} is divided by {num2} = {remainder}")
