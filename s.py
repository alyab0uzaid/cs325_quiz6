class OrderDetails:
    def __init__(self, customer_info, items, shipping_address):
        self.customer_info = customer_info
        self.items = items
        self.shipping_address = shipping_address

    def display_order_details(self):
        print("Customer Information:", self.customer_info)
        print("Items:", self.items)
        print("Shipping Address:", self.shipping_address)


class OrderCalculator:
    TAX_RATE = 0.1  # Example tax rate

    @staticmethod
    def calculate_total_order_cost(items):
        total_cost = sum(item['price'] for item in items)
        total_cost += total_cost * OrderCalculator.TAX_RATE
        return total_cost


class OrderValidator:
    @staticmethod
    def validate_order_data(order_details):
        # Example validation logic
        if not order_details.customer_info:
            raise ValueError("Customer information is missing")
        if not order_details.items:
            raise ValueError("No items in the order")
        if not order_details.shipping_address:
            raise ValueError("Shipping address is missing")
        print("Order data validation successful")


class EmailSender:
    @staticmethod
    def send_order_confirmation_email(customer_email):
        # Example email sending logic
        print("Sending order confirmation email to", customer_email)


class InventoryManager:
    @staticmethod
    def update_inventory(items):
        # Example inventory update logic
        print("Updating inventory levels after order processing")


def main():
    # Dummy values
    customer_info = {'name': 'John Doe', 'email': 'john@example.com'}
    items = [{'name': 'Product 1', 'price': 50}, {'name': 'Product 2', 'price': 30}]
    shipping_address = {'address': '123 Street, City, Country'}

    # Create instances of new classes
    order_details = OrderDetails(customer_info, items, shipping_address)

    # Call methods accordingly
    order_details.display_order_details()

    try:
        OrderValidator.validate_order_data(order_details)
    except ValueError as e:
        print("Error:", e)

    total_cost = OrderCalculator.calculate_total_order_cost(items)
    print("Total Order Cost:", total_cost)

    EmailSender.send_order_confirmation_email(customer_info['email'])

    InventoryManager.update_inventory(items)


if __name__ == "__main__":
    main()