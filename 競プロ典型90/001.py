n ,l = map(int, input().split())
K = int(input())
A = list(map(int, input().split())))

def ok(l):
    left_idx = 0
    for i in range(K):
        right_ind = left_idx
        while (A[right_ind] - A[left_ind]<l):
            