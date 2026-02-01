import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
q = deque(range(1,N+1))
result = []

while q:
    for _ in range(K-1):            # K-1번 동안 맨 앞의 숫자를 뒤로 보냄
        q.append(q.popleft())

    result.append(q.popleft())      # K번째 원소 제거, 결과값에 추가

print(f"<{", ".join(map(str, result))}>")