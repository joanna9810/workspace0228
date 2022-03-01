# 변수 할당 방법
# 변수 = 수식 또는 값
# 서로 다른 변수에 동일한 값 할당

x = 100
y = 500
print('x = ', x)
print('y = ', y)
# 값 교체
y = 'Hell world'
print('y = ', y)


# 쉼표(,)를 이용한 변수 할당
# 변수1, 변수2 = 값1, 값2
print('='*50)
userName, user_age = '홍길동', 33
print(userName, user_age)

# 예약어라서 변수 설정 불가능
# True = '참'

# 파이썬의 예약어 출력하기
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist)) # 36

# 퀴즈 : user1, user2의 변수값을 서로 변경하여라
user1 = "영희"
user2 = "철수"
print('='*50)
print('user1 = ', user1)
print('user2 = ', user2)

# 중간변수 설정 (전통식)
temp = user1
user1 = user2
user2 = temp
print('='*50)
print('user1 = ', user1)
print('user2 = ', user2)

# 쉼표를 이용한 변수 교체 (파이썬만의 방식)
c


# 데이터형 확인하기
# type(변수/값)

# 자료형의 종류
# 기본자료형
# : 숫자형(정수, 실수)
# : 문자열형
# : 논리형 Boolean - True / False

# 집합자료형
# : 리스트, 튜플, 딕셔너리, 클래스, 집합

print('='*50)

x = 100
y = 3.14
z = True
myString = "abcd"
print('x = ', x, type(x))
print('y = ', y, type(y))
print('z = ', z, type(z))
print('myString = ', myString, type(myString))

# 산술연산자
# +, - , *, /, //(정수형 몫), %(나머지), **(제곱)
n1 = 33
n2 = 5
print(n1 , '+', n2, '=', n1+n2)
print(n1 , '-', n2, '=', n1-n2)
print(n1 , '*', n2, '=', n1*n2)
print(n1 , '/', n2, '=', n1/n2)
print(n1 , '//', n2, '=', n1//n2)
print(n1 , '%', n2, '=', n1%n2)
print(n1 , '**2 =', n1**2)

# 대입 연산자
# 변수명 += , -= , *= , /=
a = 1
print('*'*50)
print(a) # 1
a += 1   # a = a+1
print(a) # 2
a -= 6  # a = a-6
print(a) # -4

# 관계 연산자
# 결과값이 True / False
# ==, !=, >, <, >=, <=
x = 100
y = 10
z = 45
print(x == y, x != y ) # False True
print(x >= y, x < z ) # True False


# 논리 연산자
# 결과값이 True / False
# and, or, not
# 관계연산자를이용한수식1 논리 연산자 관계연산자를이용한수식2
# not(관계연산자를이용한수식)
print('='*50)
x = 100
y = 10
z = 45
print((x > y) and (x > z)) # True
print((x < y) and (x > z)) # False
print((x<y) or (x>z) ) # True
print((x<y) or (y>z) ) # False
print( x == 100, not(x == 100)) # True  False


# 입력문
# 변수명 = input(메세지)
# 입력받은 변수는 데이터형이 문자열이다.

# userName = input('이름을 입력하여주세요...')
# print(userName, '님 오늘도 좋은하루!!!!')

# 자료형 변환 - Casting
# int(값/수식/변수) : 정수형 데이터형으로 변환
# float(값/수식/변수) : 실수형 데이터형으로 변환
# str(값/수식/변수)  : 문자열 데이터형으로 변환
# bool(값/수식/변수)  : 논리형 데이터형으로 변환


# 나이를 입력받아서 출생년도를 출력하여라
# 나이(문자열) => 나이(정수형)
# 0 은 False, 나머지 숫자는 True
# userAge = int(input('나이를 입력해주세요... '))
# print(userAge, type(userAge), bool(userAge)) # 45 <class 'int'> True
# print(userAge, ' => 출생년도 ', 2022-userAge)

# 퀴즈 : 2개의 숫자값을 입력받은 후 사칙 연산을 수행하여라
'''
첫번째 숫자를 입력하세요... 10
두번째 숫자를 입력하세요... 20
---------
10 + 20 = ?
10 - 20 = ?
10 * 20 = ?
10 / 20 = ?
'''
num1 = int(input("첫번째 숫자를 입력하세요..."))
num2 = int(input("두번째 숫자를 입력하세요..."))
print("-----------")
print(num1, "+", num2, "=", num1 + num2)
print(num1, "-", num2, "=", num1 - num2)
print(num1, "*", num2, "=", num1 * num2)
print(num1, "/", num2, "=", num1 / num2)

num1 = int(input("첫번쨰 숫자를 입력하시오"))
num2 = int(input("두번쨰 숫자를 입력하시오"))
print(".............")
print(num1, '+', num2, '=', num1 + num2)