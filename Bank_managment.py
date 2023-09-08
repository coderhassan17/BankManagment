Accounts = []
running = True
def create_acc():
    Name = input("Enter your Name : ")
    Account_num = int(input("Enter your 5 digit Account Number : "))
    is_found=False
    for i in range(0,len(Accounts)):
        if Account_num == Accounts[i]["account_number"]:
            print("This account number already in use. Plase continue with another Account Number.")
            is_found=True
            return
        
    if not is_found:
        
        Initial_bal = input("Enter your opening balance : ")
        if Initial_bal.isdigit():
            
            if int(Initial_bal) < 1000:
                print("Initial Balance minimum 1000.Your account is not created.")
            else:
                New_acc = {"name" : Name , "account_number" : Account_num , "initial_balance " : Initial_bal,"total_balance" : Initial_bal}
                Accounts.append(New_acc)
        else:
            print("Enter only number")
def view_acc():
    Account_num = input("Enter your account number :")
    for i in range(0,len(Accounts)):
        if int(Account_num)==Accounts[i]["account_number"]:
            print("Account Name :",Accounts[i]["name"],"Account Number :",Accounts[i]["account_number"],"Account Balance :",Accounts[i]["total_balance"])
        else:
            print("Enter correct Account number.")
def total_acc():
    print("Total account on this bank ",len(Accounts))
def send_money():
    balance = input("Enter balance you want to send :")
    sender_acc = input("Enter sender account number :")
    receiver_acc = input("Enter receiver account number :")
    is_found=False
    if balance.isdigit():
        if(int(balance)>0):
            for i in range(0,len(Accounts)):
                if sender_acc == Accounts[i]["account_number"]:
                    if Accounts[i]["total_balance"] > int(balance):
                        for j in range(0,len(Accounts)):
                            if  receiver_acc == Accounts[j]["account_number"]:
                                Accounts[j]["total_balance"]= Accounts[j]["total_balance"] + int(balance)
                            else:
                              print("No account number found")
                            is_found=True
                            return
                        if not is_found:
                            Accounts[i]["total_balance"]= Accounts[i]["total_balance"]-int(balance)
                    else:
                        print("You have insufficient balance.Try Again ")
                else:
                    print("No account number found")
        else:
            print("You enter balance in negative :")   
    print("Enter only number")            
def deposit():
    account_num = input("Enter account number: ")
    balance = input("Enter amount you want to deposit : ")
    if balance.isdigit():
        if(int(balance)>0):  
            for i in range(0,len(Accounts)):
                if int(account_num) == Accounts[i]["account_number"]:
                        Accounts[i]["total_balance"]= Accounts[i]["total_balance"]+int(balance)
            print("You have deposit successfully")
        else:
            print("You Enter negative balance")
    else:
            print("Enter only number")
def withdraw():
    account_num = input("Enter account number: ")
    balance = input("Enter amount you want to withdraw: ")
    if balance.isdigit():
        if(int(balance)>0):
            for i in range(0,len(Accounts)):
                if int(account_num) == Accounts[i]["account_number"]:
                    if Accounts[i]["total_balance"] > int(balance):
                        Accounts[i]["total_balance"] = Accounts[i]["total_balance"]-int(balance)
                    else:
                        print("You have insufficient balance .Try Again")
                else:
                    print("No account found")   
        else:
            print("You enter balance in negative")
    else:
        print("Enter only number")    
while running:
    print("1.Create Account")
    print("2.View Account")
    print("3.Total Accounts")
    print("4.Send Money")
    print("5.Deposit Money")
    print("6.Withdraw")
    print("7.Exit")
    choice = input("Enter the choice : ")

    if choice.isdigit():
        if int(choice) == 1:
            create_acc()
        elif int(choice) == 2:
            view_acc()
        elif int(choice) == 3:
            total_acc()
        elif int(choice) == 4:
            send_money()
        elif int(choice) == 5:
            deposit()
        elif int(choice) == 6:
            withdraw()
        elif int(choice) == 7:
            print("exit")
            running = False
        else:
            print("Please enter correct choice")
    else:
        print("Enter only number ")