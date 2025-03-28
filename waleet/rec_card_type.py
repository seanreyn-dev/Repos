## Recommending card type
## global credit card data

credit_cards = [
    {
        "name": "Amex Gold",
        "type": "Travel",
        "rewards": {"dining": .04, "grocery": .04, "Travel": .03, "Other": .01},
        "annual fee": 325
    },
    {
        "name": "Discover It",
        "type": "Cashback",
        "rewards": {
            "rotating": {
                "Q1": ["restaurants", "home improvement stores", "select streaming services"],
                "Q2": ["grocery stores", "wholesale clubs"],
                "Q3": ["coming soon"],
                "Q4": ["coming soon"]
            },
            "base": .01,
            "bonus_rate": .05
        },
        "annual_fee": 0
    }
]

def recommend_card(user_data, credit_cards):



def main():
    while True:    # empty user data dict
        user_data = {}
        # user inputs name
        user_name = input("Please enter your name: ")

        # get input from user    
        print(f"\nHi {user_name}, please input your monthly spending habits")
            
        grocery_spend = int(input("\nInput your grocery spend: "))
        dining_spend = int(input("\nInput your dining spend: "))
        gas_spend = int(input("\nInput your gas spend: "))
        travel_spend = int(input("\nInput your travel spend: "))

        # save user name in dict
        user_data["name"] = user_name

        # assigns user data to dict
        user_data["spending"] = {
            "groceries": grocery_spend, 
            "dining": dining_spend,
            "gas": gas_spend,
            "travel": travel_spend
            }
        print("\nYour saved spending data:")
        print(user_data)
        
        # Ask if they want to run it again
        run_again = input("Would you like to re-enter your details? (Y/N): ")
        if run_again.lower() != "Y":
            print("Thanks for using the tool! Goodbye.")
            break

    
main()