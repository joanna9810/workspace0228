# ------------------------------
# ------------------------------

# 반복문
# while 문
# for ... in
# for .. range()
# 다른 언어의 반복문 스타일 :
# for (i=0;i<10;i++)

# 반복문 : while
# while 조건:
#      실행명령
# 조건이 True 이면 명령을 실행해라

# hello world 를 n번 출력 하라
n = 1
while n <= 10:
    print(f'{n}: Hello world')
    n += 1 # 증감
print('while 테스트 종료')

# 10-1 까지 가로로 출력
n = 10 # 초기치
while n > 0:
    print(n, end=' ')
    n -= 1 # 증감
print('\n\nwhile 테스트 종료')

#퀴즈 1~100까지의 합 출력하기
n = 1 # 초기치
total = 0
while n<= 100:
    total += n
    n += 1 # 증감
print(f'1~100까지의 합은? {total}')
print('\n\nwhile 테스트 종료')

# while 문 + if 문
# 1~100 사이의 숫자중에서 5의 배수이거나 7의 배수이면 출력
n = 10 # 초기치
while n <= 100:
    if(n%5 == 0) or (n%7 == 0):
        print(n, end=' ')
    n += 1 # 증감
print('\n\nwhile 테스트 종료')

# 1~100 사이의 숫자중에서 3의 배수이거나 8의 배수로 구성된 리스트를 생성
numList = [] # 빈리스트 생성
n = 1
while n <= 40:
    if(n%3 == 0) or (n%8 == 0):
        numList.append(n)
    n += 1 # 증감
print(f'numList = {numList} 총갯수는? {len(numList)}')
print('\n\nwhile 테스트 종료')

# 퀴즈
# 1~20까지 숫자를 출력하여라. 한줄에 5개씩 출력하여라
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# ...
n = 1
while n<=20:
    if (n%5==0):
        print(n)
    else:
        print(n, end = ' ')
    n += 1 #왜 증강이 뒤로 빠지지?

print('+'*50)
n = 0
count = 0
while n < 20:
    n+=1
    count += 1
    print(n, end=' ')
    if (count%5)==0:
        print() # 개행
# 무한 루프
# while True:
#     명령문

# while True:
#     print('Python')

# while 조건:
#      실행명령
#      False 조건

# 초기값
# while False가 될 조건제시:
#      증감
#      실행명령

# 1~10까지 출력하여라

# 10~1까지 출력하여라


# 별찍기1
'''
*
**
***
****
*****
'''

# 1~50까지 짝수만 출력하기

# 퀴즈1 - 3단 출력하기
'''
3 X 1 = 3
3 X 2 = 6
...
3 X 9 = 27
'''


# 퀴즈2 - 1~100까지의 합 출력하기
# 1~100까지의 합은?


# while 문 이용해서 리스트 요소 출력하기
# list1 = ['사과', '바나나', '수박', '포도']

# 짝수번째 글자만 출력하기
# txt1 = '가나다라마바사'

# 문자열을 사선으로 출력하기
# txt2 = 'ABCDEFG'


# 가장 큰 수를 삭제하여라
# myNumList = [100, 200, 50, -30, 999, 10]
# 리스트명.remove(값)


# 가장 큰 수와 가장 작은 수를 삭제하여라


# ------------------------------
# ------------------------------

# 다중 while 문
# while 조건1:
#   while 조건2:
#       명령문2
#   명령문1

# 점선 출력후 문단 3번찍기 n번 반복하기

n1 = 1
n2 = 1
while n1 <= 3:
    print('-'*50)
    n2 = 1
    while n2 <= 3:
        print(n2)
        n2 += 1
    n1 += 1

# n 단 출력
n = 9
cnt = 1
print(f'{n} 단 출력')
while cnt <= 9:
    print(f'{n} x {cnt} = {n*cnt}')
    cnt += 1

# 2~9단 출력하기
n = 2
while n <= 9:
    print(f'\n{n}단 출력')
    cnt = 1
    while cnt <= 9:
        print(f'{n} x {cnt} = {n * cnt}')
        cnt += 1
    n += 1

# while 문을 이용한
# 리스트,딕셔너리,문단,집합,튜플 아이템 출력

# 문자열을 세로로 출력하여라
print('='*50)
txt = 'abcdefg'

i = 0
while i<len(txt):
    print('='*(i+2) + txt[i])
    i += 1

# 퀴즈
# 아래와 같이 문자열을 출력하여라
# txt = 'abcde'
'''
                a
            b
        c
    d
e
'''
print('='*50)
txt = 'abcdefg'

i = 0
while i < len(txt):
    print(' '*(7-i) + txt[i])
    i += 1

# 선생님 해답
print('=' * 50)
txt = 'abcde'
i = 0 # 인덱스
count = len(txt) # 공백

