from itertools import permutations

n = int(input())
numbers = list(map(int,input().split()))
oper = list(map(int,input().split()))
temp = '+'*oper[0] + '-'*oper[1]+'*'*oper[2] + '/'*oper[3]
temp = list(set(permutations(temp,n-1)))
array = []
for k in temp:
    result = numbers[0]
    for i in range(0,len(numbers)-1):
        if k[i] == "+":
            result += numbers[i+1]
        elif k[i] == "-":
            result -= numbers[i+1]
        elif k[i] == "*":
            result *= numbers[i+1]
        elif k[i] == "/":
            result = int(result/numbers[i+1])
        else:
            pass
    array.append(result)
print(max(array))
print(min(array))
