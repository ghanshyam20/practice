#Supermarket Program


# Main function for the supermarket program
def supermarket():
    prices = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]  # Product prices
    total_sum = 0  # Initialize total price

    print("Supermarket\n===========")

    while True:
        try:
            # Prompt user to select a product
            product_number = int(input("Please select product (1-10) 0 to Quit: "))
            if product_number == 0:  # Quit if user enters 0
                break
            elif 1 <= product_number <= 10:  # Check valid product number
                price = prices[product_number - 1]  # Get product price
                total_sum += price  # Add price to total
                print(f"Product: {product_number} Price: {price}")
            else:
                print("Invalid product number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Display total sum and calculate change
    print(f"Total: {total_sum}")
    payment = int(input("Payment: "))
    print(f"Change: {payment - total_sum}")

# Run the program
supermarket()
