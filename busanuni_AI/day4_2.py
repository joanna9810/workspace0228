# 사용자정의함수 정의
# 함수정의 문법
'''
def 함수이름(인자1, 인자2...):
    명령문
    ...
    return 문
'''

# 호출시
# 함수명(값1, 값2 ...)

# 함수 정의 1
# 인자도 없고 return문도 없음

# 함수 호출시 특정 메세지 3번 출력
# 함수 정의
def helloWorld():
    print('Hello world\t\t'*3)

# 함수 호출
helloWorld()
helloWorld()
print('#'*40)
def hello():
    n = 10 #지역 변수
    for i in range(n):
        print(f' {i} => Hello world') # 변수를 바꾸고 싶은 타이핑만 바꾸면 됨

# 함수 호출1
hello()
# 함수 호출2
hello()
# 함수 정의 2
# 인자가 있다. return이 없다.
# 인자 = 파라미터 = 아규먼트 (arguments) = 전달 변수
'''
def 함수명(인자1,인자2..):
    인자가 있는 명령문
'''
# 호출
# 함수명(값1, 값2...)

# 메세지를 n번 출력하는 함수 정의
def hello2(message, n):
    for i in range(n):
        print(f'{i} => {message}')
    print('='*50)
hello2('오늘도 좋은 하루!', 3)
hello2('Good night', 5)

# 함수 정의 3
# 인자가 없다. return이 있다
# return 문은 함수를 탈출하는 용도로도 사용.
# return 문 아래의 명령은 실행이 되지 않는다.
'''
def 함수명():
    명령문...
    return 결과값/수식/명령문

# 호출 
함수이름()       
'''
# 값을 입력받아서 메세지를 생성한다.
def hello3():
    userName = input('당신의 이름은?...')
    message = userName + ' 님 환영합니다.'
    return message # 내보내면 명령 끝, 그 밑은 실행이 되지 x
# 함수 호출
# 출력문안에 함수 호출 한 경우
print(hello3())
# 함수 호출 2
result = hello3()
print(hello3())

# 함수 정의 4
# 인자가 있다. return이 있다
'''
def 함수명(인자1, 인자2...):
    인자에 관련된 명령문...
    return 결과값/수식/명령문


# 호출
# 함수명(값1, 값2...)
'''
# n~m 까지의 합을 구하는 함수 정의
# n, m 은 인자로 전달
# n~m 까지의 합 은 함수의 최종값으로 return 받는다

def sumNM(n, m):
    tot = 0
    for i in range(n, m+1):
        tot += i
    return tot
print('1~100 까지의 합은?', sumNM(1, 100))
print(f'51~80 까지의 합은? {sumNM(51, 80)}')

# 두수의 곱이나 두수의 합을 구하는 함수 정의
# calc( x, y, 연산자) 호출
# 연산자에 따라 결과 형태가 다르게 한다.
# if, return 문
def calc(x,y,op):
    if op == '+':
        return x+y
    elif op == '*':
        return x*y
    else:
        return '계산 불가'
print(calc(100, 56, '+'))
print(calc(100, 56, '*'))
print(calc(100, 56, '#'))

#or
def calc(x, y, op):
    if op == '+':
        return f' {x} + {y} = {x+y}'
    elif op == '*':
        return f' {x} X {y} = {x*y}'
    else:
        return '계산 불가'

print(calc(100, 56, '+'))
print(calc(100, 56, '*'))
print(calc(100, 56, '#'))

# 퀴즈
# 출생년도에 따른 띠를 구하는 함수 정의
# 출생년도%12 나머지값 이용

def animal(year):
    animalList = ['원숭이띠', '닭띠', '개띠', '돼지띠', '쥐띠', '소띠', '범띠', '토끼띠', '용띠', '뱀띠', '말띠', '양띠']
    index = year % 12
    return f' 태어난 년도는 {year} 이고 {animalList[index]}띠 입니다.'

# 인자 O, return O
def animal(year):
    animalList = ['원숭이띠', '닭띠', '개띠', '돼지띠', '쥐띠', '소띠', '범띠', '토끼띠', '용띠', '뱀띠', '말띠', '양띠']
    index = year % 12
    return f"태어난 년도는 {year} 이고, {animalList[index]} 입니다."

