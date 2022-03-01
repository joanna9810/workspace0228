# 한줄주석  (ctrl+/)

# 여러줄 주석 기능 : 인용부호 3개 이용
'''
 여러줄 주석1
 여러줄 주석2
'''
"""
 여러줄 주석1
 여러줄 주석2
"""
print('주석문 이용')


# 출력문
# print(값/수식/변수) 문
# 쉼표를 이용한 출력문
# print(값/수식/변수, 값/수식/변수 )
# print(값/수식/변수, end='대체문자나 공백') 문


print(100)
print('출력문1')
print('출력문2')
print( '100 + 200 + 500 = ', 100+200+500 )
print( '출력문1', 45, '출력문2' )

# Hello , 영희 , 철수
print('Hello', end=' , ')
print('영희', end=' , ')
print('철수')


# Hello       영희        철수
print('Hello', end='      ')
print('영희', end='     ')
print('철수')


# 이스케이프 코드란?
# \n 개행, \t 여백
# \\ (\표시)
# \', \" (인용부호표시)

# 영희야 3줄 공백 처리후 놀자
print("영희야")
print()
print()
print()
print("놀자")
print("영희야\n\n\n놀자")
print("\t\t철수야\t놀자")
print("철수야! \\ 놀자")   # 철수야! \ 놀자
print("\"철수야!\" 놀자")  # "철수야!" 놀자

print('==== 퀴즈 ====')
# 퀴즈 :
# 아래와 같이 3줄로 글자를 출력하는 4가지 방법은?
'''
파이썬
파이썬
파이썬
'''
# 문자열*숫자 => 문자열을 숫자만큼 반복
print('='*50 )

# 첫번째 스타일
print('파이썬')
print('파이썬')
print('파이썬')
print('='*50 )

# 두번째 스타일 - 이스케이프 문자 이용
print('파이썬\n파이썬\n파이썬')

print('='*50 )

# 세번째 스타일 - * 이용 => 문자열*숫자
print('파이썬\n'*3)
print('='*50 )

# 네번째 스타일 - 쉼표 이용 + 이스케이프
print(' 파이썬\n','파이썬\n', '파이썬\n')

print('='*50 )
# 다섯번째 스타일
# 여러줄로 문자열 지정방식 = 인용부호 3개 이용
print('''파이썬 
파이썬
파이썬
''')






