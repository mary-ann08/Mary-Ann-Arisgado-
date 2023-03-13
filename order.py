class order:
    def __init__(self, date, status, shoppingCart, deliveryAddress, paymentMethod):
        self.date = date
        self.status = status
        self.shoppingCart = shoppingCart
        self.deliveryAddress = deliveryAddress
        self.paymentMethod = paymentMethod

    def validatePayment(self):
        return self.validatePayment

    def cancel(self):
        return self.cancel

    def dispatch(self):
        return self.dispatch

    def confirmDelivery(self):
        return self.confirmDelivery

    def refund(self):
        return self.refund

    def archive(self):
        return self.archive
