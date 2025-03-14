# Function to calculate the total price
def calculate_total(price, quantity):
    return price * quantity

# Function to display a receipt in rows using a for loop
def print_receipt(item, price, quantity):
    receipt = [
        ["Item", item],
        ["Price per unit", f"${price}"],
        ["Quantity", quantity],
        ["Total Price", f"${calculate_total(price, quantity)}"]
    ]

    print("\n--- Receipt ---")
    for row in receipt:
        print(f"{row[0]:<15}: {row[1]}")  # Formatting for neat alignment

# Function to get user input
def get_input():
    item = input("Enter item name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    print_receipt(item, price, quantity)

# Loop to allow multiple inputs
while True:
    get_input()
    choice = input("Do you want to add another item? (yes/no): ").strip().lower()
    if choice != "yes":
        print("Thank you for shopping!")
        break  # Exit the loop if the user enters anything other than 'yes'
