class Person: 
    def __init__(self, name, age, prof): # self = this (método construtor)
        self.name = name
        self.age = age
        self.prof = prof

    def toString(self):
        return ('{:<20}{:<15}{:<5}' .format(self.name, self.prof, self.age))
