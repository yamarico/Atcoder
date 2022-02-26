import collections

N = int(input())
x_list = list(map(int, input().split()))
c = collections.Counter(x_list)
print(len(c))
