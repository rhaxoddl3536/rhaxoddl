import random
class makeCharacter:

    def __init__(self, id):
        self.name = id
        self.hp = random.randrange(1, 20)
        self.mp = random.randrange(1, 40)
        self.q = random.randrange(1, 5)

    def attack(self):
            return self.q
    def attacked(self, atk):
            self.hp =self.hp -atk
    def fireball(self):
            self.mp =self.mp-10
            return 10



id = input("Enter character name :")
ogar = makeCharacter(id)

id = input("Enter character name :")

mc = makeCharacter(id)
print("befor mc", mc.hp)

mc.attacked(ogar.attack())
print("after mc", mc.hp)



while ogar.hp>0 and mc.hp>0:
    ogar.attacked(mc.attack())
    print("after ogar", ogar.hp)

    mc.attacked(ogar.attack())
    print("after mc", mc.hp)

    if ogar.hp <=0 or mc.hp <=0:
        break

turn = 1
while ogar.mp>0 and mc.mp>0:

    if turn == 1:

        select_skill = int(input("Enter your skill 1)attack 2)fireball "))

        if select_skill ==1:
            ogar.attacked(mc.attack())
            print(ogar.mp)


        elif select_skill ==2:
            ogar.attacked(mc.fireball())
            print(ogar.mp)
        turn =0

    if ogar.mp== 0 or mc.mp ==0:
        break

    else:
        num = random.randrange(1, 3)
        if num == 1:
            mc.attacked(ogar.attack())
        else:
            mc.attacked(ogar.fireball)
        turn = 1
#절대경로
다른 곳에 있는 파일에서-속성-복붙
f =open("복붙")
temp = f.readlines()
print(temp)
#상대경로 ./=내 위치에서부터 시작 , ../=내 바로 상위 폴더부터 시작









