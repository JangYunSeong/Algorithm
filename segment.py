import math

def init(start,end,index):
    if start == end:
        node[index] = array[start]
    else:
        mid = (start+end)//2
        init(start,mid,2*index)
        init(mid+1,end,2*index+1)
        node[index] = node[2*index] + node[2*index+1]

def update(start,end,pos,idx,value):
    if start==end==idx:
        node[pos] = value
        return node[pos]
    if idx<start or idx>end:
        return 0
    else:
        mid = (start+end)//2
        update(start,mid,2*pos,idx,value)
        update(mid+1,end,2*pos+1,idx,value)
        node[pos] = node[2*pos] + node[2*pos+1]
def query(start,end,left,right,pos):
    global answer
    if start>left or end<right:
        return
    if start<=left and right<=end:
        answer+=node[pos]
        return
    else:
        mid = (start,end) // 2
        query(start,mid,left,right,2*pos)
        query(mid+1,end,left,right,2*pos+1)
        return


array = [10,2,7,6,1,3,9,21]
node = [0] * (2**int(math.ceil(math.log2(len(array)))+1))
print(node)
init(0,len(array)-1,1)
print(node)