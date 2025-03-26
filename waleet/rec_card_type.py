## Recommending card type

def main():
    # ask a question
    user_name = input("Please enter your name: ")
    
    print(f"\nHi {user_name}, please input your monthly spending habits")
    
    grocery_spend = int(input("\nInput your grocery spend: "))
    dining_spend = int(input("\nInput your dining spend: "))
    gas_spend = int(input("\nInput your gas spend: "))
    travel_spend = int(input("\nInput travel  spend: "))


main()