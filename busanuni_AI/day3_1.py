# 파이썬 제어문
# 제어문의 종류
# - 조건문 : if / if ~ else / if ~elif~else
# - 반복문 : for / while

# 파이썬 제어문의 특징 :
# {} 사용하지 않고 탭1개 나 공백4칸 으로 블록 지정
# 들여쓰기가 없는 경우 IndentationError: 에러 발생
# switch 문이 없다
# else if 대신 elif 문이 있다

# 조건문 if

# 조건문 1 - 단순 if 문
# 조건이 참이면 명령문 실행
# 조건에 값이 올 수도 있음 (iterary)
# if 조건:
#   명령문

# 변수값이 양수이면 메세지 출력.
# if 안에 실행되는 명령문이 한개인 경우 한줄 코딩 가능
mynum = 100
if mynum > 0: print('양수이다')
print('if 테스트 종료')

# id, pw 가 맞으면 메세지 출력
user_id = '가든'
user_pw = 'fruit'
if (user_id == '가든') and (user_pw == "fruit"):
    print('로그인 되었습니다')
    print(f'{user_id} 님 오늘도 좋은 하루!')

# 조건식에서 True 가 되는 조건 =
# True, 0 만 빼고 나머지 숫자 길이가 0 니 아닌 문자열, 튜플, 리스트, 딕셔너리
# 조건식에서 False 가 되는 조건
# = False, 0, '', None, []. (), {}

print('='*50)
if True:
    print('Hello wolrd')
print('if 데스트 종료2')

print('='*50)
status = '가나다'

if status:  # 빈 문자열 False
    print("Hello world")
print("if 테스트 종료3")

status = [0] # 빈리스트 false로 인식

if status:  # 리스트 False
    print("Hello world")
print("if 테스트 종료4")

print('+'*50)
status = None # false

if status:
    print("Hello world")
print("if 테스트 종료5")

# 짝수인지 홀수인지 판단 ?
# 숫자%2 == 0
n = 99
if (n%2 == 0):
    print("짝수")
if (n%2 != 0):
    print("홀수")

# 조건문 2
# if 조건: - 2가지 조건이 있는 if문
#   명령문1
# else:
#   명령문2

# 짝수인지 홀수인지 판단 ?
# 숫자%2 == 0
print('='*50)
n = 99
if (n%2 == 0):
    print("짝수")
else:
    print("홀수")

# 퀴즈 :
# 숫자를 입력받아서 메세지를 출력하여라 (if ~ else)
# 숫자값이 3의 배수이면 3의 배수이다.
# 그렇지 않으면 3의 배수가 아니다.

'''
숫자를 입력해주세요 ? ...
3의 배수이다.
3의 배수가 아니다.
'''
print('='* 50)
n = int(input())
if (n%3 == 0):
    print("3의 배수이다")
else:
    print("3의 배수가 아니다.")

# 조건문 3 - 다중 if문
# if 조건1:
#   명령문1
# elif 조건2:
#   명령문2
# else:
#   명령문3

# 두 수의 대소비교
# == 서로 같다, 크다, 작다

n1 = 100
n2 = 60

if n1 == n2:
    print(f'{n1} == {n2}')
elif n1 > n2:
    print(f'{n1} > {n2}')
else:
    print(f'{n1} <{n2}')
# if 문
# if True조건식:
#    실행할 문장




# 온라인 에디터
# https://www.onlinegdb.com/online_python_compiler

# 퀴즈 :
# 숫자를 입력받아서
# 숫자값이 3의 배수이면 3의 배수이다.
# 그렇지 않으면 3의 배수가 아니다.

'''
숫자를 입력해주세요 ? ...
3의 배수이다.
3의 배수가 아니다.
'''
# data= int(input('숫자를 입력해주세요 ? ...'))
#
# if (data%3) == 0:
#     print('3의 배수이다.')
# if (data%3) != 0:
#     print('3의 배수가 아니다.')


# 퀴즈 :
# 나이를 입력받는다.
# 나이에 따라서 서로 다른 메세지 출력
'''
당신의 나이를 입력해주세요? ...
~7 : 영유아
8 ~ 13 : 초등학생
14 ~ 16 : 중학생
17 ~ 19 : 고등학생
20 ~ : 성인
'''

age = int(input('당신의 나이를 입력해주세요...'))

if age <= 7:
    print('영유아')
elif age <=13:
    print('초등학생')
elif age <=16:
    print('중학생')
elif age <=19:
    print('고등학생')
else:
    print('성인')

print('if, elif 테스트 종료')
# 조건식에서 True가 되는 조건 =
# True, 0빼고 나머지숫자, 길이가 0이 아닌 (문자열, 튜플, 리스트, 딕셔너리)
# 조건식에서 False가 되는 조건
# = False, 0, '', None, [], (), {}

# if True:
# if 123:
# if '문자열':
#     print('무조건 실행')

# if None:
# if False:
# if 0:
# if '':
#     print('실행안됨')

# if ~ else ~


# if ~ elif ~ else 다중 조건문
# 입력받은 데이타가
# 0
# 양수
# 음수
# 숫자가 아니다
# inData = int(input('숫자를 입력하세요....'))
# if inData == 0:
#     print('0이다')
# elif inData>0:
#     print('양수이다.')
# else:
#     print('음수이다.')


# 띠 테스트
# 띠 = 태어난년도%12
# 원숭이, 닭, 개, 돼지, 쥐, 소, 범, 토끼, 용, 뱀, 말, 양
# (0  ........  11)
'''
태어난 년도를 입력하세요? 2009
당신은 소띠입니다.
'''
'''
result = 2009%12
animalList = ['원숭이', '닭', '개', '돼지',
              '쥐', '소', '범',
              '토끼', '용', '뱀', '말', '양']

'''

