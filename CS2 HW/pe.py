def main():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    print(len(first_name))
    capfirstname = first_name.upper()
    lowerlastname = last_name.lower()
    print(f"{capfirstname} {lowerlastname}")
    print(f"{capfirstname} {capfirstname} {capfirstname}")

main()