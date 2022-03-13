def bfs(graph, start_node):
    visit = list()
    queue = list()
    result = ""
    queue.append(start_node)
    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            if(node not in graph.keys()):
                break
            else:
                queue.extend(sorted(graph[node]))
    for i in visit:
        result += (str(i) + " ")
    result = result[:-1]
    return result

def dfs(graph, start_node):
    visit = list()
    stack = list()
    result = ""
    stack.append(start_node)
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            if(node not in graph.keys()):
                break
            else:
                stack.extend(reversed(graph[node]))
    for i in visit:
        result += (str(i) + " ")
    result = result[:-1]
    return result


edge, vertex, start = map(int,input().split())
array = {}
for i in range(0,vertex):
    e,v = map(int,input().split())
    array[e] = array.get(e, []) + [v]
    array[v] = array.get(v, []) + [e]
for k in array.keys():
    array[k].sort()
print(dfs(array,start))
print(bfs(array,start))