while i < len(txt):
    print(('  ' * count) + txt[i])
    i += 1
    count -= 1
# 다른 친구 해답
txt = 'abcde'
i = 0
while i < len(txt):
    # print(len(txt)-1-i, i)
    print(('    '*(len(txt)-1-i)) + txt[i])
    i += 1
# while 문 이용해서 리스트 요소 출력하기
# 인덱싱위치 번째 요소는 인덱싱위치의값
# list1 = ['사과', '바나나', '수박', '포도']

'''
0 번째 요소는  사과
1 번째 요소는  바나나
2 번째 요소는  수박
3 번째 요소는  포도
'''
fruitList = ['banana', 'apple', 'strawberry','orange']
print(fruitList[0])

i = 0
while i < len(fruitList) :
    print(f'{i}번째 요소는 {fruitList[i]}')
    i += 1
# 짝수번째 글자만 출력하기
# txt1 = '가나다라마바사'

# 딕셔너리 구조에서 키와 값을 분리시켜서 출력하기
# a => africa
# s => say
# c => coffee
# d => drama
# y => yes

# dict1 = {'a': 'africa', 's': 'say', 'c': 'coffee', 'd': 'drama', 'y':'yes'}


# 리스트에서 가장 큰 값을 구한 후 삭제하여라
# 리스트에서 요소 삭제
# 리스트변수.pop() : 마지막 삭제
# 리스트변수.pop(인덱싱값) : 인덱싱값에 해당하는 아이템 삭제
# 리스트변수.remove(값) : 값에 해당하는 아이템 삭제

# myNumList = [100, 200, 50, -30, 999, 10, 999]


# 중복값 제거하여 리스트 생성하기
# set() 활용

# 퀴즈 1
# 가장 큰 수와 가장 작은 수를 삭제하여라
# myNumList2 = [100, 200, 50, -30, 999, 10, -30]

# 퀴즈 2
# 딕셔너리 값에 'a' 글자가 있는 아이템만 표시하고 총 갯수 출력하기
# dict2 = {'a': 'africa', 's': 'say', 'c': 'coffee', 'd': 'drama', 'y':'yes'}
'''
'a': 'africa'
's': 'say'
'd': 'drama'
총 갯수는? 3
'''

# 딕셔너리 값에 'a' 글자가 있는 아이템만 표시하고 총 갯수 출력하기


# 퀴즈 3 :# 다음 문자열을 사선으로 한 글자씩 출력하여라
'''
H
  e
    l
      l
        o
'''

# ------------------------------
# ------------------------------


# break
# 반복문 안에서 사용
# 명령문 실행시 제어문에서 탈출한다.
# 명령문이 실행되면 하단 명령문들은 실행되지 않는다.
# 무한루프의 종료 조건시 사용
print('='*50)
n = 1
while n <= 5:
    print(n)
    if(n == 3):
        break
    n += 1
print('break 테스트 종료')

# continue
# 제어문 안에서 사용
# 명령문이 실행되면 하단 명령문들은 실행되지 않는다.

# 1~10 사이 숫자중에서 5를 제외하고 출력

n = 0
while n <= 9:
    n += 1
    if n == 5:
        continue
    print(n)


'''
count = 0
while count<2:
    print('Hello Python1')
    count += 1
    break
    print('Hello Python2')
'''

# 무한루프 + if + break
# while True조건:
#   if 블록을 빠져나갈 조건:
#      break

# x 또는 X 를 입력하면 종료
while True:
    ans = input('입력 => ')
    # 무한루프에서 탈출 조건
    if ans == 'x' :
        break
print('break 테스트 종료')

# 대소문자 상관없이 yes 입력시 종료
# yes, Yes, yES
# 입력값 모두 대문자 upper()
# 입력값 모두 소문자 lower()
word = 'Yes'
print(word, word.upper(), word.lower())

print('='*50)
while True:
    ans = input('입력 => ')
    # 무한루프에서 탈출 조건
    if ans.upper() == 'YES':
        break
print(' break 테스트 종료 ')
'''
while True:
    ans = input('아무값이나 입력. 종료시 x ....?  ').strip()
    # while 블록을 탈출하는 조건
    if ans == 'x':
        break

print('입력 종료')
'''

# 입력받은 값을 리스트에 추가한다.
# q 입력시 입력문 종료후 리스트 출력
# 리스트에 아이템 추가
# 리스트변수.append(값)
# 리스트변수.insert(인덱스,값)
# 빈 리스트 생성
'''
resultList = []
while True:
    item = input('리스트 추가 요소 입력 ... (q:종료)').strip()
    if item == 'q':
        break
    resultList.append(item)

print('무한루프 종료')
print('리스트 출력', resultList)
'''

# 1~10까지 숫자중에서 5만 빼고 출력하여라









