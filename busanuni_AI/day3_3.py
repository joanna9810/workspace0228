# range(start, end , step)
# start~ (end-1)까지 step만큼 차례대로 숫자 생성
# range 객체로 생성되므로
# 실제 출력을 확인하려면 리스트, 튜플, 집합 형태로 자료형 변경

print('=' *50)
print(range(1, 10)) # range(1, 10)
print(list(range(1, 10))) # [1, 2, 3, 4, 5, 6, 7, 8, 9] 9까지 밖에 안 찍힘!
print(tuple(range(1, 10))) # (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1,50,2))) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]

# list( range(start, end , step) )
# : 순차적으로 숫자로 구성된 리스트
# tuple( range(start, end , step) )
# : 순차적으로 숫자로 구성된 튜플
# set( range(start, end , step) )
# : 순차적으로 숫자로 구성된 집합



# 1~20 사이의 짝수 또는 홀수로 구성된 리스트 생성하기
'''
listEven = list(range(2,21,2))
listOdd = list(range(1,21,2))
'''

# for 문과 range
# for 인덱스변수 in range(start,end,step):
#   명령문
# 다른 언어들 => for(초기값; 조건식; 증감치) {}

# 1~10까지 출력하기
for i in range(1,11):
    print(i, end=' ')


# 1~10까지 홀수만 출력하기
print()
print('='*50)
for i in range(1,11,2):
    print(i, end=' ')
# 1~100사이의 합 구하기

# 1~10 모두 곱한 값 구하기
# 1x2X...X10 = ?


# for 문에서 조건문 실행
# 1~25 까지 한줄에  5개씩 출력하기
'''
1 2 3 4 5
6 7 8 9 10
..
21 22 23 24 25
'''

# 1~27 에서 5의 배수만 빼고 출력하기

# 다중 for문과 range()
'''
for i in range(0,3):
    print('-'*30)
    for j in range(0,3):
        print('Hello world')
'''

# 다중 for 문을 이용하여 구구단 출력

# 리스트 for = 리스트 내포
# 리스트 안에 for 문이 내포된 형태
# 결과값으로 구성된 리스트가 생성된다.
# 리스트변수 = [ 결과값 for 명령문 ]

# 1~10까지 숫자로 이루어진 리스트를 만들어라
'''
numList1 = []
for i in range(1,11):
    numList1.append(i)
print('numList1 = ',numList1)

numList2 = [i for i in range(1,11)]
print('numList2 = ', numList2)
'''

# 3단의 결과값으로 리스트를 만들어라

# 3단의 결과값에서 -1 한 값으로 리스트를 만들어라

# 아래와 같은 형태로 리스트를 만들어라
# ['*', '**', '***' .... ,'**********']
'''
numList5 = ['*'*i for i in range(1,11)]
print('numList5 = ', numList5)
for i in range(0, len(numList5)):
    print(numList5[i])
for i in range(0, len(numList5)):
    print(numList5[len(numList5)-1-i])
'''

# 리스트 다중 for
# 리스트안에 이중 for문이 있는 형태
# 구구단의 결과값을 리스트로 추가
'''
numList6 = []
for i in range(2,11):
    for j in range(1,10):
        numList6.append(i*j)
'''
'''
numList7 = [i*j for i in range(2,11) for j in range(1,10)]
print('numList7 = ',numList7)
'''

#-------------------------
#-------------------------

# 자료형의 각 요소 값을 순차적으로 출력
# for 인덱스변수 in 리스트,문자열,튜플:
#   명령문

# 리스트안의 요소를 세로로 출력
myList = ['구로동', '신림동', '서초동', '역삼동']
for item in myList:
    print(item)

print('='* 50)
i = 0
while i<len(myList) :
    print(myList[i])
    i += 1

# 문자열을 세로로 출력하기
print('='*50)
txt = '가나다라마바사아'
count = 1
for c in txt:
    print(f'{count} : {c}')
    count += 1
print('='*50)

# while 문을 이용해서 세로로 출력
i = 0
while i<len(txt) :
    print(f' { i+1 } : { txt[i] } ')
    i += 1

# quiz 리스트에서 60 점이 넘으면 합격을 출력, 전체 리스트의 평균, 합 출력
# for... in + if

math_list = [22, 90, 50, 70, 90]
tot = 0
for score in math_list:
    tot += score
    if score >= 60 :
        print(f' { score }  => 합격 ')
    else:
        print(f' {score}  => 불합격 ')

print( f' 총점 => {tot}  평균 => {(tot/len(math_list)):.2f}' )


