class ATM(object):
    def __init__(self,cardnumber,pin,init_bal):
        self.cardnumber=cardnumber
        self.pin=pin
        self.init_bal=init_bal
    def checkBalance(self,cardnumber,pin):
        if(cardnumber==123):
            print("Your balance is 500$")
        else:
            print("Invalid card number entered")
    def cashWithDrawl(self,cardnumber,amount):
        if(amount>self.init_bal):
            print("Not enough balance")
        else:
            new_balance=self.init_bal-amount
            self.init_bal=new_balance
            print(str(new_balance)+"$ Is the new balance")
customer1=ATM(123,3901,500)
customer1.checkBalance(123,3901)
customer1.cashWithDrawl(123,200)
customer1.checkBalance(456,3901)
customer1.cashWithDrawl(123,200)
customer1.cashWithDrawl(123,700)
    