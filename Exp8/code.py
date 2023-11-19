def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

while True:
    print("\nOptions:")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        result = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {result}°F")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        result = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {result}°C")
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


