A, B, C, X = map(int, input().split())
if X <= A:
    print('1.000000000000')
elif A < X <= B:
    print(C/(B-A))
else:
    print('0.000000000000')