## Creating an order proccessing program with Python


from models.customer import Customer
from models.current_order import CurrentOrder
from models.totals import Totals
from models.ordersummary import OrderSummary

class Program:
    """Start of the application"""

    def main(self):
        """The main function"""
        customer = self.input_customer_details()
        current_order = self.input_current_order()
        order_items = self.input_order_items()
        order_summary = OrderSummary(order_items)
        order_totals = Totals(order_items)
        customer.formatted()
        current_order.formatted()
        order_summary.formatted()
        order_totals.formatted()


    def input_customer_details(self):
        print("\nEnter the customer information")
        first_name = input("\tWhat is the customer's first name? ")
        last_name = input("\tWhat is the customer's last name? ")
        email_address = input("\tWhat is the customer's e-mail address? ")
        return Customer(first_name, last_name, email_address)

    def input_current_order(self):
        order_number = input("\nWhat is the order number? ")
        order_description = input("\nWhat is the order description? (limit 60 characters) ")
        return CurrentOrder(order_number, order_description)
     
    def input_order_items(self):
        line_number = input("\nHow many items are included in this order? ")
        line_number = int(line_number)
        print("\nPlease enter the following information:")
        counter = 0
        order_lines = []
        while counter < line_number:
            counter += 1
            print(f"\nFor item number {counter}:")
            part_number = input("\tWhat is the part number? ")
            unit_cost = input("\tWhat is the unit cost? ")
            quantity = input("\tHow many units? ")
            order_line = [part_number, unit_cost, quantity]
            order_lines.append(order_line)
        return order_lines

    
if __name__ == '__main__':
    program = Program()
    program.main()

