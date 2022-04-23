from collections import deque

def bfs(count,start):
    counts = 0
    flag = 0
    queue = deque()
    queue.append((start,counts))
    while queue:
        v,cnt = queue.popleft()
        if v not in visit:
            visit.append(v)
            if cnt == count:
                flag = 1
                print(v)
            if v not in array.keys():
                break
            else:
                for i in array[v]:
                    queue.append((i,cnt+1))
                counts = cnt +1
    if flag == 0:
        print(-1)
n,m,k,start = map(int,input().split())
array = {}
visit = []
for i in range(m):
    e,v = map(int,input().split())
    array[e] = array.get(e,[]) + [v]
    array[v] = array.get(v,[]) + [e]
bfs(k,start)