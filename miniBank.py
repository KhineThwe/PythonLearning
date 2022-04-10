import sys
import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  # for email checking

def check(email):
    uEmailFlag = None
    if (re.search(regex, email)):
        print("Valid Email")
        return True
    else:
        print("Invalid Email")
        return False

class BankSystem:
    users_list:dict = {}

    def __init__(self):
        pass

    def creationUser(self,username,password,email):
        listLength=len(self.users_list)+1
        moneyAmount:int=int(input("Enter your money amount"))
        form={listLength:{"username":username,"userPwd":password,"userEmail":email,"balance":moneyAmount}}
        self.users_list.update(form)
        print("User creation Successful!!")
        print("All data: ",self.users_list)

    def main_menu(self):
        print()
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Welcome to the Python Bank System")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) login")
        print("2) Register")
        print("3) Quit Python Bank System")
        print(" ")
        option = int(input("Choose your option: "))
        return option

    def run_main_options(self,user_obj):
        loop = 1
        while loop == 1:
            choice = self.main_menu()
            if choice == 1:
                user_obj=self.user_login(user_obj)
                if user_obj != None:
                    self.run_user_options(user_obj)
            elif choice == 2:
                user_obj=self.register()
                if user_obj != None:
                    self.run_user_options(user_obj)
            elif choice == 3:
                 # loop = 0
                 print("\n Thank-You for stopping by the bank!")
                 sys.exit()

    def user_menu(self, user_obj):
        # print the options you have
        print(" ")
        print(
            "Welcome User %s : Avilable options are:" % (self.name))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Transfer money")
        print("2) Deposit")
        print("3) Withdraw")
        print("4) Update customer's Name")
        print("5) Update customer's Password")
        print("6) Print all customers detail")
        print("7) Sign out")
        print(" ")
        option = int(input("Choose your option: "))
        return option

    def run_account_options(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Back to main menu")
        print("2) Sign out")
        option = int(input("Choose your option: "))
        loop = 1
        while loop == 1:
            if option == 1:
                self.main_menu()
            elif choice == 2:
                print("\n Thank-You for stopping by the bank!")
                sys.exit()

    def run_user_options(self, user_obj):
        loop = 1
        while loop == 1:
            choice = self.user_menu(user_obj)
            if choice == 1:
                transferFlag=self.transferMoney()
                print(self.users_list)
                if  transferFlag != None:
                    self.run_account_options()
            elif choice == 2:
                self.deposit()

            elif choice == 3:
                 self.withdraw()

            elif choice == 4:
                 self.updateName()

            elif choice == 5:
                 self.updatePwd()

            elif choice == 6:
                 self.print_all_accounts_details()

            elif choice == 7:
                 print("Exist from user menu")
                 sys.exit()

        print("\n Exit account operations")

    def checkinguserNameAndPwd(self,name,pwd):
        listLen = len(self.users_list)+1
        print("User Length", listLen)
        for i in range(1,listLen):
            if (name == self.users_list[i]["username"] and pwd == self.users_list[i]['userPwd']):
                print(f"{name} logged in")
                return i
        return 0

    def checkinguserName(self,name):
        listLen = len(self.users_list)
        print("User Length", listLen)
        for i in range(1,listLen+1):
            if (name == self.users_list[i]["username"] ):
                return i
        return 0

    def checkingLoginInfo(self,name,pwd):
         flag:bool = self.checkinguserNameAndPwd(name,pwd)
         print("User Id",flag)
         if(flag):
             print("This user exists in usersList")
             return flag
         else:
             print("This user does not exist in usersList,Please register first")
             return flag


    def checkingLoginId(self, name):
        flag: bool = self.checkinguserName(name)
        print("User Id", flag)
        if (flag):
            return flag
        else:
            return flag

    def user_login(self,user_obj):
        name = input("\n Please input username to login: ")
        pwd = input("\n Please input password to login: ")
        flag = self.checkingLoginInfo(name,pwd)
        if(flag):
            self.run_user_options(user_obj)
        else:
            self.main_menu()
        print(self.users_list)

    def checkName(self,name):
        self.name=name
        checkNameFlag=None
        if len(str(name)) > 1 and len(str(name)) < 7:
            print("Valid name")
            checkNameFlag=True
        else:
            print("Invalid name")
            checkNameFlag = False
        return checkNameFlag

    def register(self):
        name = input("\n Please input username to register: ")
        email=input("\n Please input email to register")
        emailCheckFlag = check(email)
        if (emailCheckFlag):
            pass
        else:
            self.main_menu()
        checkNameFlag=self.checkName(name)
        if(checkNameFlag):
            pass
        else:
            self.main_menu()
        pwd = int(input("\n Please input password to register: "))
        pwd1 = int(input("\n Please input password again to check: "))
        flag = None
        if pwd==pwd1:
              self.creationUser(name,pwd,email)
        else:
              print("Try again!!Passwords are not the same!!")
              self.register()

    def transferMoney(self):
        transferFlag=None
        senderName = input("\n Please input sender surname: ")
        senderId=self.checkingLoginId(senderName)
        senderMoney=self.users_list[senderId]["balance"]
        amount = float(input("\n Please input the amount to be transferred: "))
        receiverName = input("\n Please input receiver surname: ")
        receiverId = self.checkingLoginId(receiverName)
        receiverMoney = self.users_list[receiverId]["balance"]
        sMoney = senderMoney - amount
        rMoney = receiverMoney + amount
        self.users_list[senderId]["balance"]=sMoney
        self.users_list[receiverId]["balance"]=rMoney
        print(f'Transaction completed. Current Balance of sender: ₹{sMoney}', senderName)
        print(f'Transaction completed. Current Balance of receiver: ₹{rMoney}', receiverName)
        transferFlag=True
        return  transferFlag

    def deposit(self):
        amount = int(input('Enter the deposit amount: '))
        id = self.checkingLoginId(self.name)
        fMoney = self.users_list[id]["balance"]
        fMoney+=amount
        self.users_list[id]["balance"] = fMoney
        print(f'Deposit Transaction completed. Current Balance: ₹{fMoney}', self.name)

    def withdraw(self):
        amount = int(input('Enter the withdraw amount: '))
        id = self.checkingLoginId(self.name)
        fMoney = self.users_list[id]["balance"]
        fMoney -= amount
        if (fMoney>500):
            self.users_list[id]["balance"] = fMoney
            print(f'Withdraw Transaction completed. Current Balance: ₹{fMoney}', self.name)
        else:
            print("Insufficient amount!!!")

    def updateName(self):
        nName = input("Please enter your new name")
        id = self.checkingLoginId(self.name)
        self.users_list[id].update({"username": nName})
        print("Success in changing name{} to {} ".format(self.name, nName))
        print(self.users_list)

    def updatePwd(self):
        nPwd = input("Please enter your new password")
        id = self.checkingLoginId(self.name)
        self.users_list[id].update({"userPwd": nPwd})
        print("Success in changing name{} to {} ".format(self.name, nPwd))
        print(self.users_list)

    # def delCustomer(self):
    #     name = input("Please enter your username that you wanna delete")
    #     id = self.checkingLoginId(self.name)
    #     del self.users_list[id]
    #     print("Success in deleting customer")
    #     print(self.users_list)

    def basic_details(self):
        id = self.checkingLoginId(self.name)
        fMoney = self.users_list[id]["balance"]
        print(f'User: {self.name}\t Balance: ₹{fMoney}')

    def print_all_accounts_details(self):
        i = 0
        for c in self.users_list:
            i += 1
            print('\n %d. ' % i, end=' ')
            self.basic_details()
            print("------------------------")

if __name__=="__main__":
    Bank=BankSystem()
    while True:
        Bank.run_main_options(Bank)

