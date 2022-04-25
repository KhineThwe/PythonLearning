class Test:
    def __init__(self):
        self.userInfoDict={}

    def fileReading(self):
        with open("userInfo.txt",'r') as fileRead:
            contents =fileRead.readlines()
            for i in contents:
                name , pw , amount =i.split(" ")
                id=len(self.userInfoDict)+1
                dataForm = {id:{"username":name,"password":pw,"amount":amount}}
                self.userInfoDict.update(dataForm)
            fileRead.close()

    def fileWriting(self,name,pw,amount):
        with open("userInfo.txt",'a') as fileWriting:
            data=name+" "+pw+" "+amount+"\n"
            fileWriting.write(data)
            fileWriting.close()

    def updatingName(self,id,name):
        self.fileReading()
        self.userInfoDict[id]["username"]=name

    def unpackingToString(self):
        self.fileReading()
        for i in range(1,len(self.userInfoDict)+1):
            name=self.userInfoDict[i]["username"]
            password=self.userInfoDict[i]["password"]
            amount=self.userInfoDict[i]["amount"]
            print(name,password,amount)
            toWriteUpdateDataToFile=name+" "+password+" "+amount+"\n"

            if i==1:
                with open("userInfo.txt", 'w') as fileUnpack:
                    fileUnpack.write(toWriteUpdateDataToFile)
                fileUnpack.close()
            else:
                with open("userInfo.txt", 'a') as fileUnpackAppend:
                    fileUnpackAppend.write(toWriteUpdateDataToFile)
                fileUnpackAppend.close()


if __name__=="__main__":
    test=Test()
    test.updatingName(1,"Oo")
    test.unpackingToString()