# range(start, end , step)
# start~ (end-1)까지 step만큼 차례대로 숫자 생성
# range 객체로 생성되므로
# 실제 출력을 확인하려면 리스트, 튜플, 집합 형태로 자료형 변경

# list( range(start, end , step) )
# : 순차적으로 숫자로 구성된 리스트
# tuple( range(start, end , step) )
# : 순차적으로 숫자로 구성된 튜플
# set( range(start, end , step) )
# : 순차적으로 숫자로 구성된 집합



# 1~20 사이의 짝수 또는 홀수로 구성된 리스트 생성하기
'''
listEven = list(range(2,21,2))
listOdd = list(range(1,21,2))
'''

# for 문과 range
# for 인덱스변수 in range(start,end,step):
#   명령문
# 다른 언어들 => for(초기값; 조건식; 증감치) {}

# 1~10까지 출력하기

# 1~10까지 홀수만 출력하기

# 1~100사이의 합 구하기

# 1~10 모두 곱한 값 구하기
# 1x2X...X10 = ?


# for 문에서 조건문 실행
# 1~25 까지 한줄에  5개씩 출력하기
'''
1 2 3 4 5
6 7 8 9 10
..
21 22 23 24 25
'''

# 1~27 에서 5의 배수만 빼고 출력하기

# 다중 for문과 range()
'''
for i in range(0,3):
    print('-'*30)
    for j in range(0,3):
        print('Hello world')
'''

# 다중 for 문을 이용하여 구구단 출력

# 리스트 for = 리스트 내포
# 리스트 안에 for 문이 내포된 형태
# 결과값으로 구성된 리스트가 생성된다.
# 리스트변수 = [ 결과값 for 명령문 ]

# 1~10까지 숫자로 이루어진 리스트를 만들어라
'''
numList1 = []
for i in range(1,11):
    numList1.append(i)
print('numList1 = ',numList1)

numList2 = [i for i in range(1,11)]
print('numList2 = ', numList2)
'''

# 3단의 결과값으로 리스트를 만들어라

# 3단의 결과값에서 -1 한 값으로 리스트를 만들어라

# 아래와 같은 형태로 리스트를 만들어라
# ['*', '**', '***' .... ,'**********']
'''
numList5 = ['*'*i for i in range(1,11)]
print('numList5 = ', numList5)
for i in range(0, len(numList5)):
    print(numList5[i])
for i in range(0, len(numList5)):
    print(numList5[len(numList5)-1-i])
'''

# 리스트 다중 for
# 리스트안에 이중 for문이 있는 형태
# 구구단의 결과값을 리스트로 추가
'''
numList6 = []
for i in range(2,11):
    for j in range(1,10):
        numList6.append(i*j)
'''
'''
numList7 = [i*j for i in range(2,11) for j in range(1,10)]
print('numList7 = ',numList7)
'''

#-------------------------
#-------------------------

# 자료형의 각 요소 값을 순차적으로 출력
# for 인덱스변수 in 리스트,문자열,튜플:
#   명령문

# 리스트를 생성하고 아이템을 출력하여라
'''
myList = ['구로동', '신림동', '서초동', '역삼동']
for i in myList:
    print(f'** {i} **')
'''

# 문자열을 한줄에 한글자씩 출력하여라
'''
myText = '가나다라마바사'
for i in myText:
    print(i)
'''

# 퀴즈 : 다음 리스트에서 평균, 합, 최소값 출력하기



# for 를 이용한 딕셔너리 요소 출력
# for 키변수 in 딕셔너리:
#   명령문

# 아래의 딕셔너리를 키 => 값 형태로 세로로 출력하여라
myDict = {1:'일', 100:'백', 50:'오십', 1000:'천'}
# 딕셔너리변수[키] => 값
print(myDict[1000]) # 천
print('='*50)
for key in myDict:
    print(key, ' => ',  myDict[key])
# 1  =>  일
# 100  =>  백
# 50  =>  오십
# 1000  =>  천

# 다중 리스트와 for
# 리스트안에 삽입되어 있는 리스트의 갯수가 같아야 한다.
# for (i, j...) in 다중리스트:
#   명령문

# 3*2
listMulti = [[1, 2],
             ['a', 'b'],
             ['홍길동','춘향이']]
# 다중 리스트 (중첩 리스트) 안에서의 개별 인덱스
print(listMulti[0]) # [1, 2]
print(listMulti[1]) # ['a', 'b']
print(listMulti[2][1]) # 춘향이



# 퀴즈 : 학생이름, 국어, 영어, 수학 으로 구성된
# 2차원 리스트를 생성한다.
# 출력형식은 아래와 같이 한다.
'''
학생이름  국어  영어  수학  합계  평균
김태희     30   40   100   ?     ?
...

'''


