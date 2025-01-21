#Grocery Shopping List

# Main function to handle the shopping list
def shopping_list():
    grocery_list = []  # Initialize an empty list for the grocery items

    while True:
        # Prompt user for an action
        choice = input("Would you like to\n(1) Add\n(2) Remove items\n(3) Quit?: ")

        if choice == "1":  # Add items
            item = input("What will be added?: ")
            grocery_list.append(item)

        elif choice == "2":  # Remove items
            print(f"There are {len(grocery_list)} items in the list.")
            try:
                index = int(input("Which item is deleted?: "))  # Get item index
                if 0 <= index < len(grocery_list):  # Check if index is valid
                    grocery_list.pop(index)
                else:
                    print("Incorrect selection.")
            except ValueError:
                print("Incorrect selection.")

        elif choice == "3":  # Quit
            print("The following items remain in the list:")
            for item in grocery_list:
                print(item)
            break

        else:  # Invalid input
            print("Incorrect selection.")

# Run the program
shopping_list()
