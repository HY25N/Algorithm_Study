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