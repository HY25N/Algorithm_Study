for i in range(int(input())):
    n = input().split()

    print(f"Case #{i+1}: {' '.join(n[::-1])}")

# 2026-01-25 (재풀이)
N = int(input())

for i in range(N):
    L = input().split()
    reversed_L = L[::-1]
    print(f"Case #{i+1}: {' '.join(reversed_L)}")
