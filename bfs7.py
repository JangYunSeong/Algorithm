
from collections import deque


def bfs(cnt):
    queue = deque(tomato)
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while queue:
        x,y,cnt = queue.popleft()
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if xx<0 or xx>=m or yy<0 or yy>=n:
                continue
            if array[xx][yy] == -1:
                continue
            if array[xx][yy] == 0:
                array[xx][yy] =1
                queue.append((xx,yy,cnt+1))
    return cnt
n,m = map(int,input().split())
array = []
tomato = []
count = 0
for i in range(m):
    array.append(list(map(int,input().split())))
    for k in range(n):
        if array[i][k] == 1:
            tomato.append((i,k,count))
flag = 0
count = bfs(count)
for i in array:
    if 0 in i:
        print(-1)
        flag = 1
        break
if flag == 0:
    print(count)
