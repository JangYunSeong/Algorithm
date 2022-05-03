n,k = map(int,input().split())
array =[]
for i in range(n):
    array.append(int(input()))
start = 0
end = max(array) * k
while start<=end:
    mid = (start+end) //2
    total = 0
    for i in array:
        total += mid//i
    if total >= k:
        end = mid-1
        result = mid
    else:
        start = mid+1
print(result)