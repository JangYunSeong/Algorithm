def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        if friend[a-1]<friend[b-1]:
            parent[b] = a
            #friend[b-1] = friend[a-1]
        else:
            parent[a] = b
            #friend[a-1] = friend[b-1]
n,m,cost=map(int,input().split())
friend=list(map(int,input().split()))
parent=[i for i in range(0,n+1)]
for i in range(m):
    start,end=map(int,input().split())
    union(start,end)
cnt=1
answer= 0
for i in parent[1:]:
    if cnt==parent[i]:
        answer+=friend[i-1]
    cnt+=1
if answer > cost:
    answer = "Oh no"
print(answer)