A, B = map(int, input().split())

num = 1
result = []

while len(result) < B:
    for _ in range(num):
        result.append(num)
    num += 1

print(sum(result[A-1:B]))