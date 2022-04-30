
from collections import deque

def bfs(x,y,wall):
    queue = deque()
    queue.append((x,y,wall))
    visited[x][y][wall] = 1
    while queue:
        x,y,wall = queue.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][wall]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if array[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                queue.append((nx,ny,wall))
                visited[nx][ny][wall] = visited[x][y][wall] + 1
            if array[nx][ny] == 1 and wall == 1:
                queue.append((nx,ny,wall-1))
                visited[nx][ny][wall-1] = visited[x][y][wall] + 1
    return -1
dx = [-1,1,0,0]
dy = [0,0,-1,1]
n,m = map(int,input().split())
array = []
for i in range(n):
    array.append(list(map(int,input())))
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
cnt = 1
result = bfs(0,0,1)
print(result)