class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, name, price):
        try:
            price = float(price)
            product = {"name": name, "price": price}
            self.products.append(product)
            print("Product added.")
        except ValueError:
            print("Invalid price. Please enter a valid number.")

    def remove_product(self, name):
        for product in self.products:
            if product["name"] == name:
                self.products.remove(product)
                break

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product["price"]
        return total

    def print_receipt(self):
        print("----- Receipt -----")
        print("{:<15s} {:<10s}".format("Name", "Price"))
        print("-----------------------------")
        for product in self.products:
            name = product['name']
            price = product['price']
            print("{:<15s} {:<10.2f}".format(name, price))
        print("-----------------------------")
        total = self.calculate_total()
        print("{:<15s} {:<10.2f}".format("Total", total))

# Create a shopping cart
cart = ShoppingCart()

# Add, remove, and display items based on user input
while True:
    print("\n1. Add product")
    print("2. Remove product")
    print("3. Show items")
    # Remove Option 4 by not displaying the option for user.
    # print("4. Show total price") 
    print("5. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter the product name: ")
        price = input("Enter the product price: ")
        cart.add_product(name, price)

    elif choice == "2":
        name = input("Enter the product name to remove: ")
        initial_length = len(cart.products)
        cart.remove_product(name)
        if len(cart.products) == initial_length:
            print("Product not found in cart.")
        else:
            print("Product removed.")

    elif choice == "3":
        cart.print_receipt()

    elif choice == "4":
        total = cart.calculate_total()
        print(f"Total price: {total}")

    elif choice == "5":
        break

    else:
        print("Invalid choice.")

print("Thank you for using the shopping cart!")