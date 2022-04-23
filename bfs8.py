from collections import deque


def bfs():
    queue = deque(virus)
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while queue:
        x,y,num,cnt = queue.popleft()
        if cnt == s:
            break
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if xx <0 or xx>=n or yy<0 or yy>=n:
                continue
            if array[xx][yy] !=0:
                continue
            if array[xx][yy] == 0:
                array[xx][yy] = array[x][y]
                queue.append((xx,yy,num,cnt+1))
    return array[s_x-1][s_y-1]        


n,k = map(int,input().split())
array = []
index = [0] * k
for i in range(n):
    array.append(list(map(int,input().split())))
s,s_x,s_y = map(int,input().split())
cnt = 0
virus = []
for i in range(n):
    for k in range(n):
        if array[i][k] !=0:
            virus.append((i,k,array[i][k],cnt))
virus.sort(key = lambda x:x[2])
print(bfs())