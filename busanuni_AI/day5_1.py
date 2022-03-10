'''
review

파이썬 작업환경 구축 : 아나콘다 + 파이참
주석
출력문 - print()
변수
자료형 - 숫자형(정수, 실수), 논리형(True, False), 문자열
연산자 - 산술, 대입, 논리, 관계(비교)
입력문 - input()
문자열 연산자 : +, *
문자열 인덱싱
문자열 슬라이싱
포맷팅 - %서식자, format(), f포맷팅
문자열 함수 - count(), replace() ...

===============================
집합형 자료형
리스트 [] => CRUD, 인덱싱, 슬라이싱, +, *
튜플 () => CRU, 인덱싱, 슬라이싱, +, *
딕셔너리 {키:값...} => CRUD, 키인덱싱
집합 {} => CRUD, &, -, |, ^
캐스팅 : list(), tuple(), dict(), enumerate(), split(), str(), ' '.join()

===============================
제어문 - 조건문, 반복문
if, if~else, if~elif~else
True/False 가 되는 값
while ~
for ... in 리스트/문자열/튜플
for ... in range(start, end, step)
pass
continue
break

===============================

리스트 for
함수 => 인자(Parameter, auguments, 전달변수) , return
함수 ( 인자 X, return X)
함수 ( 인자 O, return X)
함수 ( 인자 X, return O)
함수 ( 인자 O, return O)
함수 ( 인자=값....)
함수 ( 인자, 인자=값....)
함수 ( *args ) => 입력값이 튜플로
함수 ( **kwargs ) => 입력값이 딕셔너리로
'''
# -----------------------
# 함수 정의 12
# 람다 함수
# def 로 정의하지 않다.
# 한줄로 정의한다.
'''
# 람다함수 정의
함수변수 = lambda 인자:명령

# 람다함수 호출
함수변수(인자)
'''

# 일반함수 스타일
def message2(userName):
    return userName + '님 안녕하세요'

print(message2('홍길동'))
print(message2('이승기'))

# 람다함수 스타일
message3 = lambda userName:userName + '님 안녕하세요?'

print(message3('홍길동'))
print(message3('이승기'))

# 3 수의 합을 구하는 함수 정의
# 일반함수 스타일
def addNum(x, y, z):
    return f'{x} + {y} + {z} = {x+y+z}'

print(addNum(10,20,30))

# 람다함수 스타일
addNum2 = lambda x, y, z:f'{x} + {y} + {z} = {x+y+z}'
print(addNum2(10, 20, 30))

# filter(함수명/lambda 함수, 리스트/튜플),
# map(함수명/lambda 함수, 리스트/튜플),
# reduce(함수명/lambda 함수, 리스트/튜플)
# 정의된 사용자정의함수, 람다함수를  리스트 데이타 각각에 적용한다.

# filter()
# filter(함수명/lambda 함수, 리스트/튜플)
# 사용할 함수는 결과값이 True/False
# 함수를 적용하여 리스트/튜플의 data에서 True 인것만 Return
# => 참인조건의 리스트만 출력

# 리스트 중 짝수만 출력하기 = filter() 함수 이용
# 짝수인지 판독하는 함수 정의
# 리스트 정의
# filter() 함수 적용 => filter 객체
# filter 객체를 리스트화

numList = [10, 50, 3, 11, 90, 6, 7]

# 방법1 - 일반함수 사용

# 리스트를 입력받은 후 짝수만 추출해서 새로운 리스트로 반환
def odd1(dataList):
    resultList = []
    for item in dataList:
        if item%2 == 0:
            resultList.append(item)
    return resultList

print(numList, odd1(numList))

# 방법2 - filter() + 일반함수
# 짝수인지 판독하는 함수 정의 (1개의 데이터로 정의)

# 1개의 데이타에 적용될 함수 생성 => True or False
# 짝수이면 True 반환하는 함수 정의
def oddNum(x):
    if x%2 == 0:
        return True
    # else:
        # return False
