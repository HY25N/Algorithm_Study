# 2025-07-29
import sys
input = sys.stdin.readline

N = int(input())
sticks = [int(input()) for _ in range(N)]

count = 1
max_height = sticks[-1]

for i in reversed(range(N)):
    if sticks[i] > max_height:
        count += 1
        max_height = sticks[i]

print(count)

# 2026-01-24 해당 문제 재풀이
import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]

stack = []

for h in reversed(lst):
    if not stack or h > stack[-1]:
        stack.append(h)

print(len(stack))
