n = int(input())
dp = [0] * 101
result = []
dp[1] = 1
dp[2] = 1
dp[3] = 1
for i in range(n):
    temp = int(input())
    for i in range(4,temp+1):
        dp[i] = dp[i-3] + dp[i-2]
    result.append(dp[temp])
for i in result:
    print(i)