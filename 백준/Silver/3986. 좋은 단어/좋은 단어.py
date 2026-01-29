import sys
input = sys.stdin.readline

N = int(input())
result = 0

for _ in range(N):
    stack = []
    v = input().rstrip()

    for c in v:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    if not stack:
        result += 1

print(result)