print(oddNum(10))
print(oddNum(1))

# Filter() 함수 적용
# filter(함수명/lambda 함수, 리스트/튜플)
numList = [10, 50, 3, 11, 90, 6, 7]
print(filter(oddNum, numList)) # <filter object at
print(numList, list(filter(oddNum, numList))

# 방법3 - filter() + 람다 함수
#print(numList, list(filter(lambda  x:x%2 == 0, numList)))

# 리스트에서 양수만 출력하여라
numList2 = [10, -90, 0, 100, 55, -1]

# 첫번째 방법 - 일반함수 이용
# 리스트를 입력받아서 양수만 구성된 리스트 반환

def positiveNum(dataList):
    resultList = [] # 빈리스트 생성
    for item in dataList:
        if item>0: #값이 0보다 크다면
            # 리스트에 추가
            resultList.append(item)
    return  resultList
# 함수 호출
print(numList2, positiveNum(numList2))
# 두번째 방법 - filter() + 함수 이용

# 입력값이 양수이면 True 반환
def positiveNum2(x):
    return x>0

# filter() 함수로 호출
print(numList2, filter(positiveNum2, numList2))

# 세 번째 방법 - filter() + 람다함수 이용
print(numList2, list(filter(lambda x:x>0, numList2)))

# map() 함수
# map(정의된함수나 lambda함수,데이타(리스트,튜플))
# -> map오브젝트 생성
# list(map(정의된함수나 lambda함수, 데이타(리스트,튜플)))
# 데이타 요소를 정의된함수의 결과값으로 리턴한다.
# 결과값을 리스트 요소로 추가

# 리스트의 제곱을 구해서 새로운 리스트로 만들기
# [1,2,3,4] => [1, 4, 9, 16]

# 첫번째 방법 - 일반함수 이용
def powerList(dataList):
    resultList = []
    for item in dataList:
        resultList.append(item**2)
    return resultList

print('='* 50)
dataList = [1,2,3,4]
print(dataList, '=>', powerList(dataList))

# 두 번째 방법 - map() + 함수

# 리스트 각각에 대한 결과값을 리턴하는 함수 정의
# 입력 x 에 대한 제곱값을 리턴하는 함수 정의
def powerNum(x):
    return x**2
# list(map(정의된함수나 lambda함수, 데이타(리스트,튜플)))
print(dataList, '=>', map(powerNum, dataList)) #map 으로 뜸
print(dataList, '=>', list(map(powerNum, dataList))) # list로 뜸

# 새번째 방법 - map() + lambda 함수
print(dataList, '=>', list(map(lambda x:x**2, dataList)))

# 학생이름으로 구성된 리스트에서 학생명마다 문자열 재정의
# ['홍길동', '고길동', '박길동', '은지환', '이영순']
def nameList(dataList):
    resultList = []
    for item in dataList:
        resultList.append('고객' + item + '님')
    return resultList

print('='* 50)
dataList = ['홍길동', '고길동', '박길동', '은지환', '이영순']
print(dataList, '=>', nameList(dataList))

# 두 번째 방법 - map() + 일반함수
def nameData(x):
    return  '고객' + x + '님'
print('='*50)
dataList = ['홍길동', '고길동', '박길동', '은지환', '이영순']
print(dataList, '=>', list(map(nameData(, dataList))))

# 세번째 방법 - map() + lambda
dataList = ['홍길동', '고길동', '박길동', '은지환', '이영순']
print(dataList, '=>', list(map(lambda x: '고객' + x + '님', dataList)))

# random 난수 함수들
# 외장모듈 필요
# import random
# random.randint(start, end)
# : start~end 사이의 정수 난수
# random.choice(리스트)
# : 리스트에서 랜덤하게 뽑는다.
# random.shuffle(리스트)
# : 리스트를 랜덤하게 섞는다.

# 모듈 임포트
import  random
print('='*50)
print(random.randint(1, 10),random.randint(50, 100), random.randint(1000, 2000))
# 5개만 난수
for i in range(5):
    print(f'{i+1} 번째 숫자는? {random.randint(1,10)}')

# random.choice(리스트)
# : 리스트에서 랜덤하게 뽑는다.

evenList = ['신라면 1상자', '순금 10돈', '초코파이 1상자', '파리바게트 상품권 10만원', '캠핑카']
print('이벤트 당첨 확인1 =>', random.choice(evenList))
print('이벤트 당첨 확인2 =>', random.choice(evenList))

# random.shuffle(list)
# : shuffle the list randomly 원본 리스트 자체를 무작위 순으로 정리
print(evenList)
random.shuffle(evenList)
print(evenList)

#  학생중에서 2명을 뽑아서 청소당번을 지정하려고 한다.
# 오늘 당번 => ?, ?
# 내일 당번 => ?, ?
studentList = ['mimi', 'chichi','reni','lulu']
random.shuffle(studentList)
print('오늘 당번 =>'studentList[:2])
random.shuffle(studentList)
print('내일 당번 =>'studentList[:2])

lottoList = [1,36]
print('당첨자 확인1 =>', random.choice(evenList[:6]))
print('당첨자 확인2 =>', random.choice(evenList[:6]))



# 고객이름 => 인자, 리턴 값\

# 문자열을 특정 단어와 결합해서 출력한다.

#def printWord(m):
    #return 'Message => ' + m
#print(printWord('오늘도 좋은 하루'))
# Message => 오늘도 좋은 하루

#f1 = lambda message:('Message lambda => ' + message)
#print(f1('좋은 하루되세요'))
# Message lambda => 좋은 하루되세요

# 두수의 합을 출력한다.
#f2 = lambda x,y:print(f'{x} + {y} = {x+y}')
#f2(30, 100)
# 30 + 100 = 130


# -----------------------------------
# 함수의 변수 영역
# 스코프(Scope)
# 전역변수(문서 전체의 공통변수) ?
# 지역변수(함수내부에만 유효한 변수)?

# 함수내에서 지역변수를 전역변수로 정의
# global 변수명







#---------------------------

# 함수의 종류

# 사용자정의함수
# 빌트인 함수 => 파이썬에서 제공하는 함수

# import 명령의 유무
# 내장함수 : 별도의 import 명령이 필요없다
#           함수(옵션) ex) abs(), enumerate()...
# 외장함수 : 별도의 import 명령이 필요
#           모듈.함수(옵션) ex) datetime 함수



# ----------------------------------------
# datetime 모듈 이용하기
# 시간변수 = datetime.datetime.now()
# 시간변수.year
# 시간변수.month
# 시간변수.day
# 시간변수.hour


# 시간과 관련된 모듈 임포트
#import datetime

# 현재 시간을 기준으로 년,월,일,시,분,초 변수 생성


'''
2019-12-30 16:39:41.929593
 년도 :  2019
 월 :  12
 날짜 :  30
 시간 :  16
'''

# 아래와 같이 출력하여 보세요
# 오늘은 ?년 ?월 ?일 입니다.
# 현재시간은 ()시 ()분입니다.



# 퀴즈1 : if문과 datetime 모듈 이용
# 현재 시간을 아래와 같이 출력한다.
# 현재 시간은 오후 3시 () 분입니다.



# 퀴즈2 : if문과 datetime 모듈 이용
# 달을 추출 now.month
# 달에 따라 봄, 여름, 가을 ,겨울 메세지 출력
# 12, 1,2 : 겨울
# 3~5 : 봄
# 6~8 : 여름
# 9~11 : 가을
# 출력은 아래와 같이.
# 12월은 겨울입니다.


# 요일 찍기
# 요일은 (월요일)0 ~ 6(일요일)
today = datetime.datetime.today().weekday()
print(today, type(today)) # 0 <class 'int'>
if today == 0:
    print('월요일 입니다.')


# 퀴즈 :
# 아래와 같이 출력해보세요
# 2018년 8월 1일 수요일


# ----------------------------------------
# time 모듈 이용하기

# time 모듈 임포트
# import time

# time.time()
# : 현재 시간을 실수 형태로 리턴한다.

# time.localtime(time.time())
# : time.time()의 값을 년도, 월, 일, 시, 분, 초로 변경
# : 튜플 자료 구조 형태

# time.asctime(time.localtime(time.time()) )
# time.ctime()
# : time.localtime(time.time()) 에 의해 반환된 튜플 구조의 값을 알아보기 쉬운 형태로 변환

import time
print(time.time())
# 1585282117.1805494
print(time.localtime(time.time()))
# time.struct_time(tm_year=2020, tm_mon=3, tm_mday=27, tm_hour=13, tm_min=8, tm_sec=57, tm_wday=4, tm_yday=87, tm_isdst=0)

# 퀴즈 : 리스트화 한 후 아래의 출력 형태로 출력하기
# result = list(time.localtime(time.time()))
# resultFormat = ['년', '월', '일', '시', '분', '초']
'''
2020 년 / 3 월 / 27 일 / 13 시 / 13 분 / 5 초 /
'''




# 여러가지 출력 포맷 이용하기
# time.strftime('포맷코드1 포맷코드2', time.localtime(time.time()))
# 출력할 형식 포맷코드
# %a / %A  : 요일
# %b / %B  :  달
# %c : 날짜와 시간
# %d : 날(day)
# %H :24시간 기준의 시간
# %I :12시간 기준의 시간
# %j :1년중 누적 날짜 표시
# %x : 지역 기반 날짜 출력
# %X : 지역 기반 시간 출력
# %w : 숫자로된 요일 출력. 0은 일요일
# %Y : 년도 출력
# %Z : 시간대 출력
# %p : AM/PM

print('-'*30)
print(time.strftime('%x', time.localtime(time.time()))) # 03/27/20
print(time.strftime('%X', time.localtime(time.time()))) # 13:25:34
print(time.strftime('%c', time.localtime(time.time())))
# Fri Mar 27 13:25:51 2020
print(time.strftime('%a %A', time.localtime(time.time())))
# Fri Friday
print(time.strftime('%p %I', time.localtime(time.time())))
# PM 01

m = time.strftime("%m", time.localtime(time.time()))
d = time.strftime("%d", time.localtime(time.time()))
r = time.strftime("%j", time.localtime(time.time()))

# 퀴즈
'''
오늘은 03 월  27 입니다.
1년을 기준으로 087 번째 날입니다.
'''

#----------------------------------------------

# 수학관련 내장 함수
# 절대값 리턴 : abs(숫자)
# 최대값 리턴 : max(리스트/튜플/집합...)
# 최소값 리턴 : min(리스트/튜플/집합...)
# numList = [100, 45, 20, 40, 500]

num = -10
print(f'{num}의 절대값은 {abs(num)}')
numList = [100, 45, 20, 40, 500]
print(f'{numList}의 최대값은 {max(numList)}')
print(f'{numList}의 최소값은 {min(numList)}')
'''
-10의 절대값은 10
[100, 45, 20, 40, 500]의 최대값은 500
[100, 45, 20, 40, 500]의 최소값은 20
'''
numList2 = (100, 45, 20, 40, 500)
print(f'{numList2}의 최대값은 {max(numList2)}')
print(f'{numList2}의 최소값은 {min(numList2)}')


#----------------------------------------------
# 나누기 연산자 /, //
# 나머지 연산자 %
# divmod(n1,n2) => 몫과 나머지 값을 구한다. => 튜플


print(f'divmod(55,2) = {divmod(55,2)}, 데이타형 = {type(divmod(55,2))}')
# print(f'divmod(55,2) = {divmod(55,2)},
#        데이타형 = {type(divmod(55,2))}')
'''
divmod(55,2) = (27, 1), 데이타형 = <class 'tuple'>
'''
print(f'몫 = {divmod(55,2)[0]}')
print(f'나머지 = {divmod(55,2)[1]}')
'''
몫 = 27
나머지 = 1
'''

#----------------------------------------------
# enumerate(리스트/튜플/문자열 , 인덱스숫자 )
# 인덱스숫자로 구성된 리스트/튜플/문자열
# => enumerate 객체 생성
# => for .. in 하나씩아이템 출력 가능
# => 각각 튜플아이템으로 생성 (인덱스, 값)



listA = ['a','b','c']
enumResult = enumerate(listA, 5)
print(enumResult, type(enumResult))
# <enumerate object at 0x01702808> <class 'enumerate'>
for i in enumResult:
    print(i) # (인덱스번호, 값)
'''
(5, 'a')
(6, 'b')
(7, 'c')
'''
# enumResult2 => 딕셔너리 구조로 변경
# dict(enumerate(리스트/문자열/튜플, 인덱싱번호))
enumResult2 = enumerate(listA, 5)
print(dict(enumResult2), type(dict(enumResult2)))
'''
{5: 'a', 6: 'b', 7: 'c'} <class 'dict'>
'''
enumResult3 = enumerate(listA, 0)

for i, j in enumResult3:
    print(f'{i} => {j}')
'''
0 => a
1 => b
2 => c
'''


#----------------------------------------------
# eval(문자열계산식)
# 입력받은 수식을 계산하여라
result = input('수식을 입력하세요? ... ')
print(result, ' = ', eval(result))
print(result, ' = ', result)
'''
수식을 입력하세요? ... 3+4+50

3+4+50 = ?
'''


# # 퀴즈 :  5개의 값을 입력문을 이용하여 리스트로 저장한 후
# 최대값과 최소값을 출력한다.
# 빈 리스트 생성
inList = []



#-----------------------------------------
#-----------------------------------------
# 함수의 종류
# 사용자정의 함수
# - def 명령으로 함수명 정의
# - lambda 함수 : 익명함수
# 외장함수 : import 외장모듈이나 패키지
#  ex) datetime.now()
# 내장함수 : import 명령없이 사용할 수 있는 함수
#  ex) type(), len()
#    divmod(), min(), max(), abs(), eval()
#   list(), dict(), tuple(), set()
#   int(), float(), str(), bool()
#   enumerate()



#-----------------------------------------
# chr() , ord() => 아스키 코드
# all() , any() => True/False
# 유효성 검사 => True/False
# isdigit(), isalpha(), isalnum(), isnumeric(),
# islower(), isupper(), isdecimal()
# 정렬
# sort(), reverse(), sorted()
# 별도의 Object로 생성 = 다른 함수, lambda 함수에 적용
# zip(), fillter(), map()
# 객체에 대한 속성과 메소드 표시
# dir()

print('-'*10, '\n'*2)
# 내장함수 : 아스키코드와 관련된 함수
# char() , ord()
# char(숫자) => 아스키코드값에 해당하는 문자나 숫자
# 문자의 아스키 코드 값을 돌려주는 함수
# 0에서 127 사이의 숫자를 각각 하나의 문자 또는 기호에
# ord(관련 문자나 숫자) => 아스키코드값
# char()과 반대되는 함수
# 대응시켜 놓은 코드표
# https://ko.wikipedia.org/wiki/ASCII
print(chr(65)) # 'A'
print(chr(97)) # 'a'
print(chr(48)) # '0'
print(ord('A')) # 65
print(ord('a')) # 97
print(ord('0')) # 48
print('-'*10, '\n'*2)


#-----------------------------------------
# 리스트/튜플 등의 원소값이 False 값인지 True 값인지
# Boolean 형(True/False)로 표시
# all(리스트/튜플/집합) :  값이 모두 True 조건이면 True
# any(리스트/튜플/집합) : 값중 하나라도 True 조건이면 True
# False 조건값 : None, 0, 0.0, '', False
listA = [0, False, '', ' ']
setB = {0, False, '', None, 0.0}
tupleC = (1, 2, 3, True, 'Yes')
print(any(listA)) # True
print(any(setB)) # False
print(any(tupleC)) # True
print(all(listA)) # False
print(all(setB)) # False
print(all(tupleC)) # True

print('-'*10, '\n'*2)


#-----------------------------------------
# 유효성 검사?
# 데이터(숫자, 문자...)가 조건에 맞는지 검사하는 기능
# 문자열변수.isalpha()
# : 모두 문자(알파벳,한글..)인가? 숫자문자제외 , True/Fasle
# 문자열변수.isdigit() , 문자열변수.isnumeric()
# : 모두 숫자문자인가?  , True/Fasle
# 문자열변수.isalnum() : 문자열과 숫자로만 구성되어 있는가?
# islower(), isupper() : 대문자/ 소문자 검사
# isdecimal() : 모두 10진수인가?
str1 = 'fkfkfk'
str2 = '12345'
str3 = '1fdkjfsl2345'
str4 = 'BANANA'
str5 = '#&^=+'
print(str1.isalpha()) # True
print(str2.isalpha()) # False
print(str3.isdigit()) # False
print(str1.isdigit()) # False
print(str2.isdigit()) # True
print(str3.isalnum()) # True
print(str4.isupper()) # True
print(str1.islower()) # True
print(str2.isdecimal()) # True
print(str3.isdecimal()) # False
print(str5.isalpha()) # False
print('-'*10, '\n'*2)

# 퀴즈 : 숫자로 구성된 리스트 생성 (길이는 5)
# 빈 리스트를 생성한다.
# 입력문이 실행된다.
# 입력값이 숫자이면 리스트에 추가한다.
# 입력값이 숫자가 아니면 다시 입력문이 실행된다.
# 리스트의 전체길이가 5이면 입력을 종료한다.
# 리스트를 출력한다.

# # 결과값을 저장할 빈 리스트 생성
# resultList = []


# 퀴즈 : 문자열에서 숫자와 숫자가아닌문자의 갯수를 출력하여라
# testWord = 'Python1234Java4774'
'''
결과 >>
숫자 갯수 : ?
문자 갯수 : ?
'''



#-----------------------------------------
print('-'*10, '\n'*2)
# 정렬과 관련된 내장 함수
# sorted(리스트/튜플/집합..)
# : 바로 인쇄 가능. 튜플과 집합은 정렬된 형태의 리스트로 변경
# : 데이타 정렬
# : 결과값을 리턴한다. => print()로 바로 출력
# 리스트이름.sort() : 리스트정렬
# 리스트이름.reverse() : 리스트 역정렬

myList= ['b', 'a','c','x']
myTuple= ('b', 'a','c','x')
mySet= {'b', 'a','c','x'}
print(myList.sort()) # None
myList.sort()
# 오류 발생 : AttributeError
# myTuple.sort()
print(myList) # ['a', 'b', 'c', 'x']
myList.reverse()
print(myList) # ['x', 'c', 'b', 'a']
# 바로 출력 가능
print(sorted(['b', 'a','c','x'])) # ['a', 'b', 'c', 'x']
print(sorted(myTuple)) # ['a', 'b', 'c', 'x']
print(sorted(mySet)) # ['a', 'b', 'c', 'x']

print('-'*10, '\n'*2)



#-----------------------------------------
# dir(자료형) => Reference 기능
# 사용가능한 속성과 함수를 리스트 구조로 표시
print(dir('String'))
print(dir(True))
print(dir(100))
print(dir([1,2,3,4,5]))
print(dir((1,2,3,4,5)))
print(dir({1:'하나', 2:'둘'}))
print(dir({1,2,3,4,5}))
print('-'*10, '\n'*2)

'''
['__add__', '__class__', '__contains__',
'__delattr__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__',
  '__getitem__', '__getnewargs__', '__gt__',
  '__hash__', '__init__', '__init_subclass__',
   '__iter__', '__le__', '__len__', '__lt__',
   '__mod__', '__mul__', '__ne__', '__new__',
   '__reduce__', '__reduce_ex__', '__repr__',
   '__rmod__', '__rmul__', '__setattr__',
   '__sizeof__', '__str__', '__subclasshook__',
    'capitalize', 'casefold', 'center', 'count',
     'encode', 'endswith', 'expandtabs',
     'find', 'format',
     'format_map', 'index',
     'isalnum', 'isalpha', 'isascii',
     'isdecimal', 'isdigit', 'isidentifier',
      'islower', 'isnumeric', 'isprintable',
      'isspace', 'istitle', 'isupper', 'join',
      'ljust', 'lower', 'lstrip', 'maketrans',
      'partition', 'replace', 'rfind', 'rindex',
      'rjust', 'rpartition', 'rsplit', 'rstrip',
      'split', 'splitlines', 'startswith', 'strip',
       'swapcase', 'title', 'translate', 'upper',
       'zfill']

'''

#-----------------------------------------
# zip(리스트1, 리스트2 .. )
# zip 객체로 리턴 => for...in zip 문 이용해서 아이템 확인
# : 리스트의 각 아이템요소를 튜플화 구조로 묶어준다.
# list(zip 객체): [(아이템1,아이템2) ...]
# zip(*zip객체)
# : zip으로 묶어준 객체를 원래대로 풀어준다.

p1 = ['길동', '동미', '미영', '영철']
p1Gender= ['남','여','여','남']
# zip 객체로 출력
print(zip(p1, p1Gender))
# 하나씩 출력
for i in zip(p1, p1Gender):
    print(i)
# 각각 구분자로 분리해서 출력
for i, j in zip(p1, p1Gender):
    print(i, '-', j)
# 리스트화
print(list(zip(p1, p1Gender)))
# [('길동', '남'), ('동미', '여'), ('미영', '여'), ('영철', '남')]

# zip으로 리스트안의 튜플구조 해제하기 - unzip
# 변수1, 변수2 = zip(*리스트튜플이름)
# 결과물은 같은 인덱스의 값만 튜플로 다시 생성
# 리스트 튜플 정의
myList2 = [('a','apple'),('b','banana'),('c','cat')]
print(myList2, type(myList2))
x,y = zip(*myList2)
print(x) # ('a', 'b', 'c')
print(y) # ('apple', 'banana', 'cat')

print('-'*10, '\n'*2)



# 딕셔너리 구조를 튜플 형태로 변경
# 딕셔너리  => 키 리스트, 값 리스트 => zip =>  unzip 튜플
myDict = {'a':'africa', 'd':'drama', 'm':'movie'}
print(f'myDict = {myDict}, {type(myDict)}')
# 키 조합으로 리스트 생성
print(list(myDict))
# 값만 조합으로 리스트 생성
print(list(myDict.values()))
# zip 객체로 변경한 후 하나씩 출력
print(zip(list(myDict), list(myDict.values())))
for i in zip(list(myDict), list(myDict.values())):
    print(i)
# zip 객체의 리스트화 => 리스트 튜플
print(list(zip(list(myDict), list(myDict.values()))))
# unzip => 튜플
x,y = zip(*zip(list(myDict), list(myDict.values())))
print(x)
print(y)
'''
myDict = {'a': 'africa', 'd': 'drama', 'm': 'movie'}, <class 'dict'>
['a', 'd', 'm']
['africa', 'drama', 'movie']
<zip object at 0x02FC3228>
('a', 'africa')
('d', 'drama')
('m', 'movie')
[('a', 'africa'), ('d', 'drama'), ('m', 'movie')]
('a', 'd', 'm')
('africa', 'drama', 'movie')
'''

print('-'*10, '\n'*2)

