
import sys


def dfs(x,y):
    global cnt
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if array[x][y] == 0:
        array[x][y] = 1
        cnt+=1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            dfs(nx,ny)
        return True
    return False

sys.setrecursionlimit(10**6)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
n,m,k = map(int,input().split())
array = [[0 for _ in range(m)] for _ in range(n)]
for i in range(k):
    start_x,start_y,end_x,end_y = map(int,input().split())
    for j in range(start_x,end_x):
        for k in range(start_y,end_y):
            array[k][j] = 1
result = []
count = 0
for i in range(n):
    for k in range(m):
        cnt = 0
        if dfs(i,k) == True:
            result.append(cnt)
            count+=1
result.sort()
print(count)
for i in result:
    print(i,end=" ")