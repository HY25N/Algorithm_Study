import sys
from collections import deque

input = sys.stdin.readline

T = int(input())    # 테스트케이스

for _ in range(T):
    N, M = map(int, input().split())    # N: 문서 개수, M: 궁금한 문서
    P = list(map(int, input().split())) # 문서 중요도
    
    q = deque()
    for i in range(N):
        q.append((P[i], i))

    cnt = 0         # 출력 순서 카운트

    while True:
        current = q.popleft()   # 맨 앞 문서
        higher = False          # 현재 문서보다 더 중요한 문서 있는지 확인
        for doc in q:
            if doc[0] > current[0]:
                higher = True
                break

        if higher:              # 더 중요한 문서가 있을 경우 다시 뒤로 보냄
            q.append(current)

        else:
            cnt += 1

            if current[1] == M: # 찾는 문서일 경우 출력 후 종료
                print(cnt)
                break