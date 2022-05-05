
from collections import deque


def topology():
    result = []
    queue = deque()
    for i in range(1,v+1):
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        now = queue.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -=1
            if indegree[i] == 0:
                queue.append(i)
    for i in result:
        print(i, end = " ")
v,e = map(int,input().split())
indegree = [0] *(v+1)
graph = {i:[] for i in range(1,v+1)}
for i in range(e):
    a,b = map(int,input().split())
    graph[a] += [b]
    indegree[b]+=1
topology()
