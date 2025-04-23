import random
import math
"""
ask user to enter a number 
store the number
if number = -1 break
otherwise store until -1 is entered
print largest and smallest numbers
"""

def main():
    numbers = []
    while True:
        num = int(input("Enter positive numbers (-1 to stop): "))
        if num == -1:
            break
        else:
            numbers.append(num)
    numbers.sort()
    print(f"Smallest number: {numbers[0]}, Largest number: {numbers[-1]}")


"""
prompt user age and user accident history
print appropriate response with insurance amount
add conditions and accident fee
"""

def main2():
    user_age = int(input("Enter your age: "))
    acc_his = input("Have you been in an accident? (y/n): ").lower()
    if 16 <= user_age <= 35:
        if acc_his != "n":
            print("Insurance costs $5300")
        else:
            print("Insurance costs $5000")
    elif 36 <= user_age <= 49:
        if acc_his != "n":
            print("Insurance costs $3300")
        else:
            print("Insurance costs $3000")
    elif user_age >= 50:
        if acc_his != "n":
            print("Insurance costs $2300")
        else:
            print("Insurance costs $2000")


"""

"""
def main3():
    number = int(input("Provide a phone number in the format (nnnnnnnnnn): "))
    first_three = number // 10000000
    middle_three = number // 10000 % 1000
    last_four = number % 10000
    print("Phone number is", "(" + str(first_three) + ")" + str(middle_three) + "-" + str(last_four))

main3()