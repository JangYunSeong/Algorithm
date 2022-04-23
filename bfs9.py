def dfs(x,y,color):
    if x<0 or x>=size or y<0 or y>=size:
        return False
    index = array[x][y]
    if visit[x][y] == 0 and index == color:
        visit[x][y] = 1
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            dfs(xx,yy,color)
        return True
    return False

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visit = []
size = int(input())
array = []
count = 0
count_d = 0
for i in range(size):
    array.append(list(input()))
    visit.append([0] * size)
for i in range(size):
    for j in range(size):
        if dfs(i,j,array[i][j]) == True:
            count+=1
print(count)
visit = []
for i in range(size):
    visit.append([0] * size)
    for j in range(size):
        if array[i][j] == "G":
            array[i][j] = "R"
for i in range(size):
    for j in range(size):
        if dfs(i,j,array[i][j]) == True:
            count_d+=1
print(count_d)