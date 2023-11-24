country_data = {
    'IN': {'Name': 'India', 'Capital': 'Delhi', 'Population': 1320000000},
    'US': {'Name': 'America', 'Capital': 'Washington', 'Population': 320000000},
    'AU': {'Name': 'Australia', 'Capital': 'Canberra', 'Population': 24000000},
    'CA': {'Name': 'Canada', 'Capital': 'Ottawa', 'Population': 940000}
}

def view_countries():
    print("Country Codes:", ' '.join(country_data.keys()))

def view_country(country_code):
    if country_code in country_data:
        country_info = country_data[country_code]
        print(f"Country name is: {country_info['Name']}")
        print(f"Country capital is: {country_info['Capital']}")
        print(f"Country population is: {country_info['Population']}")
    else:
        print(f"There is no country for country code {country_code}")

def add_country(country_code, country_name, capital, population):
    if country_code not in country_data:
        country_data[country_code] = {
            'Name': country_name,
            'Capital': capital,
            'Population': population
        }
        print(f"Country '{country_name}' with code '{country_code}' added successfully.")
    else:
        print(f"Country with code '{country_code}' already exists.")

def delete_country(country_code):
    if country_code in country_data:
        deleted_country = country_data.pop(country_code)
        print(f"Country '{deleted_country['Name']}' with code '{country_code}' deleted.")
    else:
        print(f"Country with code '{country_code}' not found.")

while True:
    print("\nSELECT AN OPTION:")
    print("view: View country names")
    print("add: Add a country")
    print("del: Delete a country")
    print("exit: Exit the program")

    choice = input("Your choice: ").lower()

    if choice == 'view':
        view_countries()
        country_code = input("Enter country code: ")
        view_country(country_code)
    elif choice == 'add':
        country_code = input("Enter the country code: ")
        country_name = input("Enter the country name: ")
        capital = input("Enter the capital city: ")
        population = int(input("Enter the population: "))
        add_country(country_code, country_name, capital, population)
    elif choice == 'del':
        country_code = input("Enter the country code to delete: ")
        delete_country(country_code)
    elif choice == 'exit':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option (view/add/del/exit).")


