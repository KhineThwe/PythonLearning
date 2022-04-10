name = input("Name")
pwd = int(input("Password"))
idNo=1
users_list = {
     idNo : {"username": name,"userPwd": pwd }
}

size=len(users_list)-1

for i in range(size):

     idNo+=1
     users_list.update({
          idNo: {"username": name, "userPwd": pwd}
     })
print(users_list)
