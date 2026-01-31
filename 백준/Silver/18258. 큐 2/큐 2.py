import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque()
result = []

for _ in range(N):
    o = input().split()

    if o[0] == "push":
        queue.append(int(o[1]))

    elif o[0] == "pop":
        result.append(queue.popleft() if queue else -1)

    elif o[0] == "size":
        result.append(len(queue))

    elif o[0] == "empty":
        result.append(0 if queue else 1)

    elif o[0] == "front":
        result.append(queue[0] if queue else -1)

    elif o[0] == "back":
        result.append(queue[-1] if queue else -1)

print("\n".join(map(str, result)))
