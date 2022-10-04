# Intermedite improved calculator
#Code 1

# we need to get 3 variables from the user. 2 numbers and 1 operator.

num1 = float(input("Enter first number: "))
op = input("Enter your operator: ")
num2 = float(input("Enter second number: "))

# we need to check what operator the user is inputting.

if op == "+":
    print(num1 + num2)

elif op == "-":
    print(num1 - num2)

elif op == "/":
    print(num1 / num2)

elif op == "*":
    print(num1 * num2)

else:
    print("Invalid operator")




