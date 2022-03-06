# ------------------------------------------------

# 딕셔너리
# CRUD : Create Read Update Delete
# 딕셔너리 생성 - 초기값 지정
# 딕셔너리변수 = {키1:값1, 키2:값2,...}
# 키값은 문자형, 숫자형 둘다 가능 - 위치로 접근 못함-> 슬라이싱 못함

dic1 = {} # {} <class 'dict'> 0
dic2 = {'a' : 'apple', 'b' : 'banana', 'c' : 'cat'} # 키값이 문자 {'a': 'apple', 'b': 'banana', 'c': 'cat'} <class 'dict'> 3
dic3 = { 100: 'hundred', 200: 'two hundred'} # 키값이 숫자 {100: 'hundred', 200: 'two hundred'} <class 'dict'> 2
print(dic1, type(dic1), len(dic1))
print(dic2, type(dic2), len(dic2))
print(dic3, type(dic3), len(dic3))

# 딕셔너리 생성 - 빈 딕셔너리 생성 후 값 추가
# 딕셔너리 요소 추가
# 딕셔너리변수[키값]=값

# 딕셔너리 요소 조회 : 키인덱싱
# 딕셔너리변수[키값] => 해당요소의 값 표시

dic5 = {'a' : 'apple', 'b' : 'banana', 'c' : 'cat', 100: 'hundred', 200: 'two hundred'} # {'a': 'apple', 'b': 'banana', 'c': 'cat', 100: 'hundred', 200: 'two hundred'} <class 'dict'> 5
print(dic5, type(dic5), len(dic5))
print(['a'], dic5[100])

# 리스트, 튜플처럼 숫자 인덱싱이 가능할까?
# KeyError : 딕셔너리는 키값으로만 호출가능
# print(dic5[0])

# 리스트, 튜플처럼 슬라이싱이 가능할까?
# TypeError 딕셔너리는 슬라이싱이 불가능
# print(f'dict3[0:2] = {dict3[0:2]}')

# 딕셔너리 중복키는 가능할까요?
# 값은 같아도 되지만 키값이 중복되면 마지막 키값만 유효하다
dic4 = {'a' : 'apple', 'b' : 'banana', 'c' : 'cat', 'a': 'app'},
print(dic4,type(dic4), len(dic4)) # ({'a': 'app', 'b': 'banana', 'c': 'cat'},) <class 'tuple'> 1

# 딕셔너리 값 교체
# 딕셔너리[키값]=값
print('='*50)
dict6 = {'a' : 'apple', 'b' : 'banana', 'c' : 'cat', 100: 'hundred', 200: 'two hundred'}
print(dict6,type(dict6), len(dict6))
# 값 교체 => 숫자 위치 값으로 접근을 못하지만 키을 집적 입력하면서 바꿀 수 있음
dict6['a'] = 'application'
print(dict6,type(dict6), len(dict6))

# 새로운 요소 추가
dict6['d'] = 'drag'
print(dict6, len(dict6))

# 딕셔너리 요소 삭제
# 딕셔너리변수.clear()]
print('='*50)
dict7 = {'a' : 'apple', 'b' : 'banana', 'c' : 'cat', 100: 'hundred', 200: 'two hundred'}
print(dict7)
# 딕셔너리변수.pop(키값)
dict7.pop('b')
print(dict7)
# del 딕셔너리변수
# del 딕셔너리변수[키값]



# 딕셔너리 함수
# 딕셔너리변수.values() : 값 만 표시
# 딕셔너리변수.keys() : 키값만 표시
# 딕셔너리변수.items() : 튜플스타일로 표시 (키, 값)... 많이 쓰이진 않음!
dict8 = {'a' : 'algorithm', 'b' : 'banana', 'c' : 'cat', 100: 'hundred', 200: 'two hundred'}
print('='*50)
print(dict8, type(dict8))
print(dict8.values(), type(dict8.values())) # dict_values(['algorithm', 'banana', 'cat', 'hundred', 'two hundred']) <class 'dict_values'>
print(dict8.keys(),type(dict8.items())) # dict_keys(['a', 'b', 'c', 100, 200]) <class 'dict_items'>
# 리스트 변환 list(), 튜플로 변환 tuple()
print((list(dict8)), type(list(dict8))) # ['a', 'b', 'c', 100, 200] <class 'list'>
print(list(dict8.values()), type(list(dict8.values()))) # ['algorithm', 'banana', 'cat', 'hundred', 'two hundred'] <class 'list'>
print(dict8.keys(),type(dict8.items()))

