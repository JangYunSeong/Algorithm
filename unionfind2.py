import sys
sys.setrecursionlimit(10**6)
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]
def union(x,y):
    x=find(x)
    y=find(y)
    if x<y:
        parent[y] = x
    else:
        parent[x] = y
n,m = map(int,input().split())
result = []
parent = [i for i in range(0,n+1)]
for i in range(m):
    commend = list(map(int,input().split()))
    if commend[0] == 0:
        union(commend[1],commend[2])
    else:
        if find(commend[1]) == find(commend[2]):
            result.append("YES")
        else:
            result.append("NO")
for i in result:
    print(i)