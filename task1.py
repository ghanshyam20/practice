# Function to check the length of the user input and print appropriate message
def tester(givenstring="Too short"):
    # Check if the string is less than 10 characters
    if len(givenstring) < 10:
        print("Too short")
    else:
        print(givenstring)

# Main function to handle user input
def main():
    while True:
        user_input = input("Write something (quit ends): ")
        if user_input.lower() == "quit":  # End program if user types "quit"
            break
        tester(user_input)  # Pass user input to the tester function

# Run the program
main()
