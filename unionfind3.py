def find(x):
    if friend[x] == x:
        return x
    friend[x] = find(friend[x])
    return friend[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        friend[b] = a
        number[a] += number[b]
cnt = int(input())
for k in range(cnt):
    n=int(input())
    friend={}
    number={}
    for i in range(n):
        a,b=input().split()
        if a not in friend:
            friend[a] = a
            number[a] = 1
        if b not in friend:
            friend[b] = b
            number[b] = 1
        union(a,b)
        print(number[find(a)])
        
