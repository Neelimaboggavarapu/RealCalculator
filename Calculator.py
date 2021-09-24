num1,operator,num2 = map(str, input("Enter Equation: ").split())
int(num1)
int(num2)
if operator == "+":
    sum = num1 + num2
    print("Sum Of {num1} and {num2} is {sum}")
elif operator == "-":
    sub = num1 - num2
    print("Subtraction of {num2} from {num1} is {sub}")
elif operator == "*":
    mul = num1 * num2
    print("Multipication of {num1} and {num2} is {mul}")
elif operator == "/":
    div = num1 / num2
    print("Division of {num1} and {num2} is {div}")
elif operator == "%":
    mod = num1 % num2
    print("Modulus of {num1} and {num2} is {mod}")
else:
    print("Invalid input!!! Enter your input as EX: 8 + 2 ")
