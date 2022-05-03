from collections import deque
from copy import deepcopy
from itertools import combinations

def bfs(new):
    queue = deque(virus)
    cnt = len(virus)
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if new[nx][ny] == 1:
                continue
            if new[nx][ny] == 2:
                continue
            if new[nx][ny] == 0:
                new[nx][ny] = 2
                cnt+=1
                queue.append((nx,ny))
    return cnt
dx = [-1,1,0,0]
dy = [0,0,-1,1]
n,m = map(int,input().split())
array = []
blank = []
virus = []
wall = 0
for i in range(n):
    array.append(list(map(int,input().split())))
    for k in range(m):
        if array[i][k] == 0:
            blank.append((i,k))
        elif array[i][k] == 2:
            virus.append((i,k))
        else:
            wall+=1
case = list(set(combinations(blank,3)))
result = []
for i in case:
    new = deepcopy(array)
    for k in i:
        new[k[0]][k[1]] = 1
    result.append(n*m-wall-3-bfs(new))
print(max(result))
