## Task 1: Arithmetic Operators

a = 15
b = 7
c = 7

sum = a + b

diff = a - b

product = a * b

quotient = a / b


print("Sum is:", (sum))
print("Difference is:" , (diff))
print("Product is:", (product))
print("Quotient is: ", (quotient))


## Task 2: Comparison Operators

comp1 = a < b
comp2 = a > b
comp3 = a <= b
comp4 = a >= b
comp5 = c == b
comp6 = c != b


print("Comparison1 a < b is: ", (comp1))
print("Comparison2 a > b is: ", (comp2))
print("Comparison3 a<=b is: ", (comp3))
print("Comparison4 a>=b is: ", (comp4))
print("Comparison5 c==b is: ", (comp5))
print("Comparison6 c!=b is: ", (comp6))


## Task 3: Logical Operators

x = comp1  #comp1 is False
y = comp2  # comp2 is True

result_and = x and y
result_or = x or y
result_not_x = not x 
result_not_y = not y



print("Result_and is: ", (result_and))
print("Result_or is: ", (result_or))
print("Result_not_x is: ", (result_not_x))
print("Result_not_y is: ", (result_not_y))


## Task 4: Assignment Operators

total = 10
total += 5
total -= 3
total *= 2
total /= 4


print("Final total is: ", (total))


## Task 5: Bitwise Operators (Optional)


## Task 6: Identity and Membership Operators
my_list = ["apple", "ball", "cat", "dog"]
a = my_list
b = ["apple", "ball", "cat", "dog"]

idenity_is = a is b
idenity_is_not = a is not b


print("Identity a is b: ", (idenity_is))
print("Identity a is not b: ", (idenity_is_not))


membership_in = "ball" in my_list
membership_not_in = "elephant" not in my_list


print("Ball in my_list: ", (membership_in))
print("Elephant is not in my_list: ", (membership_not_in))

