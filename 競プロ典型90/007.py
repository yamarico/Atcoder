# CP Classes
N = int(input())
A_list = map(int, input().split())
Q = int(input())
B_list = []
for _ in range(Q):
    B_list.append(int(input()))

A_list.sort()

for i in range(Q):
    for j in range(len(A_list)):
        if　B_list[i] - A_list[j]  




