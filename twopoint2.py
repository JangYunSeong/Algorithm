gems = list(input().split())
n = len(gems)
kind = len(set(gems))
index = len(gems)+1
dic = {gems[0] : 1}
start = 0
end = 0
result = [0,n-1]
while start<n and end<n:
    if len(dic) < kind:
        end+=1
        if end==n:
            break
        dic[gems[end]] = dic.get(gems[end],0)+1
    else:
        if (end-start-1) < index:
            index = end-start-1
            result = [start,end]
        if dic[gems[start]] ==1:
            del dic[gems[start]]
        else:
            dic[gems[start]]-=1
        start+=1
result[0]+=1
result[1]+=1
print(result)