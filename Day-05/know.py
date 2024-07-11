salary = 8000 # global variable

def printSalary():
  salary = 12000 #local variable
  print("Salary1:", salary)
  
printSalary()
print("Salary2:", salary)