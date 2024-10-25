import datetime
import random
class Bank:
    def __init__(self,name,total_balance):
        self.name=name
        self.user_account=[]
        self.admin_account=[]
        self.total_balance=total_balance
        self.loan_user=0
        self.loan_feature=True

    def add_user(self,user):
        self.user_account.append(user)

    def add_admin(self,admin):
        self.admin_account.append(admin)

    def show(self):
        for item in self.user_account:
            print(item.name,item.account_no)

class User():
    number=0
    @classmethod
    def change_number(cls):
        cls.number+=1

    def __init__(self,name,email,address,account_type):
        self.name=name
        self.email=email
        self.address=address
        self.account_type=account_type
        self.withdraw_limit=3
        self.withdraw=0
        self.balance=0
        self.history=[]
        self.loan=0
        self.loan_time=0
        self.account_no=User.number
        User.change_number()

    def deposit(self,amount,bank):
        self.balance+=amount
        bank.total_balance+=amount
        print(f'Scuccefully deposited {amount}tk')  
        current_time=datetime.datetime.now()
        self.history.append(f'you have deposited {amount}tk at {current_time}') 

    def withdraw_money(self,amount,bank):
        if self.balance<amount:
            print('not enough money')
            return
        elif self.account_type!='Savings':
            self.balance-=amount
            bank.total_balance-=amount
            print(f'Succesfully withdrwaed {amount}tk') 
            current_time=datetime.datetime.now()
            self.history.append(f'you have withdraw {amount}tk at {current_time}') 
        elif self.balance>=amount and bank.total_balance<amount:
            print('the bank is bankrupt')
        else:
            if self.withdraw_limit>self.withdraw :
                self.withdraw+=1
                self.balance-=amount    
                bank.total_balance-=amount   
                print(f'Succesfully withdrwaed {amount}tk')
                current_time=datetime.datetime.now()
                self.history.append(f'you have withdrawed {amount}tk at {current_time}') 
            elif self.withdraw_limit<=self.withdraw:
                print('Reached limit')

    def take_loan(self,amount,bank):
        if bank.loan_feature==True:
            if self.loan_time<2 and bank.total_balance>=amount:
                self.loan+=amount
                self.balance+=amount
                self.loan_time+=1
                bank.loan_user+=amount
                bank.total_balance-=amount
                print(f'loaned {amount}tk')
                current_time=datetime.datetime.now()
                self.history.append(f'you have loaned {amount}tk at {current_time}') 
            elif bank.total_balance<amount:
                  print('the bank is bankrupt')
            else:
                print('reached limit')
        elif bank.loan_feature==False:
            print('Feature not available')

    def transfer_money(self,amount,id,bank):
        if self.balance<amount:
            print('not enough money')
            return
        elif self.balance>=amount:
            a=False
            for item in bank.user_account:
                if item.account_no==id:
                    self.balance-=amount
                    item.balance+=amount
                    print('transfer successfull')
                    current_time=datetime.datetime.now()
                    self.history.append(f'you have transfered {amount}tk at {current_time}') 
                    a=True
            if a==False:
                print('Account not exist')

    def check_balance(self):
        print(f'balance: {self.balance}') 

    def accountNum(self):
        print(self.account_no) 
    
    def history_show(self):
        for item in self.history:
            print(item)

class Admin:
    def __init__(self,name,email):
        self.name=name
        self.email=email

    def delete_account(self,name,id,bank):
        for item in bank.user_account:
            if item.name==name and item.account_no==id:
                bank.user_account.remove(item)
                print('user deleted successfully')
    
    def show_users(self,bank):
        for item in bank.user_account:
            print(f'Name : {item.name}, Id : {item.account_no}, Balance : {item.balance}')

    def total(self,bank):
        print(f'Total Balance:{bank.total_balance}')

    def loan_money(self,bank):
        print(f'Total loan:{bank.loan_user}')

    def loan_on_off(self,bank):
        bank.loan_feature=False
