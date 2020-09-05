"""
def test_hi(b,c):
    a = b + c
    return a
"""
"""
#함수 이용 구구단 - 내가 해본 것 (b부터는 선생님 도움으로)
def test_hi(a):
    for i in range(1,10):
        print("{}*{}={}".format(a, i,a*i))

b = int(input())
test_hi(b)
"""
"""
#선생님이 하신거

def nk_test(a):
    print("a value", a)
    for i in range(1,10):
        print("{}*{}={}".format(a, i,a*i))

b = int(input())
nk_test(b)
"""
"""
#함수이용해서 369만들기 -내가 해본 것
def check369(c):
    num = str(c)
    data = list(num)
    for data in num:
        if"3" in data or "6" in data or "9" in data:
         return True
    return False
for i in range(1,101):
    if check369(i) == True:
        print("*", end= " ")
    else:
        print(i, end= " ")
    if i%20==0:
        print()
"""
#선생님이 하신거
"""
def three_for_six(a):

    for i in range(1, 100):
        one = i % 10
        if one % a == 0:
            print("*")
        else:
            print(i)
"""
"""
#함수 이용해서 각자리 * -내가 해본 것
def three_for_six(a, b):

    for i in range(100):
        one = i % 10
        ten = i // 10

        one_condition = one % b == 0 and one !=0
        ten_condition = ten % a == 0 and ten !=0

        if one_condition and ten_condition:
            print("**")
        elif one_condition:
            print("*")
        else:
            print(i)

a = int(input())
b = int(input())
three_for_six(a, b)
"""
"""
#선생님이 하신거
def test(a, b):
    for i in range(1, 100):

        ten = i // 10 % a ==0
        one = i % 10 % b ==0

        if ten and one:
            print("**")
        elif ten or one:
            print("*")
        else:
            print(i)


a = int(input()) # ten
b = int(input()) # one
test(a, b)
"""
#숫자 두 개 입력 받아서 서로소 구하기(숙제)

