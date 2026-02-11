import sys
from collections import deque

input = sys.stdin.readline

N, K, M = map(int, input().split())
q = deque(range(1,N+1))
direction = 1                           # 1: 시계 방향, -1: 반시계 방향
count = 0                               # 제거된 사람 수

while q:
    if direction == 1:                  # 시계 방향
        q.rotate(-(K-1))
        print(q.popleft())

    else:                               # 반시계 방향 (뒤에서 K번째 사람 제거)
        q.rotate(K-1)
        print(q.pop())

    count += 1

    if count % M == 0:                  # M명 제거 후 방향 전환
        direction *= -1