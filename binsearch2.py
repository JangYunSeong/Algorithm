
n,need = map(int,input().split())
array = []
for i in range(n):
    array.append(int(input()))

start = 1
end = max(array)
result = 0
while start<=end:
    total = 0
    mid = (start+end)//2
    for i in array:
        total += i//mid
    if total < need:
        end = mid-1
    else:
        start = mid+1
        result = mid
print(result)