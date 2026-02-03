import sys
from collections import deque

input = sys.stdin.readline

n, m, L = map(int, input().split())    # n = 트럭 수, m = 다리 길이, L = 다리의 최대하중
q = deque(map(int, input().split()))
bridge = deque([0] * m)                # 다리 길이를 공간으로 구현
time = 0

while True:
    time += 1                           # 1초 경과 (트럭이 한 칸 이동)
    bridge.popleft()

    if not sum(bridge) and not q:       # 다리 위에 트럭 없고, 대기 트럭 없음 → 종료
        break
    
    elif q and sum(bridge) + q[0] <= L: # 대기 트럭 있고, 다리 하중을 넘지 않으면 트럭 진입
        bridge.append(q.popleft())

    else:
        bridge.append(0)

print(time)