# Initialize an empty list to store records
database = []

# Function to add a new record to the database
def add_record(name, age, city):
    record = (name, age, city)  # Create a tuple for the record
    database.append(record)  # Add the tuple to the database list

# Function to display all records in the database
def display_records():
    print("Records in the database:")
    for record in database:
        print(f"Name: {record[0]}, Age: {record[1]}, City: {record[2]}")

# Main function to demonstrate the database operations
def main():
    # Add records to the database
    add_record("Alice", 30, "New York")
    add_record("Bob", 25, "Los Angeles")
    add_record("Charlie", 35, "Chicago")
    
    # Display all records in the database
    display_records()

if __name__ == "__main__":
    main()

