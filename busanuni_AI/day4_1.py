#--------------------------------------------

# 1~100 사이의 합 구하기
tot = 0
for i in range(1, 101):
    print(i, end= ' ')
    tot += i
print(f'\n\n 1~100까지의 합은? {tot}')

# 중첨 for 문
# 점선 출력 후 문단 5번 찍기 3번 반복
for i in range(3):
    print('='*30)
    for j in range(5):
        print(f'{j} => Hello World')

print('#'*40)
for i in range(3):
    print('='*30)
    for j in range(5):
        print(f' {j} => Hello world ')

# 2~9 단 출력하기
for i in range(2, 10):
    print(f'\n{i} 단')
    for j in range(1, 10):
        print(f'{i} x {j} => {i*j}')

# 1-50 사이의 숫자 중에서 3, 8, 9의 배수만 출력
for i in range(1, 51):
    if (i%3 == 0) or (i%8 == 0) or (i%9 == 0):
        print(i, end= ' ')

# 입력 데이타로 리스트 생성
# 리스트 길이는 5개로

'''
myList = []
print()
for i in range(5):
    data = input('데이타 입력 => ')
    myList.append(data)
print(f'\n\n 리스트 => {myList}')
'''
# 퀴즈1 : 별찍기
'''
*
**
***
****
*****
'''

for i in range(1, 6):
    print('*'*i)

for i in range(5):
    print()
    for j in range(0, i+1):
        print('*', end= " ")

# 퀴즈2 : 별찍기
'''
*****
****
***
**
*
'''

for i in range(5,0,-1):
    print('*'*i)

# 리스트 for = 리스트 내포
# 리스트 안에 for 문이 내포된 형태r
# 결과값으로 구성된 리스트가 생성된다.
# 리스트변수 = [ 결과값 for 명령문 if 명령문2]
# ['col-1', 'col-2',...'col-10']
resultList1 = []
for i in range(1,10):
    if i%3 == 0:
        resultList1.append(i)
print(f'\n\n 결과 = {resultList1}')

resultList2 = [i for i in range(1,101) if i%3 == 0]
print(f'\n\n 결과2 = {resultList2}')

# 1~15 사이의 숫자중에서 4의 배수는 제외하고 리스트로 생성하여라
resultList1 = []
for i in range(1,16):
    if i%4 != 0:
        resultList1.append(i)
print(f'\n\n 결과 = {resultList1}')

# or

resultList2 = [i for i in range(1,16) if i%4 != 0]
print(f'\n\n 결과2 = {resultList2}')

resultList = []
for i in range(1,11):
    resultList.append('col-' + str(i))
print(resultList)

# 리스트내포방식 이용 리스트변수 = [결과값 for 명령문]
resultList2 = ['col-' + str(i) for i in range(1,11)]
print(resultList2)

# 아래와 같은 형태로 리스트를 만들어라
# ['*', '**', '***', ... '******']
resultList = []
for i in range(1,11):
    resultList.append('*'* (i))
print(resultList)

# 두 번째 방식 - 리스트 for 이용
resultList2 = ['*'* i for i in range(1,11)]
print(resultList2)

# 리스트 다중 for
# 리스트안에 이중 for문이 있는 형태
# 리스트변수 = [ 결과값 for 명령문1  for 명령문2 ]
resultList1 = []
for i in range(1,4):
    for j in range(1,4):
        resultList1.append('col-'+str(i) + '-' + str(j))
print(resultList1)

# 두번째 방식- 리스트forfor
resultList2 = ['col-' + str(i) + str(j) for i in range(1,4) for j in range(1,6)]
print(resultList2)

# 퀴즈1
# 3단의 결과값에서 -1 한 값으로 리스트를 만들어라
# [ 2, 5, 8, ...]
resultList3 = [int(3*j-1) for j in range(1,10)]
print(resultList3)

resultList1 = []
for i in range(1,10):
    resultList1.append(3*i-1)
print(resultList1)

# 퀴즈2
# 구구단의 결과값으로 리스트를 만들어라
# [ 2, 4, .... , 63, 72, 81]
resultList4 = [(i*j) for i in range(2,10) for j in range(1,10)]
print(resultList4)

resultList1 = []
for i in range(2,10):
    for j in range(1,10):
        resultList1.append(i*j)
print(resultList1)

