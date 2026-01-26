import sys
input = sys.stdin.readline

n = int(input())
stack = []
current = 1             # 1부터 시작
result = []             # +, - 연산 기록

for _ in range(n):
    x = int(input())    # 목표 숫자

    # 목표 숫자 x까지 push
    while current <= x:
        stack.append(current)
        current += 1
        result.append("+")

    # 스택 top이 x인 경우 pop        
    if stack and stack[-1] == x:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        exit()

print("\n".join(result))