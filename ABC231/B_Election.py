N = int(input())
list_a = []
b = 0
for i in range(N):
    A = input()
    list_a.append(A)
for i in range(N):
    a = list_a.count(list_a[i])
    if a > b:
        c = i
        b = a

print(list_a[c])