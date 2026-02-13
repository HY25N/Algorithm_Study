N = int(input())
lst1 = set(input().split())
lst2 = set(input().split())

result = lst1 - lst2
print(*result)