'''
주민번호는 다음과 같이 구성된다.
XXXXXX-XXXXXXX

왼쪽 6자리는 생년월일(YYMMDD)이고, 오른쪽 7자리는 성별,출생지역,확인코드로 구성되어있다.
주민번호를 입력받아 형태를 바꿔 출력해보자.

입력
주민번호 앞 6자리와 뒷 7자리가 '-'로 구분되어 입력된다.
(입력값은 가상의 주민번호이다.)
ex)110011-0000000

출력
'-'를 제외한 주민번호 13자리를 모두 붙여 출력한다.

참고
아무것도 없는 공(empty) 문자는 작은 따옴표(') 2개를 붙여서 '' 로 표현한다
'''

a, b = input().split('-')
print(a+b)