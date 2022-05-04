k = int(input())
array = list(map(int,input().split()))
table = {}
result = []
for i in array:
    if table.get(i) == None:
        table[i] = i+1
        result.append(i)
    else:
        k = table[i]
        temp = [k]
        while True:
            if table.get(k) == None:
                for i in temp:
                    table[i] = k+1
                table[k] = k+1
                result.append(k)
                break
            else:
                k = table[k]
                temp.append(k)
print(result)