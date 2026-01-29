S = input().rstrip()                # 입력 끝의 공백 문자 제거(\n)
stack = []                          # 단어 뒤집기, 문자 저장
result = []                         # 최종 결과
tag = False                         # < > 태그 여부

for c in S:
    # 태그 시작
    if c == "<":
        # 태그 시작 전 stack에 단어가 있으면 뒤집어서 결과에 추가
        if stack:
            result.append("".join(stack[::-1])) 
            stack.clear()
        tag = True                  # 태그 진입
        result.append(c)            # '<'는 그대로 출력

    #태그 끝
    elif c == ">":
        tag = False                 # 태그 종료
        result.append(c)            # '>' 그대로 출력

    # 태그 안
    elif tag == True:
        result.append(c)            # 태그 안 문자 그대로 출력

    # 태그 밖
    else:
        # 공백일 경우, 단어 하나 끝
        if c == " ":
            result.append("".join(stack[::-1]))
            stack.clear()
            result.append(" ")      # 공백 그대로 유지
        else:
            stack.append(c)

# 문자열 끝났는데 stack에 남아있는 단어 처리
if stack:
    result.append("".join(stack[::-1]))

print("".join(result))