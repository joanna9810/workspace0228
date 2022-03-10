# 모듈 테스트1
# message.py (hello 함수 정의)
# day5_3.py (message.py에 정의된 hello함수 호출)

# 1) message.py 파일 생성
# hello() 함수 정의
# 2) 모듈 import 선언
# import 모듈 이름
# 모듈이름. 함수(인자)
# message.py 플러그인
import message

# 3) 함수 호출
# 모듈 이름. 함수(인자)
# message.py 에 정의된 hello() 함수 호출
message.hello()
# message.py 에 정의된 gugu(n) 함수 호출
message.gugu(13)

# 모듈의 호출방법 2
# import 모듈이름 as 별칭(alias)
# 호출된 모듈의 함수 호출방법2
# 별칭.함수(인자)
# day5_3.py (message.py에 정의된 hello, gugu 함수 호출)
# 1) 모둘을 별칭으로 지정
import message as m
# 2) 모듈안의 함수 호출
m.gugu(7) # 별칭. 함수

# 모듈의 호출방법 3
# from 모듈이름 import 모듈함수
# 호출된 모듈의 함수 호출방법3
# 모듈함수(인자)

# 1) 모둘 함수 명으로 임포트
# message.py안의 hello, gugu 함수 사용 선언
from message import hello, gugu
# 2) 함수명으로만 호출
gugu(5)
hello()

# package?
# 폴더안의 모듈 (파이썬 파일)
# a 폴더안에 aa.py 안에 aaa() 함수 정의
# a 폴더(패키지) => aa.py(모듈) => aaa()함수

# 임포트
# import 패키지명.모듈명
# import 패키지명.모듈명 as 별칭
# from 패키지명.모듈명 import 함수수

# a 패키지 안의 aa 모듈 임포트 선언
import a.aa
from a.aa import aaa
# a 패키지안의 aa 모듈안에 선언된 aaa() 함수 호출
aaa()

