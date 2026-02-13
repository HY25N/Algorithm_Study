N, M = map(int, input().split())

count = {}

for _ in range(N):
    K = int(input())
    students = input().split()
    
    for s in students:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1

result = 0

for v in count.values():
    if v >= M:
        result += 1

print(result)