# 딕셔너리에서 키값만 리스트로 만들어서 마지막 키값 조회

# 캐스팅
# 딕셔너리 => 리스트

# 리스트 => 딕셔너리
# 값만 모아서 리스트로 생성
# list(딕셔너리변수) => 키값만으로 생성된 리스트


# 리스트 => 딕셔너리(인덱싱숫자가 키값이 된다)
# 리스트 => enumerate(리스트,문자열,튜플)
#   => dict(enumerate(리스트,문자열,튜플))
# dict()
# enumerate(리스트,문자열,튜플)
print('='*50)
fruitList = ['banana', 'grapes', 'orange']
print(fruitList, type(fruitList)) #['banana', 'grapes', 'orange'] <class 'list'>
# print(enumerate(fruitList))  <enumerate object at 0x7f89c8023c00> -> 컴퓨터에 담겨진 주소번지 숫자들
temp = enumerate(fruitList)
fruitList = dict(temp) #dictionary-nized
print(fruitList, type(fruitList)) #{0: 'banana', 1: 'grapes', 2: 'orange'} <class 'dict'>
# : 리스트,문자열,튜플 같은 자료형을 enumerate 객체로 반환
# enumerate 객체의 요소는 딕셔너리 스타일. 키값은 숫자로 표시

# 딕셔너리 => 문자열
# str(딕셔너리변수) => {...}
# 구분자.join(딕셔너리변수) => 키값으로 생성된 문자열
myDict2 = {'a' : 'algorithm', 'b' : 'banana', 'c' : 'cat'}
myString = str(myDict2)
print(myString, type(myString)) # {'a': 'algorithm', 'b': 'banana', 'c': 'cat', 100: 'hundred', 200: 'two hundred'} <class 'str'>
print(myString[0], myString[0:5], myString[-1]) # { {'a': }

# 딕셔너리에서 값만 추출해서 문자열로 생성
print('+'*50)
myString2 = ' '.join(myDict2)
myString3 = ' / '.join(myString2)
print(myString2, type(myString2)) # a b c <class 'str'>
print(myString3, type(myString3)) # a /   / b /   / c <class 'str'>

# 딕셔너리에서 값만 추출해서 문자열로 생성
myString4 = ' / '.join(myDict2.values())
print( myString4 , type(myString4))  # app / banana / cat / drag <class 'str'>

# tuple => dictionary
# dic(enumerate(tuple))
mytuple = (100, 200, 300)
myDict = dict(enumerate(mytuple))
print('=' *50)
print(myDict, type(myDict))

# 딕셔너리 값만 => 튜플  tuple(딕셔너리명.values())
# 딕셔너리 키만 => 튜플  tuple(딕셔너리명.keys())
# tuple(딕셔너리) => 키값으로 구성된 튜플 생성
myDict2 = {'a' : 'algorithm', 'b' : 'banana', 'c' : 'cat', 100: 'hundred', 200: 'two hundred'}
mytupleA = tuple(myDict2.values()) # ('algorithm', 'banana', 'cat', 'hundred', 'two hundred') <class 'tuple'>
mytupleB = tuple(myDict2.keys()) # ('a', 'b', 'c', 100, 200) <class 'tuple'>
print(mytupleA, type(mytupleA))
print(mytupleB, type(mytupleB))

# 튜플 변경은? ('a', 's', 'c', 'd', 'y')
# 딕셔너리 값으로만 이루어진 튜플 생성

# 딕셔너리 리스트
# 리스트안에 딕셔너리가 있는 구조
dictList = [{'a':'apple', 'v':'victory'},
            {100:'백', 200:'이백'},
            {'user1':'김철수', 'user2':'고소영'}]

# 문자열 => 리스트
# 문자열 => 튜플
txt1 = '가나다라마바사'
mylist1 = list(txt1)
mytuple1 = tuple(txt1)
print(mylist1, type(mylist1)) # ['가', '나', '다', '라', '마', '바', '사'] <class 'list'>
print(mytuple1, type(mytuple1)) # ('가', '나', '다', '라', '마', '바', '사') <class 'tuple'>

