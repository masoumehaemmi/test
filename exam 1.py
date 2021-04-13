import math

print("Menu: ")

menu = {"Action: +", "Action: -", "Action: *", "Action: /", "Action: **", "Action: log", "Action: sqrt", "Action: sin",
        "Action: cos", "Action: factorial", "Action: tan"}

for men in menu:
   
    print(men)

operator = input("Enter Operator: ")if operator == "sin" or operator == "sqrt" or operator == "cos" or operator == "factorial" or operator == "tan":
    a = float(input("Enter First Number: "))
else:
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
if operator == "+":
    print(f"sum: {a + b}")
elif operator == "-":
    print(f"Subtraction: {a - b}")
elif operator == "*":
    print(f"Multiplication: {a * b}")
elif operator == "/":
    if b == 0:
        print(("Cannot Divide By Zero", )
    else:
        print(f"Division: {a / b}")
elif operator == "**":
    print(f"Power {a ** b}")
elif operator == "log":
    print(f"Logarithm: {math.log(a, b)}")
elif operator == "sqrt":
    print(f"Sqrt: {math.sqrt(a)}")
elif operator == "sin":
    print(f"Sinus: {math.sin(a * math.pi / 180)}")
elif operator == "cos":
    print(f"{math.cos(a * math.pi / 180)}")
elif operator == "factorial":
    print(f"Factorial: {math.factorial(a)}")
elif operator == "tan":
    print(f"Tangent: {math.tan(a * math.pi / 180)}")
else:
    print("Error!! TryAgain")
 print("Error!! TryAgain")
