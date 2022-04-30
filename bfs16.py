
from collections import deque

def bfs(start,end):
    queue = deque()
    queue.append(start)
    while queue:
        start = queue.popleft()
        if start == end:
            print(time[start])
            return 
        for i in (start-1,start+1,start*2):
            if 0<=i<MAX and not time[i]:
                time[i] = time[start]+1
                queue.append(i)
MAX = 100001
time = [0] *MAX
start,end = map(int,input().split())
bfs(start,end)

