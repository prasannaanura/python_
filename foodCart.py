# shoping cart

foods = []
prices = []
total = 0

while True:
    food = input("Enter food you wnat to buy (type q to quit)")
    if food.lower() == 'q':
        
        print("your cart is empty")
        break
    else:
        price = float(input(f"enter price {food}"))
        foods.append(food)
        prices.append(price)

print("-----------your cart----------------")
for food,price in zip(foods,prices):
    total += price
    print(f"{food:8}- ${price:.2f}")
print("Total is : $",total)
    
    

