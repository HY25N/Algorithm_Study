import sys
input = sys.stdin.readline

N = int(input())
word = list(input().strip())                # 후위표기식

values = [int(input()) for _ in range(N)]   # 피연산자 값

stack = []      # 후위표기식을 계산할 스택

for ch in word:
    if 'A' <= ch <= 'Z':
        stack.append(values[ord(ch) - ord('A')])

    else:
        b = stack.pop()
        a = stack.pop()

        if ch == '+':
            stack.append(a + b)

        elif ch == '-':
            stack.append(a - b)
        
        elif ch == '/':
            stack.append(a / b)
        
        elif ch == '*':
            stack.append(a * b)

print(f"{stack[0]:.2f}")