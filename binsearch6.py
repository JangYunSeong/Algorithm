n,k = map(int,input().split())
array = list(map(int,input().split()))
start = 0
end = max(array)
answer = 0
while start <=end:
    mid = (start+end)//2
    count = 0
    result = 0
    for i in array:
        if i-mid<=0:
            count+=1
        else:
            if result<count:
                result = count
            count = 0
    if result<count:
        result = count
    if result < k:
        start = mid+1
    else:
        end = mid-1
        answer = mid
print(answer)