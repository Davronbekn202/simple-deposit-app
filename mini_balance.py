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
        make_user = input("Create username: ")
        make_pass = input("Create password: ")

        if make_user not in self.information:
            self.information[make_user] = {
                "password": make_pass,
                "balance": []
            }
            print("Registration successful!")
        else:
            print("Username already exists!")

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


if __name__ == "__main__":
    app = Balance()
    app.obtaining()

