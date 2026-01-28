import sys
input = sys.stdin.readline

N = int(input())
stack = []
result = []


for _ in range(N):
    x = input().split()

    if x[0] == '1':                     # push x
        stack.append(int(x[1]))

    elif x[0] == '2':                   # pop
        if stack:
            result.append(stack.pop())
        else:
            result.append(-1)
            
    elif x[0] == '3':                   # 크기(size)
        result.append(len(stack))

    elif x[0] == '4':                   # empty
        if stack:
            result.append(0)
        else:
            result.append(1)

    elif x[0] == '5':                   # top
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)

print("\n".join(map(str, result)))