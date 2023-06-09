class item:
    def __init__(self, code, title, description, category, picture, quantityInStock, price):
        self.updateStockLevel = None
        self.list_of_actors = None
        self.code = code
        self.title = title
        self.description = description
        self.category = category
        self.picture = picture
        self.quantityInStock = quantityInStock
        self.price = price

    def viewFullDescription(self):
        print(f'{self.code} ({self.title}) - {self.description}')
        print(f'category: {self.category}')
        print(f'price: {self.price}')
        print(f'Quantity In stock: {self.quantityInStock}')

    def addToCart(self, quantityInStock):
        if quantityInStock <= self.quantityInStock:
            print(f'Added {quantityInStock} {self.title} to cart.')
        else:
            print('Not enough stock.')

    def updateStockLevel(self, new_quantity):
        self.updateStockLevel = new_quantity
        