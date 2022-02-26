x_1, y_1, x_2, y_2 = map(int, input().split())

def aa (x_1, y_1, x_2, y_2):
    for i in range (-5, 6):
        for j in range (-5, 6):
            if (x_1 - (x_1 - i))**2 + (y_1 - (y_1 - j))**2 == 5 and (x_2 - (x_1 - i))**2 + (y_2 - (y_1 - j))**2 == 5 or (x_1 - (x_2 - i))**2 + (y_1 - (y_2 - j))**2 == 5 and (x_2 - (x_2 - i))**2 + (y_2 - (y_2 - j))**2 == 5:
                return(2) 
    return(0)
            
c_1 =0      
c_1 = aa(x_1, y_1,x_2, y_2)
if c_1 == 2 :
    print("Yes")
else:
    print("No")