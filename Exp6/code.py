# Create a list to store student records
student_records = []

# Function to add a student record to the list
def add_student_record():
    name = input("Enter student's name: ")
    roll_number = input("Enter roll number: ")
    marks = input("Enter marks: ")
    student_record = {'Name': name, 'Roll Number': roll_number, 'Marks': marks}
    student_records.append(student_record)
    print(f"Student record for {name} has been added.")

# Function to search for a student record by name
def search_student_record():
    search_name = input("Enter the name of the student you want to search for: ")
    found = False
    for record in student_records:
        if record['Name'] == search_name:
            print("Student Record Found:")
            print("Name:", record['Name'])
            print("Roll Number:", record['Roll Number'])
            print("Marks:", record['Marks'])
            found = True
            break
    if not found:
        print(f"No record found for {search_name}.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add Student Record")
    print("2. Search Student Record")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_student_record()
    elif choice == '2':
        search_student_record()
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