print('='*50)
print(animal(2022))

# 인자 O, return O
def animal(year):
    animalList = ['원숭이띠', '닭띠', '개띠', '돼지띠', '쥐띠', '소띠', '범띠', '토끼띠', '용띠', '뱀띠', '말띠', '양띠']
    index = year % 12
    return f"태어난 년도는 {year} 이고, {animalList[index]} 입니다."

print('='*50)
print(animal(2022))
# 함수 호출은
# animal(출생년도)
# 태어난 년도는 ???? 이고 ??? 띠입니다.

# 함수 정의 5
# 인자가 있다. return 값이 다중인 경우
# 다중 return 값인 경우 자료형은 튜플
# (결과값1, 결과값2...)
# 각각의 결과값은 인덱싱 으로 접근할 수 있다.
'''
def 함수명(인자1, 인자2...):
    인자에 관련된 명령문...
    return 값1/수식1 , 값2/수식2 ...

# 호출
# 함수명(값1, 값2...)

'''

# 메세지를 인자로 넘겨서 3번 출력하는 함수 정의
def messagePrint(message):
    print(message*3)

# 값 전달 함수 호출
messagePrint('Hello Python')
messagePrint('Hello MySQL')
# TypeError : 정의된 인자 갯수가 틀려서 에러 발생
# messagePrint('Hello MySQL', 'Hello Python')

# 두수의 합을 구하는 함수 정의
def addNumber(x, y):
    print(f'x = {x}')
    print(f'y = {y}')
    print(f'두수의 합 = {x+y}')

# 함수 호출
addNumber(100, 30)
addNumber(5, 7)
'''
x = 100
y = 30
두수의 합 = 130
x = 5
y = 7
두수의 합 = 12
'''

# 함수 정의 3
# 인자가 없다. return이 있다
# return 문은 함수를 탈출하는 용도로도 사용.
# return 문 아래의 명령은 실행이 되지 않는다.
'''
def 함수명():
    명령문...
    return 결과값/수식/명령문
'''
# 호출
# 함수명()

def classPrint():
    return 'MySQL, SQLite'

# 함수 호출
print(classPrint())

def classPrint2():
    # 함수 내부에서 2개의 변수 정의
    message1 = 'MySQL1'
    message2 = 'SQLite2'
    # return message2 # SQLite2
    message2+=message1
    return message2 # SQLite2MySQL1

# 함수 호출
print(classPrint2())

# 퀴즈
# 2개의 인자를 받아서 +,-,/,*,% 출력하기
'''
def cal(인자정의):
    ....

cal(2,3)

2 + 3 = ?
2 - 3 = ?
2 * 3 = ?
2 / 3 = ?
2 % 3 = ?
'''

def cal(a, b):
    print(' %d + %d = %d ' % (a,b,a+b))
    print(' %d - %d = %d ' % (a,b,a-b))
    print(' %d * %d = %d ' % (a,b,a*b))
    print(' %d / %d = %.2f' % (a,b,a/b))
    # %% 는 2번 입력
    print(' %d %% %d = %d ' % (a,b,a%b))
    print('-'*30)

cal(10,3)
'''
 10 + 3 = 13
 10 - 3 = 7
 10 * 3 = 30
 10 / 3 = 3.33
 10 % 3 = 1
'''

# 함수 정의 4
# 인자가 있다. return이 있다
'''
def 함수명(인자1, 인자2...):
    인자에 관련된 명령문...
    return 결과값/수식/명령문
'''
# 호출
# 함수명(값1, 값2...)

def messagePrint2(m):
    return 'Happy New Year.'+ m + ' 님'

print(messagePrint2('홍길동'))
print(messagePrint2('이영희'))

# 숫자를 받아서 1~숫자까지의 합구하기
'''
sum = 0
for i in range(1,101):
    sum += i
print(sum)
'''

def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

print('50까지의 합은? ',sum(50))
print('100까지의 합은? ',sum(100))

'''
퀴즈 1:
2개의 수 x, y를 인자로 전달하여 누적합 구하기
x~y까지의 합 함수로 변경
'''
#sum2(10,20) : 10~20까지의 합 반환

