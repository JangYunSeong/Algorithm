from copy import deepcopy
import sys
sys.setrecursionlimit(10**8)
def test(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    return False

def dfs(x,y,visit):
    visit[x][y] = 1
    global count
    for i in range(4):
        nx = x+dx[i]
        ny =y+dy[i]
        if test(nx,ny)==False:
            continue
        if visit[nx][ny] == 0 and array[nx][ny] == 0:
            dfs(nx,ny,visit)
            count+=1
dx = [-1,0,0,1]
dy = [0,1,-1,0]

n,m=map(int,input().split())
visit = [[0 for _ in range(m)] for _ in range(n)]
array = []
for i in range(n):
    array.append(list(map(int,input())))
result = []
for i in range(n):
    temp = ""
    for j in range(m):
        if array[i][j] == 0:
            temp+='0'
        else:
            count = 1
            visit_temp = deepcopy(visit)
            dfs(i,j,visit_temp)
            temp+=str(count)
    result.append(temp)
for i in range(n):
    print(result[i])