from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = deque()
stack = []

for _ in range(N):
    button = input().split()

    if button[0] == '1':
        q.append(button[1])
        stack.append('back')
    
    elif button[0] == '2':
        q.appendleft(button[1])
        stack.append('front')

    else:
        if stack:
            pos = stack.pop()

            if pos == 'back':
                q.pop()
            else:
                q.popleft()

if q:
    print(''.join(q))
else:
    print(0)