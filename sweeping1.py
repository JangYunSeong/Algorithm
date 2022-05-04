import sys
li = []

ans = 0
n = int(input())

for i in range(n):
    start, end = map(int, sys.stdin.readline().split()) # 입력때문에 시간초과 났음
    li.append((start, end))
li.sort()
prevStart, prevEnd = li[0][0], li[0][1]
for i in range(1, n):
    start, end = li[i][0], li[i][1]
    if start <= prevEnd:
        prevEnd = max(prevEnd, end)
    else:
        ans+=prevEnd-prevStart
        prevStart, prevEnd = start, end

ans+=prevEnd-prevStart

print(ans)