import sys
from string import punctuation, whitespace
from datetime import datetime

class MiniBank:
    def __init__(self):
        self.main_userInfo: dict = {}
        self.now = datetime.now()
        self.current_time = self.now.strftime("%H:%M:%S")

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
        if option == 1:
            self.login()
        elif option == 2:
            self.register()
            print("Registration successful at {}".format(self.current_time))
        else:
            print("~~~~~~BYE BYE NOW~~~~~~")
            sys.exit()

    def user_menu(self,loginId):
        # print the options you have
        print(" ")
        print(
            "Welcome User %s : Avilable options are:" % (self.main_userInfo[loginId]["username"]))
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
        if option == 1:
            print("This is from Transfer route")
            self.transferMoney(loginId)
        elif option == 2:
            print("This is from Deposit route")
            self.deposit(loginId)
        elif option == 3:
            print("This is from Withdraw route")
            self.withdraw(loginId)
        elif option == 4:
            print("This is from Update customer's Name route")
            self.updateName(loginId)
            self.unpackingToString()
        elif option == 5:
            print("This is from Update customer's Password route")
            self.updatePwd(loginId)
        elif option == 6:
            print("This is from Update customer's details route")
            self.print_all_accounts_details()
        else:
            self.main_menu()

    def is_email_valid(self,email):
        valid_chars = {'-', '_', '.'}
        invalid_chars = set(punctuation + whitespace) - valid_chars

        stripped_email = email.strip()

        # email must have @
        if "@" not in stripped_email:
            return False

        # there must be one @
        if stripped_email.count("@") != 1:
            return False

        # split the email into local and domain part
        local, domain = stripped_email.split("@")

        for char in invalid_chars:
            if (
                    char in local
                    and (not local.startswith('"')
                         or not local.endswith('"'))):
                return False

        if "." in local:
            try:
                dot_position_in_local = local.index(".")

                if local[dot_position_in_local + 1] == ".":
                    return False
            except:
                return False

        # local.startswith('.') and local.endswith('.') == False
        if local.startswith(".") or local.endswith("."):
            return False

        # domain, - can't be first or last char
        if domain.startswith("-") or domain.endswith("-"):
            return False

        # domain, . cant't be first or last char
        if domain.startswith(".") or domain.endswith("."):
            return False

        # dots in email must not be sequential
        dot_position_in_domain = domain.index(".")

        if "." in domain and (domain[dot_position_in_domain] == domain[dot_position_in_domain + 1]):
            return False

        return True

    def checkingASCIIforName(self, word):
        bigWord = ('A' <= word <= 'Z')
        smallWord = ('a' <= word <= 'z')
        checkFlag = None
        if bigWord or smallWord:
            print("It is an alphabet")
            checkFlag = True
        else:
            print("It is not an alphabet")
            checkFlag = False
        return checkFlag

    def checkingASCIIforInt(self, word):
        intWord = (49 <= word <= 65)
        checkFlag = None
        if intWord:
            print("It is an int")
            checkFlag = True
        else:
            print("It is not an int")
            checkFlag = False
        return checkFlag


    def checkingUserCount(self):
        """This method returns usercount"""
        count = len(self.main_userInfo)
        return count + 1

    def user_exit(self, emailAddress):
        """This method checks user exist or not"""
        user_info_length: int = len(self.main_userInfo)
        if user_info_length == 0:
            return True
        else:
            for i in range(1, user_info_length + 1):
                if self.main_userInfo[i]["username"] == emailAddress:
                    return False
        return True

    def checkLength(self,name):
        if len(str(name)) > 1 and len(str(name)) < 20:
            return True
        return False

    def register(self):
        try:
            print("\n\n_______This is From Registration Route___________\n")
            emailAddress: str = input("Please enter email to register:")

            checkNameFlag = self.is_email_valid(emailAddress)
            checkNameLength =self.checkLength(emailAddress)
            if checkNameFlag and checkNameLength:
                print("Valid name")
            else:
                print("Invalid name")
                self.main_menu()

            password: str = input("Pls enter password to register:")
            password2: str = input("Pls enter password again to confirm:")
            if password == password2:

                # checking email address
                flag: bool = self.user_exit(emailAddress)
                if flag:
                    id: int = self.checkingUserCount()
                    amount:str = input("Please enter your amount:")
                    try:
                        self.dataWriting(emailAddress, password, amount)
                        print("~~~~~~Registration Success~~~~~~~")
                        self.dataReading()
                    except Exception as err:
                        print("\n[#]Error logs from register Method\n")
                        print(err)
                else:
                    print("User Email adress Already exit!")
                    self.login()
        except Exception as err:
            print(err)

    def dataReading(self):
        with open("userInfo.txt", 'r') as fileRead:
            contents = fileRead.readlines()
            for i in contents:
                id = len(self.main_userInfo) + 1
                email, password, amount = i.split(" ")
                dataForm = {id: {"username": email, "password": password, "amount": amount}}
                print("\n[+]Loaded Data  to userInfoDict ID:\n", id)
                self.main_userInfo.update(dataForm)
            fileRead.close()
        return self.main_userInfo

    def dataWriting(self, email, password, amount):
        try:
            with open("userInfo.txt", 'a') as fileWrite:
                data = email + " " + password + " " + amount + "\n"
                fileWrite.write(data)
                print("\n[+]Data Inserted Successfully to File!\n")
                fileWrite.close()
        except Exception as err:
            print("\n [#] Error Logs From FileWriting\n")
            print(err)

    def login_checking(self, l_username, l_pwd):
        self.dataReading()
        userInfo_length: int = len(self.main_userInfo)
        print("\n\nfrom login checking function:", userInfo_length)
        for i in range(1, userInfo_length + 1):
            if self.main_userInfo[i]["username"] == l_username and self.main_userInfo[i]["password"] == l_pwd:
                print(f"{l_username} logged in")
                return i
        return False

    def checkingLoginInfo(self, name, pwd):
        flag: bool = self.login_checking(name, pwd)
        print("User Id", flag)
        if (flag):
            print("This user exists in usersList,You can login")
            return flag
        else:
            print("This user does not exist in usersList,Please register first")
            return flag

    def login(self):
        print("********This is From Login*********\n")
        l_username:str=input("\nPls enter email address to Login:")
        l_password:str=input("\nPls enter password to Login:")
        loginId =self.checkingLoginInfo(l_username,l_password)
        if loginId:
            print("\n\n\n ___Login Successful___\n")
            print("~~~~~Welcome from login Page~~~~:  {0} ".format(self.main_userInfo[loginId]["username"]))
            self.user_menu(loginId)
        else:
            print("\n\n\n~~~Login Fail~~~\n\n\n")
            self.main_menu()

    def returnId(self,name):
        count = len(self.main_userInfo)
        for i in range(1,count+1):
            if self.main_userInfo[i]["username"] == name:
                return i
        return 0

    def transferMoney(self,loginId):
        transferFlag=None
        no=self.checkingUserCount()-1
        if(no==1):
            print(f'Transaction cannot do,we only have user 1')
            # self.run_user_options()
        else:
            self.dataReading()
            senderId: int = loginId
            senderMoney: int = self.main_userInfo[senderId]["amount"]
            sFMoney = int(senderMoney)
            senderName = self.main_userInfo[senderId]["username"]
            receiverName = input("\n Please input receiver surname: ")
            receiverId: int = self.returnId(receiverName)
            print("\n\nWE get to Transer id:", receiverId)
            print("myId", loginId)
            amount: int = int(input(
                "\n Please input the amount to be transferred to {}: ".format(self.main_userInfo[receiverId]["username"])))
            receiverMoney: int = self.main_userInfo[receiverId]["amount"]
            rFMoney = int(receiverMoney)
            print("Testing rFMoney ",rFMoney,type(rFMoney))
            sMoney = sFMoney - amount
            print("Testing sMoney ", sMoney, type(sMoney))
            rMoney = rFMoney + amount
            print("Testing rMoney ", rMoney, type(rMoney))
            self.main_userInfo[senderId]["amount"] = sMoney
            self.main_userInfo[receiverId]["amount"] = rMoney
            print(f'Transaction completed. Current Balance of sender: ₹{sMoney}', senderName)
            print(f'Transaction completed. Current Balance of receiver: ₹{rMoney}', receiverName)
            transferFlag = True
            return transferFlag

    def deposit(self,loginId):
        self.dataReading()
        print("Testing",self.main_userInfo[loginId]["amount"])
        amount:int = int(input('Enter the deposit amount: '))
        print("Testing amount", amount, type(amount))
        fMoney:int = self.main_userInfo[loginId]["amount"]
        print("Testing fMoney",fMoney,type(fMoney))
        iFmoney = int(fMoney)
        print("Testing iFmoney", iFmoney, type(iFmoney))
        iFmoney+=amount
        self.main_userInfo[loginId]["amount"] = iFmoney
        print(f'Deposit Transaction completed. Current Balance: ₹{iFmoney}',   self.main_userInfo[loginId]["username"])

    def withdraw(self,loginId):
        self.dataReading()
        amount:int = int(input('Enter the withdraw amount: '))
        id:int = loginId
        fMoney:int = self.main_userInfo[id]["amount"]
        iFmoney = int(fMoney)
        iFmoney -= amount
        if (iFmoney>500):
            self.main_userInfo[id]["amount"] = iFmoney
            print(f'Withdraw Transaction completed. Current Balance: ₹{iFmoney}', self.main_userInfo[id]["username"])
        else:
            print("Insufficient amount!!!")

    def unpackingToString(self):
        length = len(self.main_userInfo) + 1
        for i in range(1, length):
            print(f'{i}: items')
            email = self.main_userInfo[i]["username"]
            password = self.main_userInfo[i]["password"]
            amount = self.main_userInfo[i]["amount"]
            print(email, password, amount)
            toWriteUpdateDataToFile = email + " " + password + " " + amount

            if i == 1:
                with open("userInfo.txt", 'w') as fileUnpack:
                    fileUnpack.write(toWriteUpdateDataToFile)
                fileUnpack.close()
            else:
                with open("userInfo.txt", 'a') as fileUnpackAppend:
                    fileUnpackAppend.write(toWriteUpdateDataToFile)
                fileUnpackAppend.close()

    def updateName(self,loginId):
        self.dataReading()
        name = self.main_userInfo[loginId]["username"]
        nName = input("Please enter your new name")
        self.main_userInfo[loginId]["username"] = nName
        print("Success in changing name{} to {} ".format(name, nName))

    def updatePwd(self,loginId):
        self.dataReading()
        name = self.main_userInfo[loginId]["username"]
        nPwd = input("Please enter your new password")
        self.main_userInfo[loginId]["password"] = nPwd
        print("Success in changing {}'s password to {} ".format(name, nPwd))

    def basic_details(self,i):
        fMoney = self.main_userInfo[i]["amount"]
        fFMoney = int(fMoney)
        name = self.main_userInfo[i]["username"]
        print(f'User: {name}\t Balance: ₹{fFMoney}')

    def print_all_accounts_details(self):
        i = 0
        for c in self.main_userInfo:
            i += 1
            print('\n %d. ' % i, end=' ')
            self.basic_details(i)
            print("------------------------")

if __name__ == "__main__":
    miniBank: MiniBank = MiniBank()
    while True:
        miniBank.main_menu()
