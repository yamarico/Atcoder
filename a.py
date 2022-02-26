N = int(input())
L = []
r, g, b = map(int, input().split())
ans = 'no'
for i in range(N):
    L.append(list(input().split()))
r_box = r
g_box = g
b_box = b

def aa (r, g, b,  light):
    if light == "R":
        r = r + 1
    elif light == "G":
        g = g + 1
    elif light == "B":
        b = b + 1
    elif light == "Y":
        r = r + 1
        g = g + 1
    elif light == "M":
        r = r + 1
        b = b + 1

    elif light == "C":
        b = b + 1
        g = g + 1
    
    elif light == "W":
        r = r + 1
        b = b + 1
        g = g + 1
    return(r, g, b)
def bb (r, g, b,  light):
    if light == "R":
        r = r - 1
    elif light == "G":
        g = g - 1
    elif light == "B":
        b = b - 1
    elif light == "Y":
        r = r - 1
        g = g - 1
    elif light == "M":
        r = r - 1
        b = b - 1

    elif light == "C":
        b = b - 1
        g = g - 1
    
    elif light == "W":
        r = r - 1
        b = b - 1
        g = g - 1
    return(r, g, b)

for i in range(N):
    place = L[i][0]
    light = L[i][1]
    if place == 'R':
        r_box, g_box, b_box = aa(r_box, g_box, b_box, light)
    elif place == 'L':
        r_box, g_box, b_box = bb(r_box, g_box, b_box, light)
    if r_box == b_box == g_box:
        ans = r_box 
        print(ans)
        exit()
print(ans)
    