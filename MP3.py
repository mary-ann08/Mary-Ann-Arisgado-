from item import item


class MP3(item):
    def __init__(self, code, title, description, category, picture, quantityInStock, price, duration, artist):
        super().__init__(code, title, description, category, picture, quantityInStock, price)
        self.duration = duration
        self.artist = artist

    def playExtract(self):
        return self.playExtract()

    def download(self):
        return self.download()


my_MP3 = MP3('n001', 'Ballad_of_Monalisa', 'tragic', 'pop rock', 'my_MP3_1.jpg', 50, 10000.00, '3minutes', 'Panic_at_the_Disco')
pass

print('Title: ', my_MP3.title)
print('Duration: ', my_MP3.duration)
