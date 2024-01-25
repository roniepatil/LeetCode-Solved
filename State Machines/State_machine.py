# Create state interface class
# Which outlines the methods that concrete states must implement.
class CheckoutState:
    def add_item(self, item):
        pass

    def review_cart(self):
        pass

    def enter_shipping_info(self, info):
        pass

    def process_payment(self):
        pass


# Create concrete state class
# Each concrete state encapsulates specific behaviors associated with its respective state.
class EmptyCartState(CheckoutState):
    def add_item(self, item):
        print("Item added to cart.")
        return ItemAddedState()
    

class ItemAddedState(CheckoutState):
    def add_item(self, item):
        print("Item added to cart.")

    def review_cart(self):
        print("Reviewing cart's content")
        return CartReviewedState()
    
class CartReviewedState(CheckoutState):
    def enter_shipping_info(self, info):
        print("Shipping info added.")
        return ShippingInfoEnteredState()
    
class ShippingInfoEnteredState(CheckoutState):
    def process_payment(self):
        print("Payment processed.")


# Create Context class
# It maintains a reference to the current state and delegates actions to that state. 
# The context class ensures a seamless transition between states and keeps track of the current state.

class CheckoutContext:
    def __init__(self):
        self.current_state = EmptyCartState()
    
    def add_item(self, item):
        self.current_state = self.current_state.add_item(item)

    def review_cart(self):
        self.current_state = self.current_state.review_cart()

    def enter_shipping_info(self, info):
        self.current_state = self.current_state.enter_shipping_info(info)
    
    def process_payment(self):
        self.current_state = self.current_state.process_payment()

if __name__ == "__main__":
    cart = CheckoutContext()
    cart.add_item("product 1")
    cart.review_cart()
    cart.enter_shipping_info("200 tr dr")
    cart.process_payment()