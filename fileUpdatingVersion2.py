class Test:
    def __init__(self):
        self.userInfoDict={}

    def fileReading(self):
        with open("userInfo.txt",'r') as fileRead:
            contents =fileRead.readlines()

            for i in contents:
                id = len(self.userInfoDict) + 1
                name , pw , amount =i.split(" ")
                dataForm = {id:{"username":name,"password":pw,"amount":amount}}
                self.userInfoDict.update(dataForm)

            fileRead.close()
        return self.userInfoDict


    def fileWriting(self,name,pw,amount):
        with open("userInfo.txt",'a') as fileWriting:
            data=name+" "+pw+" "+amount+"\n"
            fileWriting.write(data)
            fileWriting.close()

    def updatingName(self,id,name):
        self.fileReading()
        self.userInfoDict[id]["username"]=name

    def unpackingToString(self):
        #self.fileReading()
        length=len(self.userInfoDict)+1
        for i in range(1,length):
            print(f'{ i }: items')
            name=self.userInfoDict[i]["username"]
            password=self.userInfoDict[i]["password"]
            amount=self.userInfoDict[i]["amount"]
            print(name,password,amount)
            toWriteUpdateDataToFile=name+" "+password+" "+amount

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
    test.updatingName(1,"khinezarthwe")
    print(test.userInfoDict)
    test.unpackingToString()
    test.updatingName(2,"tokyo")
    test.unpackingToString()
