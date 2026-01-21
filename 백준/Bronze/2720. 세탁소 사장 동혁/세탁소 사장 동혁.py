T = int(input())       # 반복횟수

for _ in range(T):
    money = int(input())
    Q = money // 25     #1달러 = 100센트
    money %= 25
    D = money // 10
    money %= 10
    N = money // 5
    money %= 5
    P = money           # 나머지
    print(Q,D,N,P)