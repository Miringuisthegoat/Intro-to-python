#Write a simple calculator program
#when the program runs,it prompts the user to enter first number,operator( +, -, * , /) and second number.Based on the operator entered,it should provide the correct output


# Simple Calculator Program

# Prompt user for inputs
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Perform calculation based on operator
if operator == "+":
    print("Result:", num1 + num2)

elif operator == "-":
    print("Result:", num1 - num2)

elif operator == "*":
    print("Result:", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Math Error!!")

