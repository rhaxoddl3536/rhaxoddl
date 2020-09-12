# 숫자 두 개 입력 받아서 서로소인지 안닌지 판별하는 함수 만들기

"""
#내가 해본 것
def E(a,b):
    while b:
        r= max(a,b) % min(a,b)
        a= min(a,b)
        b= r
    return a

c= input("두 정수 입력")
gcd = E(int(c[0]),int(c[1]))
if gcd == 1:
    print(c[0],c[1],"서로소")
else:
    print(c[0],c[1],"최대공약수")
"""
"""
#선생님이 하신 것
def gcd2(x, y):
    for i in range(1, x+1):
        if x % i == 0 and y % i ==0:
            num = i
    if num == 1:
        print("서로소")
    else:
        print("최대공약수는 {}".format(num))
        print("서로소가 아니다.")

x = int(input("숫자x입력:"))
y = int(input("숫자y입력:"))
gcd2(x, y)
"""

# 주민번호를 입력받아서 나이와 성별을 출력하기
"""
#내가 해본 것
def str():
    while len("is not 14"):
        print('14자리가 아닙니다. 다시 입력해주세요.')
        rrn = input('주민등록번호 14자리를 입력하세요 : ')
        if len(14) :
            break

    #앞 2자리 이용하여 나이 계산
    if int(rrn[:2]) < 21 and int(rrn[6]) in (3, 4) :
        biryear = 2000 + int(rrn[:2])
    else:
        biryear = 1900 + int(rrn[:2])
    #월
    birmonth = int(rrn[2:4])
    #일
    birday = int(rrn[4:6])
    #성별
    if int(rrn[6]) == 1 or int(rrn[6]) == 3 :
        gen = 'male'
    else :
        gen = 'female'
    return [CurYear-biryear, biryear, birmonth, birday, gen]
"""
"""
#선생님이 하신 것
def people(a):
    if(len(a)!=14):
        print("잘못 입력하셨습니다.")
        exit()
        a="941021-1111111"#=>a[0]~a[13]
    else:
        if a[7] == '1' or a[7] == '3':
            gen = 'M'
        else:
            gen = 'W'
        if a[7] == '1' or a[7] == '2':
            age = 2020-(1900 + 10 * int(a[0]) + int(a[1]))+1
        else:
            age = 2020 - (2000 + 10 * int(a[0]) + int(a[1]))+1
    print("나이는 {}살 성별은 {}입니다.".format(age,gen))
a = input()
people(a)
"""
# 재귀를 사용한 팩토리얼(!)
# -재귀함수:힘수 안에 다시 자기 자신을 호출하는 것(함수의 무한루프)
"""
#내가 해본 것
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(int(input())))
"""
"""
#선생님이 하신 것
def fact1(a):
    tot = 1
    for i in range(1, a+1):
        tot *= i#tot = tot * i
    print("{}! = {}".format(a,tot))
a = int(input())
fact1(a)
def fact2(a):
    if a <= 0:
        return 1
    else:
        return a * fact2(a-1) #재귀함수

a = int(input("숫자를 입력하시오:"))
print("{}! = {}".format(a,fact2(a)))
"""

###클래스 기초###
# -1.클래스 선언
'''
class Test: #클래스명은 첫글자는 대문자로 사용한다.
   str = "클래스 개념 잡기" # str은 Test 클래스의 요소(attribute, field) 또는 Test클래스의 멤버라고도 한다.
     #Test는 붕어빵들과 같다.

test1 = Test() #test1 객체는 Test 클래스에 의해서 만들어진 인스턴스, test1은 Test클래스의 인스턴스
        #test1은 붕어빵과 같다.

print(test1.str)
'''

