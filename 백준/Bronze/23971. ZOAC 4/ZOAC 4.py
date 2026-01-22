H,W,N,M = map(int,input().split()) # 세로, 가로, 가로간격, 세로간격

a = (H + N) // (N + 1)
b = (W + M) // (M + 1)
print(a * b)