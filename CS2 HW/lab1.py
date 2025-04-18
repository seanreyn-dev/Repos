## Sean Reynolds Lab 1

MAX = 40
def main():
    name = input("Enter your name: ").lower().title()
    prev_class = input("How many previous programming classes have you taken?: ")
    class_goal = input("What is your goal for taking CIS 41A?: ").upper()
    print()
    print("*" * MAX)
    print("*" + " " * (MAX - 2 ) + "*")

    name_centered = name.center(MAX - 2)
    print("*" + name_centered + "*") 
   
    
    print("*" + " " * (MAX - 2 ) + "*")
    print("*" * MAX)



    print(f"You've taken {prev_class} programming classes")
    print(f"Your goal for this class is:\n{class_goal}")

main()
"""
Enter your name: Sean Reynolds
How many previous programming classes have you taken?: 1
What is your goal for taking CIS 41A?: I'M INTERESTED IN HIGH LEVEL PROGRAMMING AND DEVELOPING MY SKILLS. I HOPE THAT ONE DAY I WILL BE ABLE TO CODE FOR A LIVING AS A SOFTWARE ENGINEER. I HAVE RECENTLY TRANSFERRED INTO I.T. FULL TIME AND HAVE BEEN ENJOYING IT. HAVE A GOOD WEEK!

****************************************
*                                      *
*            Sean Reynolds             *
*                                      *
****************************************
You've taken 1 programming classes
Your goal for this class is:
I'M INTERESTED IN HIGH LEVEL PROGRAMMING AND DEVELOPING MY SKILLS. I HOPE THAT ONE DAY I WILL BE ABLE TO CODE FOR A LIVING AS A SOFTWARE ENGINEER. I HAVE RECENTLY TRANSFERRED INTO I.T. FULL TIME AND HAVE BEEN ENJOYING IT. HAVE A GOOD WEEK!
"""

"""
Enter your name: sEaN  rEynOlds
How many previous programming classes have you taken?: 1
What is your goal for taking CIS 41A?: blank 

****************************************
*                                      *
*            Sean  Reynolds            *
*                                      *
****************************************
You've taken 1 programming classes
Your goal for this class is:
BLANK
"""