stGradeList = [['김태희', 30, 50, 55],
               ['신민아', 50, 90, 80],
               ['박지민', 50, 90, 40],
               ['김소희', 60, 50, 56],
               ['윤준희', 90, 88, 66]]

print('학생이름 국어 영어 수학     합계 평균')
for (student, kor, eng, math) in stGradeList:
    tot = kor + eng + math
    print(f'{student} {kor} {eng} {math}        {tot} {tot/3:.2f}')

# 퀴즈 1
# 다음 2차원 리스트를 생성하고 결과와 같이 for...in 문을 이용하여 출력하여라
employees = [
                 ['김수철', '서울', 25, '남', '총무부'],
                 ['고길동', '부산', 33, '남', '회계부'],
                 ['최미나', '대전', 22, '여', '기획부'],
                 ['은지원', '서울', 44, '남', '영업부'],
                 ['김영탁', '울산', 36, '남', '영업부'],
                 ['마동탁', '대구', 50, '남', '기획부'],
                 ['이은미', '창원', 42, '여', '총무부']
               ]
print('-'*30)
print('사원명 출신지 나이 성별 부서')
print('-'*30)
for (name, region, age, gender, faculty) in employees:
    print(f'{name} {region} {age} {gender} {faculty}')
# 결과 =>
# 	----------------------------------------
#  	 사원명 	 출신지 	 나이 	 성별 	 부서
# 	----------------------------------------
#  	 김수철 	 서울 	 25 	 남 	 총무부
#  	 고길동 	 부산 	 33 	 남 	 회계부
#  	 최미나 	 대전 	 22 	 여 	 기획부
#  	 은지원 	 서울 	 44 	 남 	 영업부
#  	 김영탁 	 울산 	 36 	 남 	 영업부
#  	 마동탁 	 대구 	 50 	 남 	 기획부
#  	 이은미 	 창원 	 42 	 여 	 총무부

# 퀴즈2
# 위의 리스트에서 남자 사원 목록만 출력하여라
# 결과 =>
# 	----------------------------------------
#  	 사원명 	 출신지 	 나이 	 성별 	 부서
# 	----------------------------------------
#  	 김수철 	 서울 	 25 	 남 	 총무부
#  	 고길동 	 부산 	 33 	 남 	 회계부
#  	 은지원 	 서울 	 44 	 남 	 영업부
#  	 김영탁 	 울산 	 36 	 남 	 영업부
#  	 마동탁 	 대구 	 50 	 남 	 기획부

print('-'*30)
print('사원명 출신지 나이 성별 부서')
print('-'*30)
for (name, region, age, gender, faculty) in employees:
    if gender == '남':
        print(f'{name} {region} {age} {gender} {faculty}')
# 퀴즈3
# 퀴즈 1의 리스트에서 성이 '김'인 사원 목록만 출력하여라
# 결과 =>
# 	----------------------------------------
#  	 사원명 	 출신지 	 나이 	 성별 	 부서
# 	----------------------------------------
#  	 김수철 	 서울 	 25 	 남 	 총무부
#  	 김영탁 	 울산 	 36 	 남 	 영업부

print('-'*30)
print('사원명 출신지 나이 성별 부서')
print('-'*30)
for (name, region, age, gender, faculty) in employees:
    if name[0] == '김':
        print(f'{name} {region} {age} {gender} {faculty}')

'''
listMulti1 = [[1, 2],
              ['a', 'b'],
              ['홍길동', '춘향이']]

print(listMulti1[0]) # [1, 2]
print(listMulti1[0][0]) # 1
print(listMulti1[1][1]) # b

for (i, j) in listMulti1:
    print(f'i = {i}')
    print(f'j = {j}')
    print('-'*10)
'''

'''
listMulti2 = [[1, 2, 3],
              ['a', 'b', 'c'],
              ['홍길동', '춘향이', '이몽룡']]

for (i, j, k) in listMulti2:
    print(f'i = {i} , j = {j}, k={k}')
'''


# 퀴즈 : 학생이름, 국어, 영어, 수학 으로 구성된
# 2차원 리스트를 생성한다.
# 출력형식은 아래와 같이 한다.
'''
학생이름  국어  영어  수학  합계  평균
김태희     30   40   100   ?     ?
...

'''

'''
stGradeList = [['김태희', 30, 50, 55],
               ['신민아', 50, 90, 80],
               ['박지민', 50, 90, 40],
               ['김소희', 60, 50, 56],
               ['윤준희', 90, 88, 66]]

'''





