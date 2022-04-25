import sys
n,k =map(int,input().split())
array = []
array = sorted([int(sys.stdin.readline()) for _ in range(n)])
start = 1
result = 0
end = array[-1]-array[0]
while start <=end:
    mid = (start + end) // 2
    index = 0
    count = 1
    for j in range(n):
        if (array[j]-array[index])>=mid:
            index = j
            count+=1
    if count < k:
        end = mid-1
    else:
        start = mid+1
        result = mid
print(result)