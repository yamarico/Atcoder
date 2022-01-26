N, Q = map(int, input().split())
A = list(map(int, input().split()))
x = []
count = 0

for _ in range(Q):
    x.append(int(input()))

for i in range(Q):
    count = 0
    for j in range(N):
	    if x[i] <= A[j]:
             count = count + 1
    print(count)