n = int(input())
array = []
for i in range(n+1):
    array.append([0,0])
array[1][0] = 0
array[1][1] = 1
for i in range(2,n+1):
    array[i][0] = array[i-1][0] + array[i-1][1]
    array[i][1] = array[i-1][0]
print(sum(array[n]))