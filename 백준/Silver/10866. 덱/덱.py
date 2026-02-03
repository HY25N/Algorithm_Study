import sys
from collections import deque

input = sys.stdin.readline
q = deque()

N = int(input())
result = []

for _ in range(N):
    s = input().split()
    if s[0] == "push_front":
        q.appendleft(s[1])

    elif s[0] == "push_back":
        q.append(s[1])

    elif s[0] == "pop_front":
        result.append(q.popleft() if q else -1)
        
    elif s[0] == "pop_back":
        result.append(q.pop() if q else -1)
            
    elif s[0] == "size":
        result.append(len(q))

    elif s[0] == "empty":
        result.append(0 if q else 1)

    elif s[0] == "front":
        result.append(q[0] if q else -1)

    elif s[0] == "back":
        result.append(q[-1] if q else -1)

print("\n".join(map(str, result)))