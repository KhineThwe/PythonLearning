import sys
import re

#no error
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  # for email checking

def check(email):
    uEmailFlag = None
    if (re.search(regex, email)):
        print("\n Valid Email")
        return True
    else:
        print("\n Invalid Email")
        return False
#no error
class BankSystem:
    users_list:dict = {}

    def __init__(self):
        pass

    def checkingUserNo(self):
        count:int =len(self.users_list)
        return count+1

    # no error
    def creationUser(self,username,password,email):
        listLength:int =self.checkingUserNo()
        moneyAmount:int=int(input("\n Enter your money amount"))
        form={listLength:{"username":username,"userPwd":password,"userEmail":email,"balance":moneyAmount}}
        self.users_list.update(form)
        print("\n User creation Successful!!")
        print("\n All data: ",self.users_list)
    # no error

    # no error but design
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
        option:int = int(input("Choose your option: "))
        return option
    # no error but design

    #no error
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
                 print("\n Thank-You for stopping by the bank!")
                 sys.exit()
        # no error

    #no error
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
    # no error

    #bug have to fix after transaction
    def run_account_options(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Back to main menu")
        print("2) Sign out")
        option = int(input("Choose your option: "))
        loop = 1
        while loop == 1:
            if option == 1:
                self.main_menu()
            elif option == 2:
                print("\n Thank-You for stopping by the bank!")
                sys.exit()

    #for transfer withdraw deposit option
    def run_user_options(self, user_obj,loginId):
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
        listLen:int = len(self.users_list)
        print(self.users_list)
        print("User Length", listLen)
        for i in range(1,listLen+1):
            print(i)
            print(self.users_list[i]["userPwd"],pwd)
            if (self.users_list[i]["username"] == name and self.users_list[i]["userPwd"] == pwd):
                print(f"{name} logged in")
                return i
        return 0

    def checkingLoginInfo(self, name, pwd):
        flag: bool = self.checkinguserNameAndPwd(name, pwd)
        print("User Id", flag)
        if (flag):
            print("This user exists in usersList,You can login")
            return flag
        else:
            print("This user does not exist in usersList,Please register first")
            return flag

    def user_login(self,user_obj):
        name = input("\n Please input username to login: ")
        pwd = int(input("\n Please input password to login: "))
        flag:bool = self.checkingLoginInfo(name,pwd)
        if(flag):
            loginId=self.checkingLoginId(name)
            print("Login Successful!!!")
            self.run_user_options(user_obj,loginId)
        else:
            print("Login Fail!!!")
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

    #no error
    def register(self):
        # while True:
            name = input("\n Please input username to register: ")
            checkNameFlag = self.checkName(name)
            if (checkNameFlag):
                pass
            else:
                print("\n Bez of name error,you have to register again!!!")
                self.register()  # bug

            email = input("\n Please input email to register")
            emailCheckFlag = check(email)

            if (emailCheckFlag):
                pass
            else:
                print("\n Bez of wrong format email error,you have to register again!!!")
                self.register()  # bug

            pwd = int(input("\n Please input password to register: "))
            pwd1 = int(input("\n Please input password again to check: "))
            flag = None
            if pwd == pwd1:
                self.creationUser(name, pwd, email)
            else:
                print("\n Try again!!Passwords are not the same!!")
                self.register()
    # no error

    def checkinguserName(self, name):
        listLen: int = len(self.users_list)
        print("User Length", listLen)
        for i in range(1, listLen + 1):
            if (self.users_list[i]["username"] == name):
                return i
        return 0

    def checkingLoginId(self, name):
        flag: bool = self.checkinguserName(name)
        print("User Id", flag)
        if (flag):
            print(flag)
            return flag
        else:
            return flag

    #2 after login error have to fix it
    def transferMoney(self):
        transferFlag=None
        no=self.checkingUserNo()-1
        if(no==1):
            print(f'Transaction cannot do,we only have user 1')
            self.run_user_options(user_obj,loginId)
        else:
            senderName = input("\n Please input sender surname: ")
            senderId: int = self.checkingLoginId(senderName)
            senderMoney: int = self.users_list[senderId]["balance"]
            receiverName = input("\n Please input receiver surname: ")
            receiverId: int = self.checkingLoginId(receiverName)
            amount: int = int(input(
                "\n Please input the amount to be transferred to {}: ".format(self.users_list[receiverId]["username"])))
            receiverMoney: int = self.users_list[receiverId]["balance"]
            sMoney = senderMoney - amount
            rMoney = receiverMoney + amount
            self.users_list[senderId]["balance"] = sMoney
            self.users_list[receiverId]["balance"] = rMoney
            print(f'Transaction completed. Current Balance of sender: ₹{sMoney}', senderName)
            print(f'Transaction completed. Current Balance of receiver: ₹{rMoney}', receiverName)
            transferFlag = True
            return transferFlag


    # 3 after login error have to fix it
    def deposit(self):
        amount:int = int(input('Enter the deposit amount: '))
        id:int = self.checkingLoginId(self.name)
        fMoney:int = self.users_list[id]["balance"]
        fMoney+=amount
        self.users_list[id]["balance"] = fMoney
        print(f'Deposit Transaction completed. Current Balance: ₹{fMoney}', self.name)

    # 4 after login error have to fix it
    def withdraw(self):
        amount:int = int(input('Enter the withdraw amount: '))
        id:int = self.checkingLoginId(self.name)
        fMoney:int = self.users_list[id]["balance"]
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

    #bug
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
    Bank:BankSystem =BankSystem()
    while True:
        Bank.run_main_options(Bank)

