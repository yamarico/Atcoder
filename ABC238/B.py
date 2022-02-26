N = int(input())
A = list(map(int, input().split()))
R = []
T = []
ans = 0
for i in range(N):
    R.append(sum(A))
    del A[0]
for j in range(N):
    if R[j] >= 360:
        R[j] = R[j]% 360

R.append(0)
R.append(360)
T = sorted(R)

for k in reversed(range(N+2)):
    if T[k] - T[k-1] > ans:
        ans = T[k] - T[k-1]      
print(ans)
