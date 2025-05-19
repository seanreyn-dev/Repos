import csv

try:
    with open("population_by_country_2020.csv", "r", encoding="utf-8-sig") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=",")
        country_dict = {}
        for line in csv_reader:
            name = line["Country (or dependency)"]
            pop = int(line["Population (2020)"].replace(",", ""))
            land = int(line["Land Area (Km²)"].replace(",", ""))
            country_dict[name] = (pop, land)
except IOError:
    print("Error")

prompt = input("Choose 'country' or 'ranking': ").lower()
while prompt != "country" and prompt != "ranking":
    prompt = input("Invalid. Choose 'country' or 'ranking': ").lower()
else:
    if prompt == "country":
        country = input("What country? ")
        if country in country_dict:
            data = country_dict[country]
            print(f"{country}: Population = {data[0]}, Land Area = {data[1]} sq km")
        else:
            print("Country not found.")
    elif prompt == "ranking":
        choice = input("Do you want to see the associated country based on population or land area rank? ")
        if choice == "population":
            country_rank = int(input("What ranking country do you want to see based on population? "))
            sorted_by_pop = sorted(country_dict.items(), key=lambda item: item[1][0], reverse=True)
            if 1 <= country_rank <= len(sorted_by_pop):
                country, data = sorted_by_pop[country_rank - 1]
                print(f"Rank {country_rank} by population: {country} with Population = {data[0]} and Land Area = {data[1]} sq km")
            else:
                print("Invalid rank number.")
        elif choice == "land area":
            land_area_rank = int(input("What ranking country do you want to see based on land area? "))
            sorted_by_land = sorted(country_dict.items(), key=lambda item: item[1][1], reverse=True)
            if 1 <= land_area_rank <= len(sorted_by_land):
                country, data = sorted_by_land[land_area_rank - 1]
                print(f"Rank {land_area_rank} by land area: {country} with Population = {data[0]} and Land Area = {data[1]} sq km")
            else:
                print("Invalid rank number.")


