def solution(attack, recovery, hp):
    count = 0
    while(True): # 무한 반복
        count += 1
        hp -= attack
        if hp <= 0:
            break   # 무한 반복을 멈추게 함
        hp += recovery
    return count

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
attack = 30
recovery = 10
hp = 60
ret = solution(attack, recovery, hp)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")