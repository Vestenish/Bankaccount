class Bankaccount():
    def register(self): 
        while True:
            self.username = None
            self.password = None

            username = input("Please write your desired username: ")
            self.username = username  
            if self.username.strip() == "":
                print("Username can't be empty")
                continue
            else:          
                password = input("Please write your desired password: ")
            self.password = password
            if self.password.strip() == "":
                print("Your password can't be empty")
                continue
            else:
                return

    def login(self):
        while True:
            login_username = input("Enter your username: ")
            if login_username != self.username:
                print("Incorrect username. Please try again.")
                continue

            login_password = input("Enter your password: ")
            if login_password != self.password:
                print("Incorrect password. Please try again.")
                continue

            print("Login successful!")
            break

        self.bakiye = 3.0

    def sorgu(self):
        while True:
            self.sorgulama = input("Which operation would you like to perform? (deposito or withdraw)")
            if self.sorgulama == "deposito":
                self.deposito()
                print("Transaction completed")
                break
            elif self.sorgulama == "withdraw":
                self.withdraw()
                print("Transaction completed")
                break
            else:
                print("Invalid operation")

    def deposito(self):   
        self.deposit = int(input("How much would you like to deposit? --> deposit: "))
        self.bakiye += self.deposit
        print(f"{self.deposit} units added. Your new balance: {self.bakiye}")

    def withdraw(self):
        self.çekilen = int(input("How much would you like to withdraw? --> withdraw: ")) 
        if self.çekilen > self.bakiye:
            print("Insufficient funds.")
        else:
            self.bakiye -= self.çekilen
            print(f"{self.çekilen} units withdrawn. Your new balance: {self.bakiye}")


hesap = Bankaccount()
hesap.register()
hesap.login()
hesap.sorgu()