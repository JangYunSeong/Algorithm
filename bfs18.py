
from collections import deque


def bfs():
    queue = deque(tomato)
    cnt = 0
    while queue:
        x,y,z,cnt = queue.popleft()
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]
            if nx <0 or nx>=m or ny<0 or ny>=n or nz<0 or nz>=h:
                continue
            if array[nz][nx][ny] == -1:
                continue
            if array[nz][nx][ny] == 0:
                array[nz][nx][ny] = 1
                queue.append((nx,ny,nz,cnt+1))
    return cnt

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,1,-1]
n,m,h = map(int,input().split())
array = []
tomato = []
for i in range(h):
    temp = []
    for j in range(m):
        temp.append(list(map(int,input().split())))
        for t in range(n):
            if temp[j][t] == 1:
                tomato.append((j,t,i,0))
    array.append(temp)
result = bfs()
flag = 0
for i in range(h):
    for j in range(m):
        if 0 in array[i][j]:
            result = -1
            break
print(result)