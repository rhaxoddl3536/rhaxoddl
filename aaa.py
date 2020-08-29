"""

반씩 나눠서 몇번만에 찾은지

import random

a = int(input())

start = 1
end = 100
half = 50

b = 1
for i in range(1, 100):
    if a == half:
        break
    elif a > half:
        start = half
    else:
        end = half
    b = b+1

    half = (start + end) // 2
print(b)
"""
"""
b = (input())
c = []
for i in range (len(b)):
    c.append(b[i])
    print(c)
"""
"""
앞문자 뒷문자 똑같은지 확인하기


(내가 시도 하려고 했던거)
a = input()
for i in range(a):
if a[0] == a[]:
    print("yes")
else:
    print("no")
"""
"""

(답)

#version 1

a = input()
reverse = []
not_reverse = []

for i in range(len(a)):
    reverse.append(a[i])
    not_reverse.append(a[len(a) -1 -i])
    
flag = 0
for i in range(len(reverse)):
    
    if reverse[i] != not_reverse[i]:
        flag = 1
        break
if flag == 1:
    print("not same")
else:
    print("same")
"""
"""
#version 2

flag = 0
for i in range(len(a)):
    if a[i] != a[len(a) -1 -i]:
        flag = 1
        break
if flag == 1:
        print("not same")
else:
     print("same")
"""
"""
#튜플
a =(1, 2, 3)
한번 값을 할당하면 바꿀 수 없다. 처음부터 값을 입럭해줘야함.
"""
"""
a = [1, 2, 3], [4, 5, 6]
print(a[0][2])
"""
"""
#Dictionary
#key, value
a = {'kkk':170, 'age':100, 'value':200, 'value':300}

print(a['value'])
key는 하나여야함
"""
"""
#function
#return = 1. 값을 반환, 2.함수 끝냄
#def = function

def add_test(x, y):
    return x + y

print(add_test(1, 3))

"""



