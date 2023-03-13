from item import item


class Book(item):
    def __init__(self, code, title, description, category, picture, quantityInStock, price, ISBN, Author, synopsis):
        super().__init__(code, title, description, category, picture, quantityInStock, price)
        self.ISNB = ISBN
        self.author = Author
        self.synopsis = synopsis

    def preview(self):
        return self.preview


my_book = Book('b021', 'Be Yourself', 'a novel', 'inspirational', 'my_book_1.jpg', 100, 5000, '8700-0000567',
               'JOHN_MASON', 'telling to the readers to be honest and proud of who they are')
print(my_book.title)
print(my_book.author)
print(my_book.viewFullDescription)
print(my_book.preview())
