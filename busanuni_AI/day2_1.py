# 자료형의 종류
# 기본 자료형 - 문자열, 정수, 실수, 불린형 -> 집 한 채
# 집합형 자료형=콜렉션 : 여러개의 구성요소로 조직화 -> 아파트 안에 집 여러 채채#
# : 리스트 [], 튜플 (), 딕셔너리 { }, 집합{ }
# CRUD : Create Read Update Delete 데이터를 뽑아서 보고 업데이트, 삭제 하는 것

# 리스트 []
# 다른 데이터형 가능- 다른 데이터랑 섞여도 괜찮아! 넘파이 구조- 데이터형 똑같음 (숫자면 숫자, 문자면 문자)
# 순차적으로 생성
# 빈 리스트, 초기값 설정 방식

# 중첩 리스트 - 리스트 안에 리스트 있다
# 초기값 설정 방식을 이용한 리스트 정의
# 리스트변수 = [값1, 값2...]

# 2행 2열 리스트 선언
list6 = [ [10, 20], [100, 200] ]
print(list6, len(list6)) #[[10, 20], [100, 200]] 2-> 큰 덩어리로 인식
# 리스트 이름[][] 인덱싱
print(list6[0], list6[0][0]) # [10, 20] 10 0번의 0
print(list6[1], list6[1][0]) # [10, 20] 10 1번의 0

# 길이가 다른 중첩 리스트
list7 = ['AI', 2022, [100, 200], [True, False]]
print(list7, len(list7))
print(list7[0]) # AI
print(list7[2], list7[2][-1]) # [100, 200] 200
print(list7[3], list7[-1][-1]) # [True, False] False

# 중첩 리스트 생성2
# 1차원 리스트 정의 후 1차원 리스트를 다시 리스트로 구성

'''
kor: 합계 =?, 평균 =?
math: 합계 =?, 평균 =?
english: 합계 =?, 평균 =?
'''
# 1차원 리스트 정의
kor = [ 55, 66, 34, 60]
math = [ 78, 90, 45, 88]
eng = [ 56, 98, 78, 90]

# 2차원 리스트 정의
grade = [kor, math, eng]
print(grade) # [[55, 66, 34, 60], [78, 90, 45, 88], [56, 98, 78, 90]]

kor_sum = grade[0][0] + grade[0][1] + grade[0][2] + grade[0][3]
kor_avg = kor_sum/4
print(f'kor : 합계 = {kor_sum}, 평균 = {kor_avg: .2f}') # kor : 합계 = 215, 평균 =  53.75

# 퀴즈 1
'''
아래와 같이 리스트를 정의하고 다음과 같이 출력한다. 

foods = ['사과','망고','치즈케이크','주스']

우리집 냉장고에는?  ['사과', '망고', '치즈케이크', '주스']
동생이 사과를 먹었다 
우리집 냉장고에는?  ['망고', '치즈케이크', '주스']
이모가 수박을 사오셨다. 
우리집 냉장고에는?  ['망고', '치즈케이크', '주스', '수박']
동생 친구가 치즈케이크,수박을 먹었다. 
우리집 냉장고에는?  ['망고', '주스']
'''
foods = ['사과','망고','치즈케이크','주스']
print("우리집 냉장고에는?", foods)
print("동생이", foods[0], "를 먹었다.")
print("우리집 냉장고에는?", foods[1:5])
print("이모가 수박을 사오셨다.")
foods.append('수박')
print(foods[1:6])
print(f'동생 친구가, {foods.pop(1)},{foods.pop()} 을 먹었다.')
print(f'우리집 냉장고에는? {foods}')

# 퀴즈2
'''
데이터를 입력받은 후 리스트에 추가하고 출력하여라 
( input() 이용 )

좋아하는 음식은? 초밥
최근 본 영화는? 알라딘
좋아하는 가수는? BTS
좋아하는 숫자? 10
최근 여행지? 부산


당신에 관한 리스트 : ['초밥', '알라딘', 'BTS', 10, '부산' ]
'''
yourList =[]
yourList.append(input('좋아하는 음식은?...'))
yourList.append(input('최근에 본 영화는?...'))
yourList.append(input('좋아하는 가수는?...'))
yourList.append(input('좋아하는 숫자?...'))
yourList.append(input('최근 여행지?...'))

a = input()
print('좋아하는 음식은?', a[2:4])
print('최근 본 영화는?', a[8:11])
print('좋아하는 가수는?', a[15:18])
print('좋아하는 숫자', a[21:23])
print('최근 여행지', a[26:28])

# 빈 리스트를 이용한 리스트 정의
# 리스트변수 = []

list1 = []
list2 = [10, 20, 30]
list3 = [100, 2.13, 'python', True] # 정수, 실수, 문자열, 논리형 으로 구성된 리스트

# type(), 데이터 형 확인, len() 길이 확인
print(list1, type(list1), len(list1))
print(list2, type(list2), len(list2))
print(list2, type(list3), len(list3))

# 서로 다른 데이터형으로 리스트 정의

# 리스트 인덱싱
# 리스트이름[숫자] : 0부터 시작, 숫자값이 -1 마지막 요소 표시

