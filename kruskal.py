def find(sets,x):
    k = x
    while True:
        if sets[k] == k:
            return k
        else:
            k = sets[k]

n = int(input())
array = []
m =0
for i in range(n):
    array.append(list(map(int,input().split())))
    for k in range(2):
        if m < array[i][k]:
            m = array[i][k]
a = m
array.sort(key=lambda x:x[2])
print(array)
sets = {i:i for i in range(1,a+1)}
length = 0
for i in array:
    print(sets)
    if find(sets,i[0]) == find(sets,i[1]):
        print("cycle")
        pass
    else:
        print(i[2])
        length += i[2]
        a = find(sets,i[0])
        b = find(sets,i[1])
        if a > b:
            sets[b] = sets[a]
        else:
            sets[a] = sets[b]
print(length)