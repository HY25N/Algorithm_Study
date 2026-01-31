import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
q = deque(range(1,N+1))
result = []

while len(q) > 1:
    result.append(q.popleft())  # 버리기
    q.append(q.popleft())       # 아래로 이동하기

result.append(q.popleft())      # 마지막 카드

print(" ".join(map(str, result)))