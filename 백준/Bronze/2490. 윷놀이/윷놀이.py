result = {0: "E", 1: "A", 2: "B", 3: "C", 4: "D"}

for _ in range(3): 
    a = list(map(int, input().split()))
    count = a.count(0) 
    print(result[count])
