A , B = map(int, input().split())
while (A > 0 and B > 0):
    if A % 10 + B % 10 >= 10: 
        print(A)
        print(B)
        print(A % 10 + B % 10)
        print('Hard\n')
        exit()
    else:
        A = A / 10
        B = B / 10
print('Easy\n')
