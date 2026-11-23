num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

addition = num1 + num2
subtraction = num1 - num2 
multiplication = num1 * num2 
division = num1/num2
floorDivision = num1 // num2 
modulus = num1 % num2
exponentiation = num1 ** num2 

print("Addition : ", addition)
print("Subtraction : ", subtraction)
print("Multiplication : ", multiplication)
print("Division : ", division)
print("floorDivision : ", floorDivision)
print("Modulus : ", modulus)
print("Exponentiation", exponentiation)

age = int(input("Enter your age : "))
haveId = input("Do you have id : ")

if str(haveId).lower() == "no":
    Id = False
else :
    Id = True 

if age >= 18 and Id :
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

marks = int(input("Enter your marks : "))

if marks < 60 :
    print("Grade D")
elif marks >= 60 and marks <= 74:
    print("Grade C")
elif marks >= 75 and marks <= 89:
    print("Grade B")
else:
    print("Grade A")

number = int(input("Give a number : "))

i = 1 
total = 0

while i <= number:
    print(i)
    total += i
    i += 1 

print("Sum of number till n : ", total)

i = 1

print("Even number from 1 to 50 : ")

while i <= 50:
    if i % 2 == 0:
        print(i)
    i += 1