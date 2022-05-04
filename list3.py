n = int(input())
board = []
for i in range(n):
    board.append(list(map(int,input().split())))
moves = list(map(int,input().split()))
stack = []
cnt=0
for order in moves:
    for i in range(n):
        index = board[i][order-1]
        if index==0:
            pass
        else:
            board[i][order-1] = 0
            stack.append(index)
            if len(stack) <2:
                pass
            else:
                if stack[-2] == stack[-1]:
                    cnt+=2
                    stack.pop()
                    stack.pop()
            break
print(cnt)
