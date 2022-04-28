'''
for 반복문과 문자열 연산을 사용하여 다음과 같이 출력한다.

*
**
***
****
*****
******
*******
********
*********
**********
'''

N = int(input())
for i in range(N):
    for j in range(1+i):
        print("*", end="") # i + 1 만큼 별 출력, end 로 줄 바꿈 없이 이어서
    print("") # 다 출력하면 줄 바꿈

print("-"*50)

for i in range(N):
    print('{:<5}'.format("*"*(i+1)))

'''
for 반복문과 문자열 연산을 사용하여 다음과 같이 출력한다.

**********
*********
********
*******
******
*****
****
***
**
*
'''
J = int(input())
for i in range(J,0,-1):
    for j in range(i):
        print('*', end='')
    print('')
