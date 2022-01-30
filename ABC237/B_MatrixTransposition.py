H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = []

for i in range(W):
    for j in range(H):
        B.append(A[j][i])
    print(*B)
    B = []