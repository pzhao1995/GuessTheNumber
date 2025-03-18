def display_items(items):
    print("\nAvailable items:")
    for item, price in items.items():
        print(f"{item}: ${price}")


def vending_machine():
    items = {
        "Pepsi": 3.00,
        "Lay's": 2.00,
        "Chocolate": 1.00,
        "Sprite": 2.75
    }

    while True:
        display_items(items)

        selection = input("\nPlease select an item (or type 'quit' to exit): ").capitalize()

        if selection == 'Quit':
            print("Thank you for using the vending machine!")
            break

        if selection not in items:
            print("Invalid selection, please choose again.")
            continue

        price = items[selection]
        print(f"You selected {selection}, which costs ${price:.2f}")

        try:
            money_inserted = float(input("Enter the amount of money you have: $"))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if money_inserted < price:
            print(f"Insufficient funds. You need ${price - money_inserted:.2f} more.")
        elif money_inserted > price:
            change = money_inserted - price
            print(f"Thank you for your purchase! Your change is ${change:.2f}.")
        else:
            print("Thank you for your purchase! The exact amount was received.")

        continue_choice = input("\nWould you like to make another purchase? (yes/no): ").lower()
        if continue_choice != 'yes':
            print("Thanks for using the vending machine!")
            break


vending_machine()