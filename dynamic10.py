#2579번
n = int(input())
array = []
dp = [0] * 301
for i in range(n):
    array.append(int(input()))
dp[1] = array[0]
if n>1:
    dp[2] = array[0] + array[1]
for i in range(3,n+1):
    dp[i] = max(dp[i-3]+array[i-2],dp[i-2]) + array[i-1]
print(dp[n])