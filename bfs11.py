from collections import deque

def dfs(x,y,cnt):
    queue = deque()
    queue.append((x,y,cnt))
    flag = 1
    while queue:
        if flag == 0:
            break
        x,y,cnt = queue.popleft()
        if cnt > 1:
            pass
        else:
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx<0 or nx>=5 or ny<0 or ny>=5:
                    continue
                if array[nx][ny] == "X":
                    continue
                if array[nx][ny] == "P":
                    flag = 0
                    break
                if array[nx][ny] == "O":
                    array[x][y] = "X"
                    queue.append((nx,ny,cnt+1))
    return flag                
array = []
person = []
result = 1
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(5):
    array.append(list(input()))
    for k in range(5):
        if array[i][k] == 'P':
            person.append((i,k,0))
for i in person:
    if dfs(i[0],i[1],i[2]) == 0:
        result = 0
print(result)