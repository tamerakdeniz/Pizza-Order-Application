"""print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# todo: work out how much they need to pay based on their size choice.

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You have chosen an invalid size.")

# todo: work out how much to add to their bill based on their pepperoni choice.
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# todo: work out their final amount based on whether if they want extra cheese.
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
"""

def get_valid_input(prompt, valid_options):
    """Get and validate user input"""
    while True:
        user_input = input(prompt).upper()
        if user_input in valid_options:
            return user_input
        print(f"Invalid input. Please choose from {', '.join(valid_options)}")

def calculate_pizza_price(size, pepperoni, extra_cheese):
    """Calculate the total price of the pizza"""
    # Base prices
    prices = {
        'S': 15,
        'M': 20,
        'L': 25
    }
    
    # Calculate base price
    if size not in prices:
        return None
    
    total = prices[size]
    
    # Add pepperoni cost
    if pepperoni == 'Y':
        total += 2 if size == 'S' else 3
    
    # Add extra cheese
    if extra_cheese == 'Y':
        total += 1
    
    return total

def main():
    print("Welcome to Python Pizza Deliveries!")
    print("-" * 35)
    
    # Get pizza size
    size = get_valid_input(
        "What size pizza do you want? (S/M/L): ",
        ['S', 'M', 'L']
    )
    
    # Get pepperoni choice
    pepperoni = get_valid_input(
        "Do you want pepperoni? (Y/N): ",
        ['Y', 'N']
    )
    
    # Get extra cheese choice
    extra_cheese = get_valid_input(
        "Do you want extra cheese? (Y/N): ",
        ['Y', 'N']
    )
    
    # Calculate total bill
    bill = calculate_pizza_price(size, pepperoni, extra_cheese)
    
    # Display order summary
    print("\n=== Order Summary ===")
    print(f"Size: {'Small' if size == 'S' else 'Medium' if size == 'M' else 'Large'}")
    print(f"Pepperoni: {'Yes' if pepperoni == 'Y' else 'No'}")
    print(f"Extra Cheese: {'Yes' if extra_cheese == 'Y' else 'No'}")
    print(f"Total Bill: ${bill:.2f}")

if __name__ == "__main__":
    main()