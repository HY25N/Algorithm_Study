import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
dq = deque()
moves = list(map(int, input().split()))

for i in range(len(moves)):
    dq.append((i+1, moves[i]))

while dq:
    num, move = dq.popleft()
    print(num, end = ' ')

    if move > 0:
        dq.rotate(-(move - 1))
    else:
        dq.rotate(-move)