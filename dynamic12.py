from math import factorial

#1932번
n = int(input())
array = []
count = 0
for i in range(n):
    array.append(list(map(int,input().split())))
for i in range(1,n):
    for k in range(len(array[i])):
        if k == 0:
            array[i][k] += array[i-1][0]
        elif k == len(array[i])-1:
            array[i][k] += array[i-1][k-1]
        else:
            array[i][k] += max(array[i-1][k-1],array[i-1][k])
print(max(array[n-1]))