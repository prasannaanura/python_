class Product:
    """Represents a product in the supermarket."""
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - ${self.price} (Stock: {self.stock})"

class Supermarket:
    """Represents the supermarket inventory and customer cart."""
    def __init__(self):
        self.products = {
            "apple": Product("Apple", 1.5, 5),  # Reduced stock for testing
            "banana": Product("Banana", 0.5, 10),
            "milk": Product("Milk", 2.0, 3),
            "bread": Product("Bread", 1.8, 7),
        }
        self.cart = {}

    def display_products(self):
        """Displays available products."""
        print("\nAvailable Products:")
        for key, product in self.products.items():
            print(f"{key}: {product}")

    def add_to_cart(self, product_name):
        """Adds a product to the shopping cart with stock validation."""
        if product_name not in self.products:
            print("❌ Product not found!")
            return
        
        product = self.products[product_name]

        while True:
            try:
                quantity = int(input(f"Enter quantity for {product.name} (Available: {product.stock}): "))
                if quantity > product.stock:
                    print(f"⚠️ Only {product.stock} {product.name}(s) available. Please enter a valid quantity.")
                elif quantity <= 0:
                    print("❌ Quantity must be greater than zero.")
                else:
                    break  # Valid quantity entered
            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")

        # Add to cart
        if product_name in self.cart:
            self.cart[product_name]["quantity"] += quantity
        else:
            self.cart[product_name] = {"product": product, "quantity": quantity}

        product.stock -= quantity
        print(f"✅ Added {quantity} {product.name}(s) to the cart.")

    def view_cart(self):
        """Displays the items in the cart."""
        if not self.cart:
            print("\n🛒 Your cart is empty.")
            return
        
        print("\n🛒 Your Cart:")
        for item in self.cart.values():
            product = item["product"]
            quantity = item["quantity"]
            print(f"{product.name} - ${product.price} x {quantity} = ${product.price * quantity}")

    def checkout(self):
        """Calculates total bill and generates a receipt."""
        if not self.cart:
            print("❌ Your cart is empty. Add products before checkout!")
            return

        total = sum(item["product"].price * item["quantity"] for item in self.cart.values())
        discount = 0.1 * total if total > 20 else 0  # 10% discount if total is more than $20
        final_total = total - discount

        print("\n🧾 Bill Receipt:")
        self.view_cart()
        print(f"\nSubtotal: ${total:.2f}")
        print(f"Discount: -${discount:.2f}")
        print(f"Total Amount: ${final_total:.2f}")
        print("✅ Thank you for shopping with us!")

# Main Program
if __name__ == "__main__":
    supermarket = Supermarket()

    while True:
        print("\n📌 Supermarket Menu:")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            supermarket.display_products()
        elif choice == "2":
            product_name = input("Enter product name: ").lower()
            supermarket.add_to_cart(product_name)
        elif choice == "3":
            supermarket.view_cart()
        elif choice == "4":
            supermarket.checkout()
            break  # Exit after checkout
        elif choice == "5":
            print("🛑 Exiting... Thank you for visiting!")
            break
        else:
            print("❌ Invalid choice! Please try again.")
