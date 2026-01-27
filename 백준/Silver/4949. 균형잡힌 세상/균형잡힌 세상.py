result = []                 # 각 문장 검사 결과 저장

while True:
    sentence = input()
    if sentence == ".":     # . 입력 시 전체 입력 종료
        break

    stack = []              # 괄호 '(' , '[' 저장용 스택
    valid = True            

    for s in sentence:
        if s == "(" or s == "[":
            stack.append(s)

        elif s == ")":
            if not stack or stack[-1] != "(":   # 짝이 맞지 않으면 False
                valid = False
                break
            stack.pop()
        
        elif s == "]":
            if not stack or stack[-1] != "[":   # 짝이 맞지 않으면 False
                valid = False
                break
            stack.pop()
            
        elif s == ".":      # 현재 문장 검사 종료
            break

    if valid and not stack:
        result.append("yes")
    else:
        result.append("no")

print("\n".join(result))