N, K = map(int ,input().split())
S = []

for _ in range(N):
    S.append(sum(map(int, input().split())))
T = S
border =  sorted(T)[-K]
for i in range(N):
    if S[i] < border - 300:
        print("No")
    else:
        print("Yes")
