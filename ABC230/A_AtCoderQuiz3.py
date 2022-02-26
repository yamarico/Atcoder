N = int(input())
if N >= 42:
    N = N + 1
    print('AGC0' + str(N))
elif 10 <= N < 42:
    print('AGC0' + str(N))
    
else:
    print('AGC00' + str(N))