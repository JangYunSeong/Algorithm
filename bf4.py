
import re
from itertools import permutations
from copy import deepcopy

def cal(x,y,oper):
    if oper == '+':
        return x+y
    if oper == '-':
        return x-y
    if oper == '*':
        return x*y
n = input()
temp = ['+','-','*']
oper = []
result = []
array = list(map(int,re.split('[-|+|*]',n)))
for i in n:
    if i in temp:
        oper.append(i)
opercnt = list(set(oper))
operlist = list(permutations(opercnt,len(opercnt)))
for cnt in operlist:
    newarr = deepcopy(array)
    newoper = deepcopy(oper)
    for opers in cnt:
        index = 0
        while True:
            if index >= len(newoper):
                break
            else:
                if opers == newoper[index]:
                    newarr[index] = cal(newarr[index],newarr[index+1],opers)
                    newarr.pop(index+1)
                    newoper.pop(index)
                else:
                    index+=1
    result.append(abs(newarr[0]))
print(max(result))