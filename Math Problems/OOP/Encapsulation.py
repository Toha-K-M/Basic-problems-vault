class bankAccount:

    def __init__(self, account_name = "Current Account", balance = 500):
        self.__account_name = account_name
        self.__balance = balance

    def viewBalance(self):
        print("balance: ", self.__balance)

    def withdrawMoney(self, value):
        if value > self.__balance:
            print("cant ")
        else:
            self.__balance = self.__balance - value
            print("New Balance ", self.__balance)


#acc_1 = bankAccount("c",2000) ebhabe dile change hoi
acc_1 = bankAccount()

print(acc_1.__dict__)

acc_1.viewBalance()
value = int(input("how much: "))
acc_1.withdrawMoney(value)
acc_1.viewBalance()