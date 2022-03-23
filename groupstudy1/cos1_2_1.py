'''
#문제1
A 학교에서는 단체 티셔츠를 주문하기 위해 학생별로 원하는 티셔츠 사이즈를 조사했습니다.
선택할 수 있는 티셔츠 사이즈는 작은 순서대로 "XS", "S", "M", "L", "XL", "XXL" 총 6종류가 있습니다.

학생별로 원하는 티셔츠 사이즈를 조사한 결과가 들어있는 리스트 shirt_size가 매개변수로 주어질 때,
사이즈별로 티셔츠가 몇 벌씩 필요한지 가장 작은 사이즈부터 순서대로 리스트에 담아 return 하도록 solution 함수를 완성해주세요.

---
##### 매개변수 설명
학생별로 원하는 사이즈를 조사한 결과가 들어있는 리스트 shirt_size가 solution 함수의 매개변수로 주어집니다.
* shirt_size 의 길이는 1 이상 100 이하입니다.
* shirt_size 에는 치수를 나타내는 문자열 "XS", "S", "M", "L", "XL", "XXL" 이 들어있습니다.

---
##### return 값 설명
티셔츠가 사이즈별로 몇 벌씩 필요한지 가장 작은 사이즈부터 순서대로 리스트에 담아 return 해주세요.
* return 하는 리스트에는 [ "XS" 개수, "S" 개수, "M" 개수, "L" 개수, "XL" 개수, "XXL" 개수] 순서로 들어있어야 합니다.

---
##### 예시

| shirt_size                       | return        |
|----------------------------------|---------------|
| ["XS", "S", "L", "L", "XL", "S"] | [1, 2, 0, 2, 1, 0] |

##### 예시 설명
* "XS"와 "XL"은 각각 한 명씩 신청했습니다.
* "S"와 "L"은 각각 두 명씩 신청했습니다.
* "M"과 "XXL"을 신청한 학생은 없습니다.

따라서 순서대로 [1, 2, 0, 2, 1, 0]을 리스트에 담아 return 하면 됩니다.
'''
#You may use import as below.
import math

def solution(shirt_size):
    shirt_list = [0 for _ in range(6)]

    for i in shirt_size:
        if i == "XS":
            shirt_list[0] += 1
        elif i == "S":
            shirt_list[1] += 1
        elif i == "M":
            shirt_list[2] += 1
        elif i == "L":
            shirt_list[3] += 1
        elif i == "XL":
            shirt_list[4] += 1
        elif i == "XXL":
            shirt_list[5] += 1

    return shirt_list

#The following is code to output testcase.
shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size);

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")