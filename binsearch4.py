
n = int(input())
array = list(map(int,input().split()))
array.sort()
start = 0
end = n-1
limit = array[start]+array[end]
while start<end:
    mid = array[start] + array[end]
    if abs(mid) <= abs(limit):
        limit = mid
        min = start
        max = end
    if mid >= 0:
        end -=1
    else:
        start+=1
print(array[min],array[max])