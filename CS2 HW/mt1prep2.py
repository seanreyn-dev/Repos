#mt2prep 2
import random
import math

def main():
    rand = random.randint(1,10)
    tries = 0
    while True:
        guess = int(input("Guess a number between 1 and 10: "))
        tries += 1
        if guess != rand:
            print("Incorrect guess, try again")
        else:
            print("You took", tries, "tries")





def hypotenuse(a,b):
    return math.sqrt(a**2 + b**2)

print(hypotenuse(2,4))


def q3():
    numb = []
    user_num = int(input("Enter positive numbers (-1) to stop: "))


def main():
    num = int(input("Enter positive numbers (-1 to stop): "))
    numbers = [num, num]
    while True:
        num = int(input("Enter positive numbers (-1 to stop): "))
        if num == -1:
            break
        else:
            if num < numbers[0]:
                numbers[0] = num
            elif num > numbers[1]:
                numbers[1] = num
    print(f"Smallest number: {numbers[0]}, Largest number: {numbers[1]}")





def main2():
    user_age = int(input("Enter your age: "))
    acc_his = input("Have you been in an accident? (y/n): ").lower()
    amount = 0
    if 16 <= user_age <= 35:
        amount = 5000  
    elif 36 <= user_age <= 49:
        amount = 3000
    elif user_age >= 50:
        amount = 2000
    if acc_his == "y":
        amount += 300
    print("your insurance is", amount)



def surface_area(a):
    return (a * 6)**2

def volume(a):
    return (a**3)

def bleh():
    user_ans =  float(input("Enter floating point numbers (0 to quit): "))
    numbers = [user_ans, user_ans]
    while True:
        user_ans =  float(input("Enter floating point numbers (0 to quit): "))
        if user_ans == 0:
            break
        else:
            if user_ans > numbers[1]:
                numbers[1] = user_ans
            elif user_ans < numbers[0]:
                numbers[0] = user_ans
    #print("The difference is", numbers[1] - numbers[0])


def pope_francis():
    num_years = int(input("Enter how many years the monarch has reigned: "))
    jubilee = ""
    difference = 0
    if num_years == 25:
        jubilee = "silver"
    elif num_years == 50:
        jubilee = "golden"
    elif num_years == 60:
        jubilee = "diamond"
    if jubilee == "":
        if 0 < num_years < 25:
            difference = 25 - num_years
            jubilee = "The next jubilee is silver"
        elif 25 < num_years < 50:
            difference = 50 - num_years
            jubilee = "The next jubilee is golden"
        elif 50 < num_years < 60:
            difference = 60 - num_years
            jubilee = "The next jubilee is diamond"
        elif num_years > 60:
            jubilee = "Diamond jubilee has already passed"
        if num_years > 60:
            print("The diamond jubilee has passed")
        else:
            print(jubilee, "in", difference, "years")
    else:
        print(num_years, "years is the", jubilee, "jubilee")



def ques4():
    phone_number = int(input("Enter a 7 digit phone number (nnn-nnnn): ").replace("-", ""))
    first_three = phone_number // 10000
    last_four = phone_number % 10000
    difference = last_four - first_three
    print("The difference between the last 4 digits and the first 3 digits is", difference)
    quotient = float(last_four / first_three)
    print("The quotient of the last 4 digits divided by the first 3 digits is", quotient)

    

                         




def ques5():
    mys_word = "poo"
    guess_a_word = input("Guess the word: ").lower()
    while guess_a_word != mys_word:
        print("Wrong guess, try again. The word has 3 letters")
        correct_letters = 0
        for i in range(6):
            try:
                if(guess_a_word[i] == mys_word[i]):
                    correct_letters += 1
            except IndexError:
                break
        print("You have", correct_letters, "letters correct.")
        guess_a_word = input("Guess the word: ")
    print("Congrats you guessed the word.")





