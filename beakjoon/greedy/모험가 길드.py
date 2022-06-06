n = int(input()) # 모험가 수
group = list(map(int, input().split())) # 모험가들의 두려움 강도
group.sort() # 두려움 강도 오름차순 정렬

cnt = 0 # 그룹 당 사람 수 세는 바구니
result = 0 # 그룹 수 세는 바구니
for i in group: # group 안의 모험가들의 두려움 강도를 하나하나 밟을 계단
    cnt += 1
    if cnt >= i: # 두려움 강도 만큼의 인원이 차면
        result += 1 # 그룹 수 카운트
        cnt = 0 # 바구니 비우기
print(result)

