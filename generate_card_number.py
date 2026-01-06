import random
from datetime import datetime
class Generate:
    card = []

    def __init__(self, name, password, bank):
        self.name = name
        self.__end_date = datetime.now()
        self.__password = password
        self.bank = bank

    def date(self):
        time = self.__end_date
        return time.year + 5
    def show(self):
        return f"name {self.name} Bank {self.bank}"

    def password(self):
        return self.__password

    def show(self):
        return f"name {self.name} Bank {self.bank}"

    def send(self):
        for i in range(9):
            number = random.randint(1, 9)
            Generate.card.append(9860)
            Generate.card.append(number)
new = Generate('Davronbek',1234,'NBU')
print(new.show())
print(new.date())

