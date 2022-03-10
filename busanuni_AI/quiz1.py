

# 퀴즈 : 로또번호 출력하기
# 로또 숫자는 1~36 숫자중에서 6개가 출력되도록 한다.
# 로또 숫자는 중복값이 없어야 한다.
# 함수를 이용하여라.
# 출력 예시
# print(lotto()) 함수 호출시
# [10, 25, 1, 22, 12, 8]
import random

def lotto():
    l = []
    for i in range(6):
        if random.randint(1, 37) != random.randint(1, 37):
            ran = random.randint(1, 37)
            l.append(ran)
    return l

print(lotto())

# while() + in/not in 연산자 + random.randint()
def lotto():
    numList = []
    while(len(numList)<6):
        x=random.randint(1,36)
        # 리스트에 중복값이 없다면 데이타를 리스트에 추가
        if x not in numList:
            numList.append(x)
    return numList
print('='*50)
print(lotto())

# range() + random.shuffle()
def lotto2():
    # 1~36 까지의 리스트 생성 [1,2,...36]
    lotto = list(range(1,37))
    random.shuffle(lotto)
    return lotto[:6]