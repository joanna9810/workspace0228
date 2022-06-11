n = int(input())
coins = list(map(str,input().split()))
max_coins = sum(int(coins))
for i in range(1, max_coins):
    if coins[i] != max_coins[i] or coins[i] != max_coins[i] + max_coins[i]:
        print(i)