#문자열 => 딕셔너리 dict(enumerate(문자열))
myDict1 = dict(enumerate(txt1))
print(myDict1, type(myDict1)) #{0: '가', 1: '나', 2: '다', 3: '라', 4: '마', 5: '바', 6: '사'} <class 'dict'>
#------------------------------
# 집합
# {값1, 값2, 값3....}
# CRUD :
# Create
# Read(전체조회만 가능)
# Update Delete
# 집합의 생성
# 집합변수 = set(리스트/문자열/튜플)

s1 = set([ 100, 200, 300])
s2 = set(( 5, 4, 3, 2, 1))
s3 = set('도레미파솔')
print(s1, type(s1)) #{200, 100, 300} <class 'set'>
print(s2, type(s2)) # {1, 2, 3, 4, 5} <class 'set'>
print(s3, type(s3)) # {'도', '파', '레', '미', '솔'} <class 'set'>

# 비어있는 집합
s4 = set()
print(s4, type(s4)) # set() <class 'set'>

# 순서가 없다. 랜덤하게 출력된다.
# 인덱싱이 불가능하다. 슬라이싱 불가능하다.
# 중복값을 허용할까요? => 1개만 표시
s5 = {1, 2, 3, 1, 1, 2, 100}
print( s5, type(s5)) # {1, 2, 3, 100} <class 'set'>

# 집합의 요소 추가
# 집합변수.add(값)
# 집합변수.update([값1, 값2...])
s6 = set()
print(s6, len(s5)) # set() 4
s6.add( 'python')
s6.add( 'mimi')
s6.add( 'chichi')
print(s6, len(s6)) # {'mimi', 'python', 'chichi'} 3 순서 없이 랜덤하게 출력
s6.update(['ai', 'db', 'love'])
print(s6, len(s6)) # {'love', 'chichi', 'python', 'mimi', 'ai', 'db'} 6

#값으로 삭제
s6.remove('mimi') # 특정 값을 삭제
print(s6, len(s6))
s6.pop() # 랜덤하게 삭제
print(s6)
# 집합의 요소 삭제
# 집합변수.remove(값)

# del 집합변수 => 메모리에서 삭제

# 집합의 연산
# +, * => 불가능

# 집합 합치기 = 합집합
# 집합변수3 = 집합변수1|집합변수2
# 집합변수3 = 집합변수1.union(집합변수2)

# 차집합
# 집합변수3 = 집합변수1-집합변수2
# 집합변수3 = 집합변수1.difference(집합변수2)


# 교집합
# 집합변수3 = 집합변수1&집합변수2
# 집합변수3 = 집합변수1.intersection(집합변수2)

# 대칭차집합 = 합집합-교집합
# 집합변수3 = 집합변수1^집합변수2
# 집합변수3 = 집합변수1.symmetric_difference(집합변수2)

setA = {'호랑이', '토끼', '돼지'}
setB = {'사자', '토끼', '돼지', '펭귄', '여우'}
print(f' 합집합 = {setA|setB} {setA.union(setB)}') # 합집합 = {'돼지', '토끼', '호랑이', '사자', '여우', '펭귄'} {'돼지', '토끼', '호랑이', '사자', '여우', '펭귄'}
print(f' 차집합 = {setA-setB} {setA.difference(setB)}') # 차집합 = {'호랑이'} {'호랑이'}
print(f' 교집합 = {setA&setB} {setA.intersection(setB)}') # 교집합 = {'토끼', '돼지'} {'토끼', '돼지'}
print(f' 대칭차집합 = {setA^setB} {setA.symmetric_difference(setB)}') # 대칭차집합 = {'펭귄', '호랑이', '사자', '여우'} {'펭귄', '호랑이', '사자', '여우'}

# 캐스팅
# 집합 => 리스트 list()
# list(집합변수)
# 집합 => 튜플 tuple()
# 집합 => 딕셔너리 dict(enumerate())
# 집합 => 문자열 str(), '구분자'.join()

