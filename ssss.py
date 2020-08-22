"""

a= [1, 2, 3, 4]
for i in range(len(a)):
    if i == 1:
        del a[i]
"""
"""
a = [1, 2, 3, 4, 5, 6, 7]

print(a[2:5])
"""
"""
a = int(input())
b= []
while a != 1:
     b.append(a%2)
     a = a//2
b.append(1)
print(b)

for i in range(len(b)- 1, -1, -1):
    print(b[i])
"""
import random
a = int(input())

start = 1
end = 100
half = 50

for i in range(1, 100):
    if a == half:
        break
    elif a > half:
        start = half
    else:
        end = half

    half = (start+end)//2









