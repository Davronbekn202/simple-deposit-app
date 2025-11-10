class Balance:

    def __init__(self, balance=0):
        self.information = {}
        self.balance = balance

    def obtaining(self):
        get_info = input("enter username:")
        get_passkey = input("enter password:")
        get_money = input("enter money $")
        self.information = {get_info: get_passkey}
        self.balance = get_money

    def login(self):
        get_info = input("enter username:")
        get_passkey = input("enter password:")
        if get_info in self.information.keys() and self.information[get_info] == get_passkey:
            print("login success")
            print(self.show())
        else:
            print("login failed try again")

    def show(self):
        return f"your balance have {self.balance}$"


if __name__ == "__main__":
    all = Balance()
    all.obtaining()
    all.login()