'''
퀴즈 2:
n개의 입력을 받아서 리스트에 저장하는 함수 정의

printList(5) # 5개로 구성된 리스트 반환
printList(3) # 3개로 구성된 리스트 반환
'''

def sum2(x, y):
    sum = 0
    for i in range(x, y+1):
        sum += i
    # return print(f'{x}부터 {y}의 합은? {sum}')
    return sum

print('5~10까지의 합은? ',sum2(5,10))
print('10~50까지의 합은? ',sum2(10,50))
'''
5~10까지의 합은?  45
10~50까지의 합은?  1230
'''

def printList(n):
    resultList = []
    print(f'\n\n{n}개 입력')
    for i in range(0, n):
        temp = input('리스트 아이템을 입력하세요 ...')
        resultList.append(temp)
    return print(resultList)

# printList(3)
# printList(5)


# 함수 정의 5
# 인자가 있다. return 값이 다중인 경우
# 다중 return 값인 경우 자료형은 튜플
# (결과값1, 결과값2...)
# 각각의 결과값은 인덱싱 으로 접근할 수 있다.
'''
def 함수명(인자1, 인자2...):
    인자에 관련된 명령문...
    return 결과값1, 결과값2 ....
'''
# 호출
# 함수명(값1, 값2...)

# 두개의 인자를 전달한 후 합과 차의 결과를 리턴한다.
def multiReturn(n, m):
    return n+m, n-m

print(multiReturn(50, 20), type(multiReturn(50, 20)))
'''
(70, 30) <class 'tuple'>
'''
result1 = multiReturn(50, 20)
print(f'두수의 합은? {result1[0]}')
print(f'두수의 차는? {result1[1]}')

# 함수 정의 6
# 인자의 초기값 설정 (모든 인자의 초기값이 있는 경우)
'''
def 함수명(인자1=값1, 인자2=값2):
    인자에 관련된 명령문...
    return 값/변수/수식/명령문
'''
# 호출
# 함수명()
# 함수명(값1)
# 함수명(값1, 값2)
# 두수의 합 리턴. 초기값 있음
def sum3(n=0, m=10):
    return print(n+m)
sum3() # 10
sum3(20) # 30
sum3(20,30) # 50


# 함수 정의 7
# 인자의 초기값 설정 (인자의 일부만 초기값이 있는 경우)
# 주의 사항은 마지막 인자부터 초기값이 있어야 한다.
'''
def 함수명(인자1, 인자2=값2):
    인자에 관련된 명령문...
    return 값/변수/수식/명령문
'''
# 호출
# 함수명(값1)
# 함수명(값1, 값2)

# 두수의 곱을 리턴한다.
# def mul(n=1, m): # SyntaxError
def mul(n, m=1):
    return print(f'{n}x{m}={n*m}')

# mul() # TypeError
mul(7) # 7x1=7
mul(7, 8) # 7x8=56

#-------------------------------------
#--------------------------------------


# 함수 정의 8
# 가변인자인 경우 : 인자의 갯수가 정해지지 않는 경우
# *args => arguments
# 인자가 args 튜플로 반환
'''
def 함수명(*args):
    args에 관련된 명령문...
    return 값/변수/수식/명령문
'''
# 호출
# 함수명(값1)
# 함수명(값1, 값2)
# 함수명(값1, 값2, 값3 ...)

# 학생의 이름을 출력한다.
def studentName(*args):
    print(f'수강학생 목록 : {args}')
    print(f'데이터형은? {type(args)}')
    print(f'첫번째 수강생 목록: {args[0]}')
    print('-'*20)

# studentName()
studentName('홍길동')
studentName('홍길동', '이순신')
studentName('홍길동', '이순신', '이몽룡')

# 퀴즈1 . 위의 예제를 다음 형태로 변경하여라
'''
studentName2('홍길동')
1번 학생 : 홍길동

studentName2('홍길동', '이순신')
1번 학생 : 홍길동
2번 학생 : 이순신

studentName2('홍길동', '이순신', '이몽룡')
1번 학생 : 홍길동
2번 학생 : 이순신
3번 학생 : 이몽룡
'''

# 퀴즈2. n개의 숫자의 합을 구하는 가변함수를 정의하여라
'''
sumNumber(1,2) => 1+2=?
sumNumber(4,5,6) => 4+5+6=?
'''







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
myDict = {1:'일', 100:'백', 50:'오십', 1000:'천'}
for key in myDict:
    print(key, '=>',myDict[key])

