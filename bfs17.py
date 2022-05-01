
from sys import setrecursionlimit


def dfs(x,y):
    if x<0 or x>=m or y<0 or y>=n:
        return False
    if array[x][y] == 1:
        array[x][y] = 0
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            dfs(nx,ny)
        return True
    return False
dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,1,-1,-1,1]
result = []
setrecursionlimit(10**6)
while True:
    n,m = map(int,input().split())
    if n == 0 and m==0:
        break
    array= []
    cnt = 0
    for i in range(m):
        array.append(list(map(int,input().split())))
    for i in range(m):
        for j in range(n):
            if dfs(i,j) == True:
                cnt+=1
    result.append(cnt)
for k in result:
    print(k)