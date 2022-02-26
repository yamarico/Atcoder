#002_Encyclopedia of Parentheses

# 入力の受け取り
N = int(input())

# カッコ列を格納する配列
pare = []

# ビット全探索
for i in range(1 << N):

# 1の時 "(" を、0の時 ")" を文字列に追加していく
    l = ""
    for j in range(N):
        if i >> j & 1:
            l += "("
        else:
            l += ")"
    print(l)
# 文字列の長さがNの時のみ、左から検索する。その時cntで"("と")"の出現回数を計算する。cntが0より小さくならなかった＋cntが0(出現回数が等しかった)文字列のみをpareに格納する
    if len(l) == N:
        cnt = 0
    flag = True
    for k in range(N):
        
        if l[k] == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            flag = False
    if flag and cnt == 0:
        pare.append(l)

# pareを辞書順にソート、順番に出力する
pare.sort()

for i in range(len(pare)):
    print(pare[i])
