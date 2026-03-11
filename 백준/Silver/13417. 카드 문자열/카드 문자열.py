from collections import deque

N = int(input())

for _ in range(N):
    num = int(input())
    data = input().split()
    T = deque(data[0])

    for i in range(1, num):
        if data[i] <= T[0]:
            T.appendleft(data[i])
        else:
            T.append(data[i])

    print("".join(T))