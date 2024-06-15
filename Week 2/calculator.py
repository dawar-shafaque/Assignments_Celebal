def add(num1,num2):
    return num1 + num2 

def sub(num1,num2):
    return num1 - num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2 

print("Please select operation -\n" "1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n")

inp = int(input("Please enter your choice\n"))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if inp == 1:
    print('{} + {} = {}'.format(num1,num2,add(num1,num2)))

elif inp == 2:
    print('{} - {} = {}'.format(num1,num2,sub(num1,num2))) 

elif inp == 3:
    print('{} * {} = {}'.format(num1,num2,mul(num1,num2))) 

elif inp == 4:
    print('{} / {} = {}'.format(num1,num2,div(num1,num2)))

else:
    print("Invalid input!!")
