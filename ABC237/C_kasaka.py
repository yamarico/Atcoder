S = input()
N = len(S)
a_count = 0
b_count = 0
m = 0
for i in reversed(S):
    if 'a' == i:
        a_count = a_count + 1
    else:
        break

for k in S:
    if 'a' == k:
        b_count = b_count + 1
    else:
        break

#そもそも回文かを判定
for j in range(b_count, N - a_count):
    if S[j] != S[N - a_count-1-m] or a_count < b_count :
        print("No")
        exit()
    m = m + 1
print("Yes")