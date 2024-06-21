arn = "arn:aws:service:region:account-id:resource-type/resource-id"
str1 = "Laxman Kiran"
str2 = "Seedabathula"
text = "I am learning Python and it's Awesome"
substring = "and"
length = len(text)
num1 = 20.445
num2 = 5.32
result = num1 + num2
result2 = round(3.14186456578453, 2)
result3 = num1 // num2
r_id = arn.split("/")
r_id2 = str1+ " " +str2
r_id3 = r_id2. replace("Laxman Kiran" , "Viyan")

print("Indexed Result: ", r_id[0])
print("Split Result: ", arn.split("/")[1])
print("Concat'n Result: ", r_id2)
print("Length of the String: ", len(r_id2))
print("Length of String #2: ", len(text))
print("In Lower case: ",r_id2.lower())
print("In Upper case: ",r_id2.upper())
print("Replaced name: ", r_id3)
print("Stripped Text: ", r_id2.strip())

# substring in action
if substring in text:
    print(substring, "found in the text")

# Float
print("Addition: ",result)

#Rounding
print("Rounded: ", result2)

#Integer division
print("Integer Division: ", result3)

# Modulus (Remainder)
result4 = num1 % num2
print("Modulus (Remainder):", result4)