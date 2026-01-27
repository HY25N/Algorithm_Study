s = input().strip()
stack = []
result = 0
prev = ""                       # 이전 문자 기억

for c in s:
    if c == "(":
        stack.append(c)

    else:                       # c == ")"
        stack.pop()
        if prev == "(":         # 레이저
            result += len(stack)
        else:                   # 막대기 끝
            result += 1

    prev = c

print(result)