#ex1-ex6 are all in Lab0.py
#Author: He Shijia
#Student ID: 202483890013
#Lab ID: Lab0
#Date: 17/3/25
#URL of your remote GitHub repository:https://github.com/dididudu-123/NUIST_ProjectSem2.git


num = float(input("Please enter a number: "))
num1 = num*2
print(f"The double of the input number is {num1}")

name = input("Please enter your name: ")
name1 = name.upper()
print(name1)

import random
correct_num = random.randint(10,20)
if enter_num:=int(input("Guess a number between 10 and 20")) == correct_num:
    print("You are correct")
else:
    print("It is wrong.Please try again")

age = int(input("Please enter your age: "))
if age <= 19:
    print("You qualify for student discounts")
elif 20<= age <=54:
    print("You qualify for no age discounts")
elif age>=55:
    print("You can receive senior discounts.")

num3 = 1
num2 = int(input("Please enter a positive integer: "))
while num2 > 0:
    num3 *= num2
    num2 -=1
print (num3)

num5 = 1
num4 = int(input("Please enter a positive integer: "))
for i in range(1,num4+1):
    num5 *=i
print (num5)

