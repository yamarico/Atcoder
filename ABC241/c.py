N = int(input())
S=[]
ans_flag = False 
box = []


def yoko (a_list):
    b_list =[]
    for a in range(N-4):
        b_list = a_list[a:a+6]
        print(b_list)
        if b_list.count('#') >= 4:
            print('Yes')
            exit()
        return()

for _ in range(N):
    S.append(list(input().split()))
print(S)

for i in range(N):
    box = S[1][i]
    print(box)
    yoko(box)


    
    
    
