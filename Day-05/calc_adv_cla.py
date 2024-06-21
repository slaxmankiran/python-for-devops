# import sys module for the calc to pass CLA (Command Line Arguments)
import sys 

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])


def addtn(num1, num2):
    add = num1 + num2
    return add

# If user is passing "add" operation in CLA; perform below
if operation == "add":
    output = addtn(num1, num2)
    print("Addition result: ", output)


def subtn(num1, num2):
    sub = num1 - num2
    return sub 

# If user is passing "sub" operation in CLA; perform below
if operation == "sub":
    output = subtn(num1, num2)
    print("Substraction result: ", output)


def divtn(num1, num2):
    div = num1 / num2
    return div

# If user is passing "div" operation in CLA; perform below ; output is rounded to 3 decimals
if operation == "div":
    output = divtn(num1, num2)
    print("Division result: ", round(output, 3))  


def multn(num1, num2):
    mul = num1 * num2
    return mul

# If user is passing "mul" operation in CLA; perform below
if operation == "mul":
    output = multn(num1, num2)
    print("Multiplication result: ", output)

