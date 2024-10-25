from Bank import Bank,User,Admin

bank=Bank('BD BANK',10000)

bank.add_user(User('rahim','rahim@gamil.com','Dhaka','Savings'))
bank.add_user(User('Karim','kahim@gamil.com','uganda','current'))
bank.add_user(User('farik','farik@gamil.com','chittagong','Savings'))
bank.add_user(User('YOUTube','youtube@gamil.com','usa','Current'))

bank.add_admin(Admin('minhaj','minhaj@gmail.com'))
bank.add_admin(Admin('Kamal','kamal@gmail.com'))

while True:
    print('***welcome to our Bank***')
    print('Are you Admin or User?')
    print('press 1 for user account')
    print('press 2 for admin account')
    print('press 3 for exit')
    choice=input('Enter number:')
    if choice=='1':
        print('Do you have an account?press 1 for Yes and 2 for No')
        my_choice=input('Enter Number: ')
        if my_choice=='1':
            ac_Id=int(input('Enter your Account id:'))  
            for item in bank.user_account:
                if item. account_no==ac_Id:
                    while True:
                        print("***welcome***")
                        print("1.For deposite")
                        print("2.For withdraw")
                        print("3.For transfer")
                        print("4.For loan")
                        print("5.For show account status")
                        print('6.For transaction history')
                        print("7.For exit")
                        i=int(input('Enter NUMBER:'))
                        if i==1:
                            amount=int(input("enter amount:"))
                            item.deposit(amount,bank)
                        elif i==2:
                            amount=int(input("enter amount:"))
                            item.withdraw_money(amount,bank)
                        elif i==3:
                            amount=int(input("enter amount:"))
                            id=int(input('Id:'))
                            item.transfer_money(amount,id,bank)  
                        elif i==4:
                            amount=int(input("enter amount:"))
                            item.take_loan(amount,bank)
                        elif i==5:
                            print(f"Name:{item.name},id:{item.account_no},balance:{item.balance},loan:{item.loan}")
                        elif i==6:
                            item.history_show()
                        elif i==7:
                            break
        if my_choice=='2':
            Name=input('enter Name:')
            email=input('email:')
            address=input('address:')
            account_type=input('account type Savings or current:')
            my_account=User(Name,email,address,account_type)
            bank.add_user(my_account)
            print(f'your account id:{my_account.account_no}')

    if choice=='2':
        print("Do you have an account??1 for yes 2 for no")
        a=input('Enter number:')
        if a=='2':
            name=input('Enter Name as password:')
            email=input('Enter email')
            bank.add_admin(Admin(name,email))
            print(f'use name for login')
        if a=='1':
            name=input('Enter name:')
            my_admin=None
            for item in bank.admin_account:
                if item.name==name:
                    my_admin=item
            if my_admin==None:
                print('Fake admin out')
                break        
            while True:
                x=True
                for item in bank.admin_account:
                    if item.name==name:
                        print("1.For delete user's account")
                        print("2.For see all user account")
                        print("3.For total available balance")
                        print('4.For total loan')
                        print('5.For on/off loan feature of bank')
                        print('6.For exit')
                        d=input('enter number:')
                        if d=='1':
                            name=input('enter user name:')
                            id=int(input('Enter id:'))
                            my_admin.delete_account(name,id,bank)
                        if d=='2':
                            my_admin.show_users(bank)
                        if d=='3':
                            my_admin.total(bank)
                        if d=='4':
                            my_admin.loan_money(bank)
                        if d=='5':
                            bank.loan_feature=False 
                            print('Loan feature disabled')       
                        if d=='6':
                            x=False
                            break
                if x==False:
                    break        



    if choice=='3':
        break

            