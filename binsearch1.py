def binary(array,rice,start,end):
    result = 0
    while start<=end:
        total = 0
        mid = (start+end)//2
        for i in array:
            if i > mid:
                total += i-mid
        if rice <= total:
            result = mid
            start = mid+1
        else:
            end = mid-1
    return result

n,rice=map(int,input().split())
array = list(map(int,input().split()))
print(binary(array,rice,0,max(array)))