import sys
input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    command = input().split()   # 명령어 입력

    if command[0] == "push":
        lst.append(int(command[1]))
    
    elif command[0] == "pop":
        if not lst:             # lst가 비어 있으면 -1 출력
            print(-1)
        else:                   # 아니면 lst[-1]값 출력 후 제거
            print(lst[-1])
            lst.pop()
    
    elif command[0] == "size":
        print(len(lst))         # 정수 개수 출력


    elif command[0] == "empty":
        if not lst:             # lst가 비어 있으면 1 출력
            print(1)
        else:                   # 아니면 0 출력
            print(0)

    elif command[0] == "top":
        if not lst:             # lst가 비어 있으면 -1 출력
            print(-1)
        else:                   # 아니면 lst[-1]값 출력
            print(lst[-1])