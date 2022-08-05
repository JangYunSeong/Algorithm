n,m=map(int,input().split())
array = list(map(int,input().split()))
start = max(array)
end = sum(array)
answer = 0
while start<=end:
    mid = (start+end)//2
    count = 1
    temp = mid
    for tape in array:
        if temp >= tape:
            temp -= tape
        else:
            count+=1
            temp = mid-tape
    if count <=m:
        end = mid-1
        answer = mid
    else:
        start = mid+1
print(answer)