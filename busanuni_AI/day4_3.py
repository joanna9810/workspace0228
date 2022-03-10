# 함수 정의 9
# 일반인자랑 가변인자랑 함께 있는 경우
# 주의 사항: 일반 인자는 앞쪽으로 배치. 가변 인자 *args는 뒷편에 배치
'''
def 함수명(인자, *args):
    인자와 args를 이용한 명령문...
    return 값/변수/수식/명령문
'''
# 호출
# 함수명(인자값, 가변값1)
# 함수명(인자값, 가변값1, 가변값2...)

def printSymbolNumber(symbol, *args):
    return print(f'{symbol} // {args}')

printSymbolNumber('##', 10)
printSymbolNumber('$$$$', 10, 20, 30)
'''
## // (10,)
$$$$ // (10, 20, 30)

'''
# 계산기호인자 값에 따라서 뒤의 가변인자값을 계산하여라
'''
# 함수 정의
def calChoice(계산기호인자, *args) :
    명령문

# 함수 호출
# calChoice('*', 20,30)
# 계산결과 = 곱 : 600
# calChoice('+', 20,30,50)
# 계산결과 = 합 : 100

'''






# 함수 정의 10
# 딕셔너리 가변인자 **kwargs
# 가변인자는 키=값
# 결과 데이터형이 딕셔너리
# kwargs = Keyword Arguments

'''
def 함수명(**kwargs):
    kwargs를 명령문...
    return 값/변수/수식/명령문
'''
# 호출
# 함수명(키1=값1)
# 함수명(키1=값1, 키2=값3 ...)

def printDict(**kwargs):
    return print(kwargs, type(kwargs))

printDict(key1='키1')
printDict(key1='키1', key2='키2')

# {'key1': '키1'} <class 'dict'>
# {'key1': '키1', 'key2': '키2'} <class 'dict'>

def printDict2(**kwargs):
    print('kwargs[key1] = {key1}'.format(**kwargs))
    print('kwargs[key2] = {key2}'.format(**kwargs))
    print(f'kwargs[key1] = {kwargs["key1"]}')

# printDict2(key1='키1') # kwargs[key] = 키1
printDict2(key1='키1', key2='키2')
# kwargs[key1] = 키1
# kwargs[key2] = 키2

def printDict3(**kwargs):
    for key in kwargs:
        print(f'{key} : {kwargs[key]}')
printDict3(key1='키1')
# key1 : 키1
printDict3(key1='키1', key2='키2')
# key1 : 키1
# key2 : 키2



# 함수 정의 11
# 초기값이 있는 딕셔너리 가변인자 **kwargs
# 가변인자는 키=값
# 결과 데이터형이 딕셔너리

# 학생 정보를 딕셔너리 구조로 생성하는 함수 정의
def stdInfo(**kwargs):
    print('\n 함수 호출')
    print(kwargs, type(kwargs))
    for key in kwargs:
        print(f'{key} => {kwargs[key]}')

# 함수호출
stdInfo(stdName='김철수', age=28, gender='남')
stdInfo(stdName='이영자', gender='여', addr='부산', job='개그맨')

# 주소록
def makeAddr(**kwargs):
    # 초기값 지정

    if 'nation' not in kwargs:
        kwargs['nation'] = '한국'
    for key in kwargs:
        print(f'{key} => {kwargs[key]}')
# 함수 호출
makeAddr(userName = 'chichi', addr = 'brisbane', job= 'phd student')
makeAddr(userName = 'chichi', addr = 'brisbane', job= 'phd student')
makeAddr(userName = 'chichi', addr = 'brisbane', nation= 'australia')
'''
def 함수명(**kwargs):
    # 초기값 지정
    kwargs[키값] = 값
    kwargs를 명령문...
    return 값/변수/수식/명령문
'''
# 호출
# 함수명(키1=값1)
# 함수명(키1=값1, 키2=값3 ...)
'''
st1 = {'nationality':'USA', 'age':33, 'name':'Jackson'}
st2 = {'nationality':'USA', 'age':22, 'name':'Maria'}
'''
# nationality 값이 고정
def makePerson(**kwargs):
    kwargs['nationality'] = 'USA'
    # return  print(kwargs)
    print('-'*20)
    for key in kwargs:
        print(f'{key} = {kwargs[key]}')

makePerson(age=33, name='Jackson')
makePerson(age=22, name='Maria')


'''
age = 33
name = Jackson
nationality = USA
--------------------
age = 22
name = Maria
nationality = USA
'''
makePerson(age=13, name='Sopia', nationality='Spain')
'''
age = 13
name = Sopia
nationality = USA
'''



# 아이템 in 그룹 / 아이템 not in 그룹
print('a' in 'banana') # True
print('a' not in 'banana') # False

# nationality 값이 함수 호출시 전달되는 값으로 변경
def makePerson2(**kwargs):
    if 'nationality' not in kwargs:
        kwargs['nationality'] = 'USA'
    print('-'*20)
    for key in kwargs:
        print(f'{key} = {kwargs[key]}')

makePerson2(age=33, name='Jackson')
'''
age = 33
name = Jackson
nationality = USA
'''
makePerson2(age=13, name='Sopia', nationality='Spain')
'''
age = 13
name = Sopia
nationality = Spain
'''



