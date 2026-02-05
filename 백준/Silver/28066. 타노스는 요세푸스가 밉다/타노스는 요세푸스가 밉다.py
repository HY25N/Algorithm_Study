import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
q = deque(range(1, N+1))

while len(q) > 1:
    if len(q) < K:
        break
    q.append(q.popleft())
    for _ in range(K-1):
        q.popleft()

print(q[0])