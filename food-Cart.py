# Shopping cart

foods = []
prices = []
total = 0

while True:
    food = input("Enter food you want to buy (type 'q' to quit): ").capitalize()
    if food.lower() == 'q':
        if not foods:  # Check if the cart is empty
            print("Your cart is empty.")
        break
    elif not food.strip():
        print("Food name cannot be empty. Please try again.")
        continue
    else:
        while True:  # Loop for price input until valid
            try:
                price = float(input(f"Enter price for {food}: $"))
                foods.append(food)
                prices.append(price)
                break  # Exit the price input loop if valid
            except ValueError:
                print("Please enter a valid price.")

if foods:
    print("\nYour shopping cart:")
    for i in range(len(foods)):
        print(f"{foods[i]:8} - ${prices[i]:.2f}")
        total += prices[i]

    print("----------------")
    print(f"Total: ${total:.2f}")
else:
    print("\nNo items in the cart.")
