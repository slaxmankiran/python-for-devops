#for loop example

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("for loop result: ", fruit)

#while loop example
count = 0
while count < 5:
    print("while loop result: ", count)
    count += 1

#loop controls - break & continue exmaple

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        break
    print("Break loop result: ", number)

numbers2 = [1, 2, 3, 4, 5]
for number in numbers2:
    if number == 3:
        continue
    print("Continue loop result: ", number)
