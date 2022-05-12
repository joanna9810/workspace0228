# N가지 종류의 화폐와 가치의 합 M 원 입력 받기
n, m = map(int, input().split())
array = []
# N 줄 만큼 각 화폐의 가치 입력 받기
for i in range(n):
    array.append(int(input()))
# 한 번 계산된 결과를 저장하기 위한 dp 테이블 초기화
d = [10001] * (m+1)

# 다이나믹 프로그래밍 진행 (보텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[j]] != 10001: # (i-k) 방법이 존재하는 경우
            d[j] = min(d[j], d[j-array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 m 원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])
