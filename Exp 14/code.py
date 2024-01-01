
with open("MyFile.txt", "w") as file:
    # Ask the user to input three lines
    for i in range(3):
        line = input(f"Enter line {i + 1}: ")
        file.write(line + "\n")

print("Three lines have been written to MyFile.txt.")
