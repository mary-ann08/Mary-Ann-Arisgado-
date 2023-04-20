from person import Person


class Teacher(Person):
    def __init__(self, id, lastname, firstname, middlename, type, department, position):
        super(). __init__(self, id, lastname, firstname, middlename)
        self.department = department
        self.position = position

    def getDept(self):
        return f'{self.department}'

    def getPosition(self):
        return f'{self.position}'


