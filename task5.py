#Custom Split and Join Functions



# Custom split function
def my_split(sentence, separator):
    result = []  # List to store split items
    current_word = ""  # Temporary variable to hold each word

    for char in sentence:
        if char == separator:  # Check if the current character is the separator
            result.append(current_word)  # Add the current word to the result list
            current_word = ""  # Reset current word
        else:
            current_word += char  # Add character to current word

    result.append(current_word)  # Add the last word
    return result

# Custom join function
def my_join(items, separator):
    result = ""  # Initialize result string

    for i, item in enumerate(items):
        result += item  # Add item to result string
        if i < len(items) - 1:  # Add separator if not the last item
            result += separator

    return result

# Main function for testing
def main():
    sentence = input("Please enter sentence: ")
    split_sentence = my_split(sentence, " ")  # Split using space as separator
    print(my_join(split_sentence, ","))  # Join items with commas

    for word in split_sentence:  # Print each word on a new line
        print(word)

# Run the program
main()