'''
if .. elif .. else 퀴즈
태어난 년도를 입력하세요 ...? 2009
-------------------
태어난 년도 : 2009
당신은 소띠입니다.
오늘의 운세:
  오늘은 독서하기에 좋은 날이다.

'''
print( '-'*10, '\n\n' )

# birth = int(input('태어난 년도를 입력하세요 ...?  '))
# animalList2 = ['원숭이띠', '닭띠', '개띠', '돼지띠',
#               '쥐띠', '소띠', '범띠',
#               '토끼띠', '용띠', '뱀띠', '말띠', '양띠']
# animal = birth%12
#
# if animal == 0:
#     print(animalList2[0])
# elif animal == 1:
#     print(animalList2[1])
# elif animal == 2:
#     print(animalList2[2])
# elif animal == 3:
#     print(animalList2[3])
# elif animal == 4:
#     print(animalList2[4])
# elif animal == 5:
#     print(animalList2[5])
# elif animal == 6:
#     print(animalList2[6])
# elif animal == 7:
#     print(animalList2[7])
# elif animal == 8:
#     print(animalList2[8])
# elif animal == 9:
#     print(animalList2[9])
# elif animal == 10:
#     print(animalList2[10])
# elif animal == 11:
#     print(animalList2[11])
#
# # 아래도 동일
# print( '당신은', animalList2[animal], '입니다. ' )


# 조건문안에 조건문

#아이디가 맞다면 => 패스워드 검사
'''
user_id = input('ID => ')
if (user_id == '가든'):
    user_pw = input('password =>')
    if (user_pw == '1234'):
        print('로그인 되었습니다')
        print(f'{user_id} 님 오늘도 좋은 하루!')
    else:
        print("failed to login")
else:
    print("failed to login")
print('end the test')

'''

# 숫자를 입력받아서
# 0, 양수, 숫자가 아니다.
# 입력받은 데이타가 숫자이면 데이터형 변경.
# 그렇지 않으면 메세지 출력
# 문자열.isdigit() : 문자열이 숫자이면 True

# -----------------------------------------
# ----------------------------------------

#  in / not in 연산자
# 아이템 in 그룹(튜플, 리스트, 문자열, 집합) => True / False
# 아이템 not in 그룹(튜플, 리스트, 문자열, 집합) => True / False

numlist = [100, 400, 'python', 'JAVA']
sample = '가나다라마바사'
print(100 in numlist) # True
print(100 not in numlist) # False
print('가' not in sample) # False
print('강' in sample) # False

# 문자가 문자열에 있는가?
# print('a' in 'banana')  # True

# 값이 리스트에 있는가?
'''
myList = [100, 200, 300]
print(100 in myList) # True
'''

# if문에 in/not in 연산자 사용하기
# if item in group(리스트,튜플,문자열,집합) :
#   명령문


# if item in group(리스트,튜플,문자열,집합) :
#   명령문1
# else:
#   명령문2

bts = ['지민', '뷔', 'RM']
svt = ['조슈아', '승관', '도겸']

print('='*50)
member = '도겸'
if member in bts:
    print(f'{member} => BTS')
elif member in svt:
    print(f'{member} => SVT')
else:
    print(member)

#bmi 값에 따라 다음과 같은 메세지를 출력하세요
'''
# 키를 입력해주세요... 단위 cm...175
# 체중을 입력해주세요... 단위 kg...67
# bmi = 21.8776
# 정상
'''


# bmi 공식
# k = 키(입력값) 단위 cm
# w = 체중(입력값)
# bmi = 체중(kg)/키(m)의제곱, 키의 단위는 미터(m)

# bmi 값에 따라 출력되는 메세지
# 고도 비만 : 35 보다 클 경우
# 중등도 비만  : 30 - 35 미만
# 경도 비만 : 25 - 30 미만
# 과체중 : 23 - 25 미만
# 정상 : 18.5 - 23 미만
# 저체중 : 18.5 미만

k = int(input('키를 입력해주세요... 단위 cm...'))
w = int(input('체중을 입력해주세요...단위 kg...'))
k2= k/100
bmi = w/(k2**2)
print(f'{bmi:.4f}')

if bmi > 35:
    print('고도 비만')
elif bmi >= 30:
    print('중등도 비만')
elif bmi >= 25:
    print('경도 비만')
elif bmi >= 23:
    print('과제중')
elif bmi >= 18.5:
    print('정상')
else:
    print('저체중')

print('bmi 테스트 종료')
# if.. elif..else.. 문에 in/not in 연산자 사용하기
# if item in group(리스트,튜플,문자열,집합) :
#   명령문1
# elif item in group(리스트,튜플,문자열,집합) :
#   명령문2
# else:
#   명령문3



# pass 키워드 이용하기
# 명령문의 일종으로 비실행
# 함수, 클래스 생성시 등록만 시킬때 사용

pocket = ['paper', 'money', 'cellphone']
if 'card' in pocket:
    pass
elif 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")




# 입력받은 데이터에 따라 양수, 음수, 숫자가 아니다 출력
# 입력받은 데이타가 0인 경우에는 메세지를 출력하지 않는다.
# 문자열변수.strip() : 좌우공백 삭제
# 입력받은 데이타가 2글자 이상인 경우
# 첫번째 글자와 나머지 글자 찍기


'''
myNumber = input('데이타를 입력하세요').strip()
if len(myNumber)>=2 :
    print(myNumber[0],'\n\t', myNumber[1:] )
print('-'*30)

if myNumber[0]=='-' and myNumber[1:].isdigit():
    print('음수')
elif myNumber == '0':
    pass
elif myNumber.isdigit():
    print('양수')
else:
    print('숫자가 아니다')

'''

