'''Consider the string Welcome to python world.Perform the following operations:
   Count the number of alphabets in the given string. 
   To extract charcaters in the given range from the given range. 
   Check if the string is alphanumeric or not'''


input_string = "Welcome to python world"

alphabet_count = sum(1 for char in input_string if char.isalpha())


start_index = 2
end_index = 8
extracted_characters = input_string[start_index:end_index]

is_alphanumeric = input_string.isalnum()

print(f"1. Number of alphabets in the string: {alphabet_count}")
print(f"2. Extracted characters in the range {start_index}-{end_index}: '{extracted_characters}'")
print(f"3. Is the string alphanumeric? {is_alphanumeric}")
