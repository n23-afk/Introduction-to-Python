a = int(input("First number: "))
op = input("Operator (+ - * /): ")
b = int(input("Second number: "))

if op == "+":
    print(int(a + b))
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b == 0:
        print("Error: division by zero")
    else:
        print(a / b)
else:
    print("Unknown operator:", op)