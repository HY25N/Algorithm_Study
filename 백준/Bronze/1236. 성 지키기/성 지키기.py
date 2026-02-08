import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [input().strip() for _ in range(N)]

row = 0
col = 0

for i in range(N):
    if "X" not in lst[i]:
        row += 1

for j in range(M):
    guard = False

    for i in range(N):
        if lst[i][j] == "X":
            guard = True
            break

    if not guard:
        col += 1

print(max(row, col))