N, B = input().split()
B = int(B)

location = len(N)-1
total = 0
for i in N:
    num = ord(i)
    if num < 65:
        num = int(i)
    else:
        num = num - 55
    total += num * (B**location)
    location -= 1

print(total)