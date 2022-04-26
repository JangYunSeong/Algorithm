#9095번
n = int(input())
num = [1,2,3]
result = []
for i in range(n):
    temp = int(input())
    dp = [0]*(temp+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for k in range(4,temp+1):
        dp[k] = dp[k-1]+dp[k-2]+dp[k-3]
    result.append(dp[temp])
for i in result:
    print(i)