from item import item


class DVD(item):
    def __init__(self, code, title, description, category, picture, quantityInStock, price, director, certificate,
                 list_of_actors):
        super().__init__(code, title, description, category, picture, quantityInStock, price)
        self.director = director
        self.certificate = certificate
        self.list_of_actors = list_of_actors


my_dvd = DVD('R002', 'Creeping', 'he/she cheated on his/her lover', 'drama', 'my_dvd.jpg', 2, 100.00, 'Conor',
             'music award', 'conor, anth')
pass

print('Title: ', my_dvd.title)
print('Actors: ', my_dvd.list_of_actors)
