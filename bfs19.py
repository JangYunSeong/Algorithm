
from collections import deque


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if array[nx][ny] == 0:
                array[nx][ny] = array[x][y] + 1
                queue.append((nx,ny))

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,2,1,-1,-2]
result = []
k = int(input())
for a in range(k):
    n = int(input())
    array = [[0 for _ in range(n)] for _ in range(n)]
    start_x, start_y = map(int,input().split())
    end_x, end_y = map(int,input().split())
    bfs(start_x,start_y)
    if start_x == end_x and start_y == end_y:
        result.append(0)
    else:
        result.append(array[end_x][end_y])
for i in result:
    print(i)