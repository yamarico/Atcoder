N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(M):
    if B[i] in A:
        for j in range(N):
            if B[i] == A[j]:
                del A[j]
                break
    else:
        print("No")
        exit()
print("Yes")