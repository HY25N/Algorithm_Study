N = int(input())

for _ in range(N):
    s = input().strip()
    stack = []
    valid = True    # 논리값

    for ch in s:
        if ch == '(':
            stack.append(ch)
        else :
            if not stack:   # 스택이 비어있을 경우
                valid = False
                break
            stack.pop()
    if valid and not stack: # 중간에 실패 없고 '('가 남지 않음
        print("YES")
    else:
        print("NO")