from collections import deque
from itertools import combinations

dx = [-1,1,0,0]
dy = [0,0,-1,1]
n,m = map(int,input().split())
array = []
chicken = []
home = []
for i in range(n):
    array.append(list(map(int,input().split())))
    for k in range(n):
        if array[i][k] == 2:
            chicken.append((i,k))
        if array[i][k] == 1:
            home.append((i,k,0))
a = list(combinations(chicken,m))
result = []
for i in a:
    temp = 0
    for j in home:
        mins = 987654321
        for k in i:
            mins = min(mins, (abs(j[0]-k[0]) + abs(j[1]-k[1])))
        temp += mins
    result.append(temp)
print(min(result))