import sys
from collections import deque

input = sys.stdin.readline
q = deque()

N = int(input())
result = []

for _ in range(N):
    s = input().split()
    if s[0] == "1":
        q.appendleft(s[1])

    elif s[0] == "2":
        q.append(s[1])

    elif s[0] == "3":
        result.append(q.popleft() if q else -1)
        
    elif s[0] == "4":
        result.append(q.pop() if q else -1)
            
    elif s[0] == "5":
        result.append(len(q))

    elif s[0] == "6":
        result.append(0 if q else 1)

    elif s[0] == "7":
        result.append(q[0] if q else -1)

    elif s[0] == "8":
        result.append(q[-1] if q else -1)

print("\n".join(map(str, result)))