from collections import deque

def dfs(x,y,visit):
    # queue = deque()
    # queue.append((x,y,visit))
    queue = set([(x,y,visit)])
    
    result = 1
    while queue:
        # x,y,visit = queue.popleft()
        x,y,visit = queue.pop()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if array[nx][ny] == array[x][y]:
                continue
            if array[nx][ny] not in visit:
                queue.add((nx,ny,visit + array[nx][ny]))
                result = max(result,len(visit+array[nx][ny]))
    return result
dx = [-1,1,0,0]
dy = [0,0,-1,1]
n,m = map(int,input().split())
array = []
count = 0
for i in range(n):
    array.append(list(input()))
visit = array[0][0]
count = dfs(0,0,visit)
print(count)