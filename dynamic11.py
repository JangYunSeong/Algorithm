#11053번
n = int(input())
array = list(map(int,input().split()))
dp = [1] * 1001
for i in range(1,n):
    for j in range(i):
        if array[j]<array[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))