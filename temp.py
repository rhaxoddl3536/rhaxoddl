"""

x = int(input("줄을 입력하세요"))
for i in range(1,x+1):
    print("*"*(x+1-i))
"""
"""
for i in range(100):
    a = i % 10
    if a % 3 == 0 and a != 0:
        print("*")
    else:
        print(i)
"""
"""
for i in range(100):
    a = i // 10
    b = i % 10

    a_c = a % 3 == 0 and a != 0
    b_c = b % 3 == 0 and b != 0
    if a_c and b_c:
    elif a_c:
        print("*")
    elif b_c:
        print("*")
    else:
        print(i)
"""
"""
for i in range(10):
    if i == 5:
        break #continue
    print(i)
 """
"""
print("{} * {} = {}".format(2,4,6))
"""
"""
for i in range(1, 10):
    for j in range(1, 10):
        print("{} * {} = {}".format(i,j,i*j))
"""
a = int(input())
flag = 0 # 0 is prime, 1 is not prime
for i in range(2,a):
    if a % i == 0:
        flag = 1
        break

if flag == 0:
    print("prime")
else:
    print("not prime")
