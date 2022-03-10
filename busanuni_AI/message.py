def hello():
    for i in range(10):
        print(f'{i+1} => Hello world')

hello()

# message.py 에 gugu(n) 함수 정의
# 해당 숫자에 대한 구구단 출력
def gugu(n):
    for i in range(1,10):
        print(f'{n} x {i} = {n*i}')