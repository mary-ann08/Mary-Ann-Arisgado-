from person import Person


class Student(Person):
    def __init__(self, ID, lastname, firstname, middlename, type, year, course, section):
        super().__init__(ID, lastname, firstname, middlename, type)

        self.year = year
        self.course = course
        self.section = section

    def getCourse(self):
        return f'{self.year}/{self.course}/{self.section}'


