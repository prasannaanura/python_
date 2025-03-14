# Shopping cart

foods = []
prices = []
total = 0

while True:
    food = input("Enter food you want to buy (type q to quit): ").capitalize()
    if food.lower() == 'q':
        if not foods:  # Check if the cart is empty
            print("Your cart is empty.")
            
        break
    else:
        try:
            price = float(input(f"Enter price for {food}: $:  "))
            foods.append(food)
            prices.append(price)
        except ValueError:
            print("Please enter a valid price.")
            

if  foods == True:
 print("your shoping cart")
if foods:
    print("your cart is full")
    for i in range(len(foods)):
        print(f"{foods[i]:8} - ${prices[i]:.2f} ")
        total += prices[i]

    print("----------------")
    print(f"Total: ${total:.2f}")
else:
    print("No items in the cart.")
