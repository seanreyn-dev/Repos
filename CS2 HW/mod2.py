## Exercise Module 2

def first_question():
    user_age = int(input("Enter your age: "))

    if user_age < 7:
        print("Can watch G rated movies")
    elif 7 <= user_age < 13:
        print("Can watch G and PG rated movies")
    elif 13 <= user_age < 17:
        print("Can watch G, PG, and PG-13 rated movies")
    elif user_age >= 17:
        print("Can watch G, PG, PG-13, and R rated movies")



def second_question():
    total = 0
    count = 0
    
    while True:
        user_input = int(input("Enter a positive number or enter -1 to quit): "))
        if user_input == -1:
            break
        elif user_input >= 0:
            total += user_input
            count += 1
        else:
            print("Only enter posiive numbers or -1 to quit")
    
    if count > 0:
        average = total / count
        print(f"The average is: {average}")
    else:
        print("No numbers were entered.")

def third_question():
    phone = input("Enter your phone number in format nnn-nnn-nnnn: ")
    if len(phone) == 12 and phone[3] == "-" and phone[7] == "-" and phone.replace("-","").isdigit():
        print("valid num")
    else:
        print("invalid num")

#third_question()

def triangle():
    base = int(input("base: "))
    height = int(input("height: "))
    area = (base * height) / 2
    return area

##print(f"area = {triangle()}")

def fourth_question():
    name1 = input("Enter name 1: ")
    name2 = input("Enter name 2: ")
    price1 = input("Enter price 1: ")
    price2 = input("Enter price 2: ")
    print(f"Food1: {name1}\nPrice1: {price1}")
    print(f"Food2: {name2}\nPrice2: {price2}")


#fourth_question()

def summation(n):
    if n < 1:
        return "input must be at least 1"
    if n == 1:
        return 1
    else:
        return n + summation(n - 1)

















def third_question():
    phone = input("Enter a phone number (format: nnn-nnn-nnnn): ")
    if len(phone) == 12 and phone[3] == '-' and phone[7] == '-' and phone.replace('-', '').isdigit():
        print("Valid phone number format.")
    else:
        print("Invalid phone number format.")

def triangle_area(base, height):
    area = 0.5 * base * height
    return area

def fifth_question():
    food1 = input("Enter the first food: ")
    price1 = float(input(f"Enter the price of {food1}: "))
    food2 = input("Enter the second food: ")
    price2 = float(input(f"Enter the price of {food2}: "))
    
    print(f"{food1}: ${price1}")
    print(f"{food2}: ${price2}")

def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n - 1)