'''
257 클래스 메소드 - 1
사람 (Human) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 추가하세요.

>>> areum.who()
이름: 조아름, 나이: 25, 성별: 여자
'''

class Human():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print("name: {}, age:{}, sex:{}".format(self.name, self.age, self.sex))

mimi = Human("mimi", 25, "female")
mimi.who()