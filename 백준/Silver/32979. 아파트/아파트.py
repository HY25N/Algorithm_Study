import sys
from collections import deque

input = sys.stdin.readline

N = int(input())    # 참가자 수
T = int(input())    # 게임 횟수 (총 라운드)
a = deque(input().strip().split())          # 손바닥 쌓는 순서(아래 → 위)
b = list(map(int, input().strip().split())) # 각 라운드에서 부르는 숫자

result = []

for i in range(T):
    a.rotate(-(b[i] - 1))   # b[i]번째 손 찾기
    result.append(a[0])     # 가장 아래에 있는 손이 패배자

print(" ".join(result))