setC = {'펭귄', '호랑이', '사자', '토끼', '여우', '돼지'}
listC = list(setC)
tupleC = tuple(setC)
dictC = dict(enumerate(setC))
print('='*50)
print(listC, type(listC)) # ['펭귄', '호랑이', '돼지', '여우', '토끼', '사자'] <class 'list'>
print(tupleC, type(tupleC)) # ('펭귄', '호랑이', '돼지', '여우', '토끼', '사자') <class 'tuple'>
print(dictC, type(dictC)) # {0: '돼지', 1: '토끼', 2: '여우', 3: '펭귄', 4: '사자', 5: '호랑이'} <class 'dict'>

print('='*50)
txtC1 = str(setC)
txtC2 = '=='.join(setC)
print(txtC1, type(txtC1)) # {'토끼', '펭귄', '돼지', '사자', '여우', '호랑이'} <class 'str'>
print(txtC2, type(txtC2)) # 토끼==펭귄==돼지==사자==여우==호랑이 <class 'str'>

# 퀴즈1
# number_list에서 중복 숫자를 제거한 후 리스트를 만들어서 출력하여라.
# number_list = [ 5, 1, 2, 2, 3,4, 5, 6, 7, 6, 7, 8, 9, 9, 10, 10 ]
# 결과 => [ .... ]

number_list = [ 5, 1, 2, 2, 3,4, 5, 6, 7, 6, 7, 8, 9, 9, 10, 10 ]
s1 = set(number_list)
print(f'결과 => {list(s1)}')

# 퀴즈2
# 두 집합의 중복 값으로 리스트를 생성하여라.
# set1 = { '쥬만치', '정글북', '타이타닉', '월E', 'ET' }
# set2 = { '타이타닉', '아바타', '에일리언', '스타워즈', '쥬만치'}
# 결과 => [ .... ]

set1 = { '쥬만치', '정글북', '타이타닉', '월E', 'ET' }
set2 = { '타이타닉', '아바타', '에일리언', '스타워즈', '쥬만치'}
print(f' 결과=> {list(set1&set2)} ')

# 퀴즈3
# 퀴즈 3의 결과 리스트를 다음과 같이 구분자 '/'를 이용한 문자열로 출력하여라.
# 결과 =>  ? / ? / ....

result = list(set1&set2)
print(f'결과 => {" / ".join(result) }')

# 연산자 정리
# 문자열, 튜플, 리스트 => +(연결), *(반복)
# 집합 => |, &, -, ^

txt1 = 'hello'
txt2 = 'python'
print(txt1 + txt2, ' / ', txt1*3)
t1 = (1, 2, 3)
t2 = (100, 200, 300)
print(t1 + t2, ' / ', t1*3)

# 인덱싱 정리
# 인덱싱, 슬라이싱 => 리스트, 튜플, 문자열열
# 키인덱싱 => 딕셔너리
# 인덱싱 x, 슬라이싱 x => 집합

# 값 변경 => 리스트, 딕셔너리
# 값 변경 x => 튜플, 집합

# 아이템 추가 => 리스트, 튜플, 딕셔너리
# 아이템 삭제 => 리스트, 딕셔너리, 집합
# 아이템 삭제 x => 튜플

# 캐스팅 : list(), tuple(), dict(), enumerate(), split(), str*(, ''.join()

# 문자열 => 리스트 list(문자열), 문자열.split()
txt3 = 'abcdefg'
txt4 = 'a b c d e f g'
result1 = list(txt3)
result2 = list(txt4)
print(result1, len(result1)) #['a', 'b', 'c', 'd', 'e', 'f', 'g'] 7
print(result2, len(result2)) # ['a', ' ', 'b', ' ', 'c', ' ', 'd', ' ', 'e', ' ', 'f', ' ', 'g'] 13
result3 = txt3.split()
result4 = txt4.split()
print(result3, len(result3)) # ['abcdefg'] 1 -> 공백이 없는 한덩어리 이기 때문에 하나로 리스트가 만들어짐
print(result4, len(result4)) # ['a', 'b', 'c', 'd', 'e', 'f', 'g'] 7 -> 공백이 있어서 사이로 쪼개짐, 공백이 한칸 이상이어도 결과는 같음
# tuple(집합변수)

# 리스트,문자열,튜플 => 집합
# set(리스트,문자열,튜플)







