n = int(input())
seen = set()

for _ in range(n):
    s = input().strip()
    r = s[::-1]

    # 회문이면 즉시 정답
    if s == r:
        print(len(s), s[len(s)//2])

    if r in seen:
        print(len(s), s[len(s)//2])

    seen.add(s)