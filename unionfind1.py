def find(x):
    if parent[x]==x:
        return x
    parent[x] = find(parent[x])
    return parent[x]
def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        parent[b]= a
    else:
        parent[a] = b
answer = "YES"
n = int(input())
m = int(input())
parent = [i for i in range(n+1)]
for i in range(1,n+1):
    temp = list(map(int,input().split()))
    cnt = 1
    for k in temp:
        if k == 1:
            union(i,cnt)
        cnt+=1
route = list(map(int,input().split()))
start = find(route[0])
for k in route[1:]:
    if find(k) != start:
        answer="NO"
        break
print(answer)