import bisect

Q = int(input())

q_list=[]
index =[]
ans =[]
for _ in range(Q):
    q_list.append(input())

for i in range(Q):
    ans.sort()
    a = q_list[i]
    b = a.split()
    print(b)
    
    if b[0] == '1':
        ans.append(int(b[1]))
    elif b[0] == '2':
        index = bisect.bisect_left(ans, int(b[1]))
        if len(index) >= int(b[2]):
            print(index[-int(b[2])])
        else:
            print(-1)
    elif b[0] == '3':
        if len(index) >= int(b[2]):
            print(index[(b[2])])
        else:
            print(-1)
        
        
print(ans)
    