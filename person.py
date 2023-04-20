class Person:
    def __init__(self, id, lastname, firstname, middlename, type):
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
        self.middlename = middlename
        self.type = type

    def getName(self):
        return f'{self.lastname}, {self.firstname}, {self.middlename}'