# 다중 리스트와 for
# 리스트안에 삽입되어 있는 리스트의 갯수가 같아야 한다.
# for (i, j...) in 다중리스트:
#   명령문
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



#--------------------------------------------

# 사용자정의함수 정의
# 함수정의 문법
'''
def 함수이름(인자1, 인자2...):
    명령문
    ...
    return 문
'''

# 호출시
# 함수명(값1, 값2 ...)

# 함수 정의 1
# 인자도 없고 return문도 없음

# 함수 호출시 특정 메세지 3번 출력
# 함수 정의
def helloWorld():
    print('Hello world\t\t'*3)

# 함수 호출
helloWorld()
helloWorld()

# 함수 정의 2
# 인자가 있다. return이 없다.
'''
def 함수명(인자1,인자2..):
    인자가 있는 명령문
'''
# 호출
# 함수명(값1, 값2...)

# 메세지를 인자로 넘겨서 3번 출력하는 함수 정의
def messagePrint(message):
    print(message*3)

# 값 전달 함수 호출
messagePrint('Hello Python')
messagePrint('Hello MySQL')
# TypeError : 정의된 인자 갯수가 틀려서 에러 발생
# messagePrint('Hello MySQL', 'Hello Python')

# 두수의 합을 구하는 함수 정의
def addNumber(x, y):
    print(f'x = {x}')
    print(f'y = {y}')
    print(f'두수의 합 = {x+y}')

# 함수 호출
addNumber(100, 30)
addNumber(5, 7)
'''
x = 100
y = 30
두수의 합 = 130
x = 5
y = 7
두수의 합 = 12
'''

# 함수 정의 3
# 인자가 없다. return이 있다
# return 문은 함수를 탈출하는 용도로도 사용.
# return 문 아래의 명령은 실행이 되지 않는다.
'''
def 함수명():
    명령문...
    return 결과값/수식/명령문
'''
# 호출
# 함수명()

def classPrint():
    return 'MySQL, SQLite'

# 함수 호출
print(classPrint())

def classPrint2():
    # 함수 내부에서 2개의 변수 정의
    message1 = 'MySQL1'
    message2 = 'SQLite2'
    # return message2 # SQLite2
    message2+=message1
    return message2 # SQLite2MySQL1

# 함수 호출
print(classPrint2())

# 퀴즈
# 2개의 인자를 받아서 +,-,/,*,% 출력하기
'''
def cal(인자정의):
    ....

cal(2,3)

2 + 3 = ?
2 - 3 = ?
2 * 3 = ?
2 / 3 = ?
2 % 3 = ?
'''

def cal(a, b):
    print(' %d + %d = %d ' % (a,b,a+b))
    print(' %d - %d = %d ' % (a,b,a-b))
    print(' %d * %d = %d ' % (a,b,a*b))
    print(' %d / %d = %.2f' % (a,b,a/b))
    # %% 는 2번 입력
    print(' %d %% %d = %d ' % (a,b,a%b))
    print('-'*30)

cal(10,3)
'''
 10 + 3 = 13
 10 - 3 = 7
 10 * 3 = 30
 10 / 3 = 3.33
 10 % 3 = 1
'''

# 함수 정의 4
# 인자가 있다. return이 있다
'''
def 함수명(인자1, 인자2...):
    인자에 관련된 명령문...
    return 결과값/수식/명령문
'''
# 호출
# 함수명(값1, 값2...)

def messagePrint2(m):
    return 'Happy New Year.'+ m + ' 님'

print(messagePrint2('홍길동'))
print(messagePrint2('이영희'))

# 숫자를 받아서 1~숫자까지의 합구하기
'''
sum = 0
for i in range(1,101):
    sum += i
print(sum)
'''

def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

print('50까지의 합은? ',sum(50))
print('100까지의 합은? ',sum(100))

'''
퀴즈 1:
2개의 수 x, y를 인자로 전달하여 누적합 구하기
x~y까지의 합 함수로 변경
'''
#sum2(10,20) : 10~20까지의 합 반환

