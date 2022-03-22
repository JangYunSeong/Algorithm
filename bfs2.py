from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]
array = []
def dfs(x, y, row,col):
    global count
    if x== row and y == col:
        count +=1
        array.append(count)
        count = 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<row and 0<=yy<col and array[xx][yy] ==0:
                board[xx][yy] = 1
                count += 1
                dfs(xx,yy)
                board[xx][yy] = 0
row, col = map(int, input().split())
board = [0] * row
for i in range(0,row):
    tmp = list(map(int,input()))
    temp = []
    for j in range(0,col):
        temp.append(tmp)
    board[i] = temp
dfs(0,0,row,col)
print(count)