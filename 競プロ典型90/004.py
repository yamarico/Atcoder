#Cross Sum
# 入力の受け取り
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# 各行の和をLに格納する
L = []
for i in range(H):
  L.append(sum(B[i]))

# 各列の和をRに格納する
R = []
for i in range(W):
  cnt = 0
  for j in range(H):
    cnt += B[j][i]
  R.append(cnt)

# 各マスにおいての行と列の合計値を求め、二重に加算されているA[i][j]を減算する。
B = []

for i in range(H):
  l = []
  for j in range(W):
    sums = L[i] + R[j] - A[i][j]
    l.append(sums)
  B.append(l)

# 答えを出力する
for i in range(H):
  print(*B[i])