print(f'{ list3 } 첫번째 요소 값은? { list3[0]}')
print(f'{ list3 } 첫번째 요소 값은? { list3[3]}')
print(f'{ list3 } 첫번째 요소 값은? { list3[-1]}')

# 리스트 슬라이싱
# 리스트이름[start:end:step]
# 리스트이름[start:end]
# 리스트이름[start:]
# 리스트이름[:end]
# 리스트이름[::step]
# 리스트이름[:] = 리스트이름[::] = 전체리스트

list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list4, len(list4))
print(list4[1:3]) # [2, 3]
print(list4[-5:-2]) # [5, 6, 7]
print(list4[::2]) # [혹수 값]
print(list4[1::2]) # [1자리 부터 2칸 씩 건너 뛰어서 찍기]
print(list4[-1::2]) # [9]
print(list4[::-1]) # [뒤에서부터 역순으로]


# 리스트 값 변경하기
# 리스트변수[인덱스] = 값

# 리스트 연산
# 리스트1 + 리스트2 : 같이 표시
# 리스트이름*숫자 : 반복

# 리스트 함수
# 리스트변수.함수명(옵션)
# 정의된 리스트에 새로운 값을 추가
# 리스트변수.append(값) : 마지막에 아이템이 추가
# 리스트변수.insert(삽입위치, 값) : 삽입위치에 아이템이 추가
print('=' * 50)
list1 = []
print(list1)
list1.append('가')
print(list1)
list1.append('나')
print(list1)
list1.insert(0, 'python') # 0 인덱스에 값 추가
print(list1) # ['python', '가', '나']
list1.insert(2, 77)
print(list1) # ['python', '가', '77', '나']

# 기존 값 변경
# 리스트명[인덱스] = 새로운 값
list1[2] = 88
print(list1)

# 리스트 삭제와 관련된 함수와 명령어
# 리스트변수.remove(값) : 값으로 삭제하기
# 리스트변수.pop() : 마지막 요소가 삭제되면서 값이 반환된다.
# 리스트변수.pop(위치값)
# : 위치에 해당하는 요소가 삭제되면서 값이 반환된다.
# 리스트변수.clear() : 리스트안의 값이 모두 삭제. 빈리스트로 된다.
print('='* 50)
list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list4)
list4.remove(5) # 값으로 삭제
list4.pop() # 마지막 위치 삭제
print(list4)
list4.clear()
print(list4)
# del 리스트변수 : 리스트 자체가 삭제된다.

# 메모리에 리스트 없애기

# del 리스트변수[위치] = 리스트변수.pop(위치)
# NameError: name 'numList2' is not defined
# print(f'numList2 = {numList2}')

# 리스트 전체 길이 출력
# len(리스트변수)
# 리스트 데이터형 출력
# type(리스트변수)

# 입력받은 값으로 리스트를 생성하여라

# 리스트 값 정렬하기
# 리스트변수.reverse()
# 리스트변수.sort()
# 주의사항은 리스트변수.sort()의 경우
# 리스트를 이루는 구성요소의 데이터형은 같아야한다
# TypeError 발생

# 리스트변수.count(값)
# 중복값이 몇개인가?

# 리스트변수.index(값)
# 값에 해당하는 요소가 몇번째에 위치하고 있는가?


# 여러개의 요소를 한꺼번에 리스트에 추가 싶다면?
# 리스트변수.extend([값1,값2...])

list5 = [100, 200]
print(list5)
list5.extend([True, False])
print(list5)

# ------------------------------------------------

# 캐스팅
# 문자열 => 리스트
# 문자열변수.split() : 공백을 기준으로 해서 리스트화
# 문자열변수.split(구분문자) : 구분문자를 기준으로 해서 리스트화
# list(문자열변수)
# : 공백도 모두 리스트화. 낱글자가 아이템요소로 변경


# 리스트 => 문자열
# str(리스트이름)
# : [ ], 쉼표(,) 도 포함해서 모두 문자열화
# '구분자'.join(리스트이름)
# : 구분자가 아이템요소 사이에 모두 추가된 후 문자열화

# 중첩 리스트 구조
# 리스트안에 리스트가 있다
# 중첩리스트의 인덱싱은?
# 리스트이름[index1][index2]

# 중첩 리스트 생성1
# 초기값으로 중첩 리스트 생성
# 리스트변수 = [ [값1, 값2...],[값1, 값2...]]

# 중첩 리스트 생성2
# 1차원 리스트 정의 후 1차원 리스트를 다시 리스트로 구성

# 퀴즈 :
'''
아래의 리스트를 이용하여 grade 리스트를 생성하고 합계와 평균을
과목별로 출력한다. 평균은 소숫점 2번째 자리까지 출력한다.

kor = [100, 80, 85]
math = [55, 70, 35]
eng = [80, 80, 100]
python = [90, 70, 88]
------------
result
kor : 합계 = ? , 평균 = ?
math : 합계 = ? , 평균 = ?
eng : 합계 = ? , 평균 = ?
python : 합계 = ? , 평균 = ?
'''