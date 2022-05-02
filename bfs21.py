
from collections import deque

def bfs():
    queue = deque()
    queue.append((0,0,0,0))
    while queue:
        x,y,dir,value= queue.popleft()
        newvalue = 0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                if nx==0 and ny==0:
                    continue
                if array[nx][ny] != 1:
                    if x ==0 and y == 0:
                        newvalue = value + 100
                    else:
                        if dir == i:
                            newvalue = value+100
                        else:
                            newvalue = value+600
                    if costs[nx][ny] == 0:
                        costs[nx][ny] = newvalue
                        queue.append((nx,ny,i,newvalue))
                    else:
                        if costs[nx][ny] >= newvalue:
                            costs[nx][ny] = newvalue
                            queue.append((nx,ny,i,newvalue))
        print(queue)
        for o in costs:
            print(o)
    return costs[n-1][n-1]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
n= int(input())
array = []
costs = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    array.append(list(map(int,input().split())))
print(bfs())
for o in costs:
    print(o)
