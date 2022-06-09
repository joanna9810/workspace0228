# 연속된 숫자를 뒤집을 때 해야 하는 최소 행동 수 구하기
s = input()
now = int(s[0])
cnt = 0
for i in range(1, len(s)):
    num = int(s[i])
    if now != num:
        new = num
        cnt += 1
        if new == num:



print(cnt)

print('-'*50)
#
# from itertools import groupby
#
# def long_repleat(data):
#     return max([len(list(g)) for k, g in groupby(data)], default=0)

