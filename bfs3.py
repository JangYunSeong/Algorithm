n = int(input())
s = []
visit = [[False]*n for i in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    s.append(list(input()))
count = 0
num = []
a = 0

def dfs(x,y):
    s[x][y] = a
    visit[x][y] = True
    global count
    count += 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if xx >= n or yy >=n or xx<0 or yy<0:
            continue
        if s[xx][yy] == "0":
            continue
        if visit[xx][yy] == False:
            dfs(xx,yy)
for i in range(n):
    for j in range(n):
        if s[i][j] == "1" and not visit[i][j]:
            a +=1
            dfs(i,j)
            num.append(count)
            count = 0
num.sort()
print(len(num))
for i in num:
    print(i)