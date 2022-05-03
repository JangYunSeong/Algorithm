array = list(input().split())
n = len(array)
total = len(set(array))
start = 0
end = 0
index = len(array)+1
result = [0,0]
while True:
    if total == 1:
        result = [1,1]
        break
    if start>n-total and end>=n:
        break
    else:
        if end-start >= total:
            if len(set(array[start:end])) == total:
                if index > end-start-1:
                    index = end-start-1
                    result = [start+1,end]
                start+=1
            elif len(set(array[start:end])) < total:
                end+=1
            if end >n:
                start+=1
        else:
            end+=1
print(result)