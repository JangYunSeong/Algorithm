num = int(input())
array = []
array.append([1]*10)
array[0][0] = 0
for i in range(1,num):
    array.append([0]*10)
for i in range(1,num):
    array[i][0] = array[i-1][1]
    array[i][9] = array[i-1][8]
    for j in range(1,9):
        array[i][j] = array[i-1][j-1] + array[i-1][j+1]
print(sum(array[num-1])%1000000000)