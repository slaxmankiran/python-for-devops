
def addtn(num1, num2):
    add = num1 + num2
    return add  #instead of printing the value, we are just returning it to below print block on line #9

print("Addition result: ", addtn(125, 25)) # one way of defining variables

def subtn(num1, num2):
    sub = num1 - num2
    return sub 

x = subtn(125, 25) # another way of defining the variables

print("Substraction result: ", x)


def divtn(num1, num2):
    div = num1 / num2
    return div
    
print("Division result: ", divtn(125,25))  


def multn(num1, num2):
    mul = num1 * num2
    return mul

print("Multiplication result: ", multn(125,25))




