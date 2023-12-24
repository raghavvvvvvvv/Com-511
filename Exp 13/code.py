
def extract_unique_words(file_path):
    unique_words = set()

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.split()
                for word in words:
                    # Remove punctuation and convert to lowercase for uniformity
                    cleaned_word = word.strip('.,!?()[]{}":;')
                    cleaned_word = cleaned_word.lower()
                    unique_words.add(cleaned_word)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

    return sorted(list(unique_words))

def main():
    file_path = input("Enter the path to the text file: ")

    unique_words = extract_unique_words(file_path)

    if unique_words:
        print("Unique words in alphabetical order:")
        for word in unique_words:
            print(word)
    else:
        print("No unique words found.")

if __name__ == "__main__":
    main()
