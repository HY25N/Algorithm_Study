import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())            # N: 큐 크기, M: 뽑아야 할 숫자 개수
targets = list(map(int, input().split()))   # 뽑아야 할 숫자들

q = deque(range(1,N+1))         # 초기 큐 생성 (1부터 N까지)
cnt = 0                         # 연산 횟수 누적 변수

for x in targets:
    # 현재 큐에서 x가 몇 번째에 있는지(왼쪽으로 idx번 돌리면 x가 맨 앞으로 온다)
    idx = q.index(x)       

    if idx <= len(q) // 2:          # 왼쪽 회전이 더 적거나 같은 경우
        q.rotate(-idx)              # 왼쪽으로 idx번 회전
        cnt += idx
    else:
        q.rotate(len(q) - idx)  
        cnt += len(q) - idx    

    q.popleft()         # 맨 앞의 x 제거

print(cnt)