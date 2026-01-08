import random
from sql import *
class Balance:

    def __init__(self):
        self.information = {
            #by default
            "davronbek": {
                "password": "12345",
                "balance": [100]
            }
        }

    def register(self):
        email = input("Create email: ")
        make_pass = input("Create password: ")
        add_info(email,make_pass)


    def obtaining(self):
        while True:
            get_info = input("Enter username: ")
            get_passkey = input("Enter password: ")

            if get_info in self.information and get_passkey == self.information[get_info]["password"]:
                print(f"Login successful! Current balance: {sum(self.information[get_info]['balance'])}")

                get_money = input("Enter money to deposit: ")
                if get_money.isdigit():
                    get_money = int(get_money)
                    self.information[get_info]["balance"].append(get_money)
                    print(f"You deposited {get_money}$")
                else:
                    print("Invalid amount!")
                    break

            else:
                print("Incorrect username or password.")
                ask = input("Do you want to register yes/no: ").lower()

                if ask == "yes":
                    self.register()
                else:
                    continue

    def show(self, username):
        return f"Your balance: {self.information[username]['balance']}"

class Card:
    card_number =[9,8,6,0]
    def __init__(self,username,age,password):
        self.username = username
        self.age = age
        self.password = password



    def card_numbers(self):
        for i in range(12):
                Card.card_number.append(random.randint(0, 9))


    def get_card(self):
        self.card_numbers()
        print("Karta nomer :",*self.card_number)
        print("Username",self.username)
        print("Yoshi:",self.age)
        print("Paroli:",self.password)


if __name__ == "__main__":
    app = Balance()
    app.obtaining()


