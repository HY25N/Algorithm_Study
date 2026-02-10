import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
skill = list(map(int, input().split())) # 사용 기술들 (1,2,3번)
skill.reverse() # 기술을 역순으로 추적

dq = deque()

for i, s in enumerate(skill, start=1):
    if s == 1:                  # 카드 i를 맨 위(앞)에 놓음
        dq.appendleft(i)

    elif s == 2:                # 카드 i를 위에서 두 번째 위치에 놓음
        top = dq.popleft()      # 현재 덱의 맨 앞 원소를 잠시 추출
        dq.appendleft(i)        # 새 카드(i)를 맨 앞에 삽입
        dq.appendleft(top)      # 아까 빼둔 top을 다시 맨 앞에 삽입 (top = 1번째, i = 2번째)

    elif s == 3:                # 카드 i를 맨 아래(뒤)에 놓음
        dq.append(i)

print(*dq)