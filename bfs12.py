from collections import deque
from copy import deepcopy

def bfs(new,x,y,cnt,value):
    temp = 0
    queue = deque()
    queue.append((x,y,cnt,value))
    while queue:
        x,y,cnt,value = queue.popleft()
        if cnt >= 3:
            temp = max(temp, value)
            continue
        else:
            other = []
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue
                if new[nx][ny] == 0:
                    continue
                if new[nx][ny]>0:
                    other.append(new[nx][ny])
                    queue.append((nx,ny,cnt+1,value+new[nx][ny]))
                    new[nx][ny] = 0
            if len(other) == 4:
                other.sort()
                temp = new[x][y]+sum(other[1:])
            elif len(other) == 3:
                temp = new[x][y]+sum(other)
            else:
                pass
    return temp

dx = [-1,1,0,0]
dy = [0,0,-1,1]
n,m = map(int,input().split())
array = []
result = []
for i in range(n):
    array.append(list(map(int,input().split())))
for i in range(n):
    for k in range(m):
        new = deepcopy(array)
        value = new[i][k]
        cnt = 0
        result.append(bfs(new,i,k,cnt,value))
print(max(result))

        