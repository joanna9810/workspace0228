n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1~10 까지 무게를 담을 수 있는 리스트
array = [0] * 11
for x in data:
    # 각 무게에 해당되는 데이터 카운트
    array[x] += 1
result = 0
# 1~m 까지의 각 무게에 대하여 처리
for i in range(1, m+1):
    n -= array[i] # 무게가 i 인 볼링공의 개수 제외 (A가 선택할 수 있는 개수)
    result += array[i] * n # B가 선택하는 경우의 수와 곱
print(result)