# -2.클래스의 구성
'''
class 클래스명:
   변수    #클래스에 소속된 변수들을 필드(field)라고 부른다.

   함수    #클래스(객체)내에 어떤 기능을 갖을 수 있도록 하는 함수
            # 이러한 함수들을 클래스의 메소드(method)라고 한다.

결론적으로 클래스는 필드와 메소드로 구성된다.
변수나 함수와는 다르게 구별지어서 부르는 것은 클래스나 객체에
소속되어 있는 대상이라는 것을 나타내기 위함이다.

필드와 메소드들을 통틀어 클래스의 속성(attribute) 이라고 부른다.

클래스내의 메소드와 일반 함수와의 차이점은 바로 'self'이다.
메소드의 경우 매개 변수의 목록에 항상 추가로 한개의 변수(self)를 맨 앞에 추가 해야 한다.

메소드를 호출 할 때, 이 변수에는 직접 우리가 값을 넘겨 주지 않는다.
파이썬이 자동으로 self에 값을 할당한다.

self는 c++ 에서의  this 포인터와 같은 것, java나 c#에서는 this 참조 같다.
'''
'''
class Person:
   def say(self):
      print("안녕, 친구!!!")

p1 = Person()

p1.say() #self에 대입값을 전달하지 않았음에도 불구하고 에러가 없다. 즉, 파이썬에서 자동으로 전달을 한다는 의미

class Person:
   pass

p2 = Person() #객체화 한다. 즉, 메모리에 객체를 생성한다. 인스턴스화
print(p2)
'''
'''
init 매소드 : 객체가 생성될 때 여러가지 초기화작업을 할 때
            유용하게 사용할 수 있다. 매소드명은 '__init__'이다.
파이썬의 클래스는 여러가지 특별한 메소드가 존재한다.
그중에서 init 메소드는 클래스가 인스턴스화(객체화) 될 때 호출된다.
'''
# __init__:클래스 안에서만 만들 수 있음

'''
class Person:
   def __inint__(self, name):
      self.name = name
   def say(self):
      print("내이름은",self.name)


p1 = Person('홍길동')

p1.say()
'''

# 생성자(Constructor), 소멸자(Destructor)

'''
from time import time, ctime, sleep

class Life:
   def __init__(self):  #생성자
      self.birth = ctime(time())  #현재 시간에 대한 문자열을 얻는다.
      print('생성시간', self.birth)  #현재 시간 출력

   def __del__(self):  #소멸자
      print('소멸시간', ctime())  #소멸 시간 출력

def test():
   mylife = Life()
   print('Sleeping for 3 sec')
   sleep(3) #3초간 sleep(block) 상태로감.

test()
'''
'''
붕어빵을 객체라고 생각하자

구조
메소드 == 함수, 변수

클래스의 특징
상속, 부모 클래스이 함수를 사용할 수 있다.
'''

# 상속: 자식클래스에만 있는 것을 부모클래스는쓸 수 없음
# 부모클래스에 있는 것-자식에게 상속(몇개를 상속하던 상관x)

'''
<아래 예시는 약간 잘못된 코드임>
class A:
   a = 10
   def say(self):
      print("hi im a")

class B(A):
   def f(self):
      pass

b = B()
b.say()
a = A()
a.f()

pass 는 아무것도 실행 할 것이 없다는 것을 의미한다.
'''

# 정적 메소드
'''
@staticmethod 는 클래스에 의해 정의되는 네임스페이스에 들어 있는 보통 함수
class Foo:
   @staticmethod
   def add(x,y):
      return x + y

#-전역 변수 사용한다.
print(Foo.add(3,6))

import, from

'''

# 클래스 변수와 객체변수의 예
'''
class Man:
   # 클래스 변수
   cnt = 0

   def __init__(self, name):  # __init__메소드를 생성자라고도 한다.
      """ 데이터 초기화 하기 """
      self.name = name  # self.name에서 name은 객체변수를 의미한다.
      print("({}이(가) 만들어지는 중.....)".format(self.name))

      Man.cnt += 1  # 클래수 변수 접근하기 : 클래스명.클래스변수명

   def die(self):
      """Man 객체가 죽었을 때"""
      print("{} 는 죽었습니다!!!".format(self.name))

      Man.cnt -= 1

      if Man.cnt == 0:
         print("{} 는 최후의 생존자 였다".format(self.name))
      else:
         print("아직 {:d}명의 생존자가 남아있다".format(Man.cnt))

   def say(self):
      print("생성완료!!!!   안녕하세요!!! 내이름은 {} 입니다".format(self.name))

   @classmethod  # 장식자(decorator) : how_many = classmethod(how_many)의 다른 표현
   def how_many(how):
      """ 현재의 객체 수량을 체크한다"""
      print("현재 {} 명이 남았습니다".format(Man.cnt))


# how_many = classmethod(how_many)


gameActor1 = Man("맨1")
gameActor1.say()

gameActor2 = Man("맨2")
gameActor2.say()

gameActor3 = Man("맨3")

print("------------------------------")
gameActor2.die()
'''


