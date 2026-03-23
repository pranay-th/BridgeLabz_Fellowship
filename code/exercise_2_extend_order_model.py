"""
Exercise 2:
Extend the model above:
- Add a method `add_product()` to the `Order` class.  
- Add an attribute `order_id` generated using `uuid4`.  
- Display order details (customer name, product list, total).

Hint: Use the `uuid` module.
"""
import uuid

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Order:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products
        self.order_id = uuid.uuid4()

    def total_price(self):
        return sum(p.price for p in self.products)

    def add_product(self, product):
        self.products.append(product)

    def display_order(self):
        print(f"Customer Name: {self.customer.name}")
        print(f"Product list: {[p.name for p in self.products]}")
        print(f"Total Price: ${self.total_price():.2f}")

p1 = Product("Apple", 1.50)
p2 = Product("Banana", 0.75)
customer = Customer("John Doe", "john@example.com")
order = Order(customer, [p1, p2])
order.add_product(Product("Cherry", 2.00))
order.display_order()
print(f"Order ID: {order.order_id}")
