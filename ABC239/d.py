A, B, C, D= map(int, input().split())
f_1 = 0

for i in range(A, B + 1):
    for j in range(C, D + 1):
        sum = i + j
        if sum <= 1:
            auu=0    
        else:
            for i in range(2, int(sum**0.5)+1):
                if sum % i == 0:
                    auu=0     
                else:
                    f_1 = 1
        
print(f_1)
if f_1 ==1 :
    print("Aoki")
else:
    print("Takahashi")
        
