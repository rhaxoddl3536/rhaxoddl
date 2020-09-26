#로그인
'''
f = open("log",'r')
lines = f.readlines()

id = input("id : ")
pw = input("pw : ")
flag=0

for line in lines:
    server_id = line.split(',')[0]
    server_pw = line.split(',')[1].split('\n')[0]
    print(server_id, server_pw)


    if id == server_id and pw == server_pw:
        print("suc")
        flag=1
        break

if flag ==0:
    print("fail")
'''

'''
a= "hihihikbyebye"
b= a.split('k')
type(b)
print(b)
'''
#회원가입
'''
f= open("log",'a')
fr= open("log", 'r')

id= input("id : ")
pw= input("pw : ")

flag=0
lines= fr.readlines()
for line in lines:
    server_id = line.split(',')[0]
    server_pw = line.split(',')[1].split('\n')[0]
    print(server_id, server_pw)

    if id == server_id :
        print("fail")
        flag=1
        break

if flag ==0:
    id = input("id : ")
    pw = input("pw : ")

f.write(id+','+pw+'\n')
'''





