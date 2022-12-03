'''
256 인스턴스 속성에 접근
255에서 생성한 인스턴스의 이름, 나이, 성별을 출력하세요. 인스턴스 변수에 접근하여 값을 출력하면 됩니다.

이름: 조아름, 나이: 25, 성별: 여자
인스턴스 변수에 접근하여 값을 가져오는 예

>>> areum.age
25
'''

class Human:
    def __init__(self,name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

mimi = Human("mimi",25,"female")
print(mimi.sex)