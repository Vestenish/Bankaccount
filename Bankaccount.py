class Bankaccount():
    def register(self): 
        while True:
            self.username = None
            self.password = None

            username = input("Please write your username you want: ")
            self.username = username  
            if self.username.strip() == "":
                print("Username can't be empty")
                continue
            else:          
                password = input("Please write the password you want: ")
            self.password = password
            if self.password.strip() == "":
                print("Your password can't be empty")
                continue
            else:
                return

    def login(self):
        while True:
            login_username = input("Login with your username --> ")
            if login_username != self.username:
                print("Username is incorrect. Try again.")
                continue

            login_password = input("Login with your password --> ")
            if login_password != self.password:
                print("Password is incorrect. Try again.")
                continue

            print("Login successful!")
            break

        self.bakiye = 3.0

    def sorgu(self):
        while True:
            self.sorgulama = input("Hangi işlemi gerçekleştirmek istersiniz: ")
            if self.sorgulama == "deposito":
                self.deposito()
                print("İşlem tamamlandı")
                break
            elif self.sorgulama == "withdraw":
                self.withdraw()
                print("İşlem tamamlandı")
                break
            else:
                print("Geçersiz işlem")

    def deposito(self):   
        self.deposit = int(input("Ne kadar yüklemek istersiniz? --> deposit: "))
        self.bakiye += self.deposit
        print(f"{self.deposit} birim eklendi. Yeni bakiyeniz: {self.bakiye}")

    def withdraw(self):
        self.çekilen = int(input("Ne kadar çekmek istersiniz? --> withdraw: ")) 
        if self.çekilen > self.bakiye:
            print("Yetersiz bakiye.")
        else:
            self.bakiye -= self.çekilen
            print(f"{self.çekilen} birim çekildi. Yeni bakiyeniz: {self.bakiye}")


hesap = Bankaccount()
hesap.register()
hesap.login()
hesap.sorgu()