# 연속된 숫자를 뒤집을 때 해야 하는 최소 행동 수 구하기
s = input()
cnt0 = 0
cnt1 = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '0':
            cnt0 += 1
        elif s[i+1] == '1':
            cnt1 += 1

print(min(cnt0, cnt1))

print('-'*50)
#
# from itertools import groupby
#
# def long_repleat(data):
#     return max([len(list(g)) for k, g in groupby(data)], default=0)