'''
퀴즈 2:
n개의 입력을 받아서 리스트에 저장하는 함수 정의

printList(5) # 5개로 구성된 리스트 반환
printList(3) # 3개로 구성된 리스트 반환
'''

def sum2(x, y):
    sum = 0
    for i in range(x, y+1):
        sum += i
    # return print(f'{x}부터 {y}의 합은? {sum}')
    return sum

print('5~10까지의 합은? ',sum2(5,10))
print('10~50까지의 합은? ',sum2(10,50))
'''
5~10까지의 합은?  45
10~50까지의 합은?  1230
'''

def printList(n):
    resultList = []
    print(f'\n\n{n}개 입력')
    for i in range(0, n):
        temp = input('리스트 아이템을 입력하세요 ...')
        resultList.append(temp)
    return print(resultList)

# printList(3)
# printList(5)


# 함수 정의 5
# 인자가 있다. return 값이 다중인 경우
# 다중 return 값인 경우 자료형은 튜플
# (결과값1, 결과값2...)
# 각각의 결과값은 인덱싱 으로 접근할 수 있다.
'''
def 함수명(인자1, 인자2...):
    인자에 관련된 명령문...
    return 결과값1, 결과값2 ....
'''
# 호출
# 함수명(값1, 값2...)

# 두개의 인자를 전달한 후 합과 차의 결과를 리턴한다.
def multiReturn(n, m):
    return n+m, n-m

print(multiReturn(50, 20), type(multiReturn(50, 20)))
'''
(70, 30) <class 'tuple'>
'''
result1 = multiReturn(50, 20)
print(f'두수의 합은? {result1[0]}')
print(f'두수의 차는? {result1[1]}')

# 함수 정의 6
# 인자의 초기값 설정 (모든 인자의 초기값이 있는 경우)
'''
def 함수명(인자1=값1, 인자2=값2):
    인자에 관련된 명령문...
    return 값/변수/수식/명령문
'''
# 호출
# 함수명()
# 함수명(값1)
# 함수명(값1, 값2)
# 두수의 합 리턴. 초기값 있음
def sum3(n=0, m=10):
    return print(n+m)
sum3() # 10
sum3(20) # 30
sum3(20,30) # 50


# 함수 정의 7
# 인자의 초기값 설정 (인자의 일부만 초기값이 있는 경우)
# 주의 사항은 마지막 인자부터 초기값이 있어야 한다.
'''
def 함수명(인자1, 인자2=값2):
    인자에 관련된 명령문...
    return 값/변수/수식/명령문
'''
# 호출
# 함수명(값1)
# 함수명(값1, 값2)

# 두수의 곱을 리턴한다.
# def mul(n=1, m): # SyntaxError
def mul(n, m=1):
    return print(f'{n}x{m}={n*m}')

# mul() # TypeError
mul(7) # 7x1=7
mul(7, 8) # 7x8=56

#-------------------------------------
#--------------------------------------


# 함수 정의 8
# 가변인자인 경우 : 인자의 갯수가 정해지지 않는 경우
# *args => arguments
# 인자가 args 튜플로 반환
'''
def 함수명(*args):
    args에 관련된 명령문...
    return 값/변수/수식/명령문
'''
# 호출
# 함수명(값1)
# 함수명(값1, 값2)
# 함수명(값1, 값2, 값3 ...)

# 학생의 이름을 출력한다.
def studentName(*args):
    print(f'수강학생 목록 : {args}')
    print(f'데이터형은? {type(args)}')
    print(f'첫번째 수강생 목록: {args[0]}')
    print('-'*20)

# studentName()
studentName('홍길동')
studentName('홍길동', '이순신')
studentName('홍길동', '이순신', '이몽룡')

# 퀴즈1 . 위의 예제를 다음 형태로 변경하여라
'''
studentName2('홍길동')
1번 학생 : 홍길동

studentName2('홍길동', '이순신')
1번 학생 : 홍길동
2번 학생 : 이순신

studentName2('홍길동', '이순신', '이몽룡')
1번 학생 : 홍길동
2번 학생 : 이순신
3번 학생 : 이몽룡
'''

# 퀴즈2. n개의 숫자의 합을 구하는 가변함수를 정의하여라
'''
sumNumber(1,2) => 1+2=?
sumNumber(4,5,6) => 4+5+6=?
'''



