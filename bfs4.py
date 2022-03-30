
from copyreg import constructor


def bfs(array,start_node):
    visit = list()
    queue = list()
    count = 0
    queue.append(start_node)
    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            if node not in array.keys():
                break
            else:
                queue.extend(sorted(array[node]))
                count += 1
    return count
edge = int(input())
vertex = int(input())
array = {}
for i in range(0,vertex):
    e,v = map(int,input().split())
    array[e] = array.get(e,[]) + [v]
    array[v] = array.get(v,[]) + [e]
print(array)
print(bfs(array,1)-1)

