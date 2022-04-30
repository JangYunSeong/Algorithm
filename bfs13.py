
from collections import deque
from copy import deepcopy

def bfs(x,y,cnt):
    queue =deque()
    queue.append((x,y,cnt))
    new[x][y] = 'W'
    while queue:
        x,y,cnt = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if new[nx][ny] == "L":
                new[nx][ny] = 'W'
                queue.append((nx,ny,cnt+1))
    return cnt

dx = [-1,1,0,0]
dy = [0,0,-1,1]
n,m = map(int,input().split())
array = []
land = []
for i in range(n):
    array.append(list(input()))
    for k in range(m):
        if array[i][k] == 'L':
            land.append((i,k,0))
result = []
for i in land:
    new = deepcopy(array)
    result.append(bfs(i[0],i[1],i[2]))
print(max(result))