from teacher import Teacher


class Load(Teacher):
    def __init__(self, units):
        self.units = units

    def getUnits(self):
        return f'{self.units}'
