ax1, ay1, bx1, by1, cx1, cy1, dx1, dy1, ax2, ay2, bx2, by2, cx2, cy2, dx2, dy2 = map(int, input().split())
A = []
B = []

def slide(ax2, ay2, bx2, by2, cx2, cy2, dx2, dy2):
    wax2, way2, wbx2, wby2, wcx2, wcy2, wdx2, wdy2 = bx2, by2, cx2, cy2, dx2, dy2,ax2, ay2
    return(wax2, way2, wbx2, wby2, wcx2, wcy2, wdx2, wdy2)

for _ in range(10):
    ax2, ay2, bx2, by2, cx2, cy2, dx2, dy2 = slide(ax2, ay2, bx2, by2, cx2, cy2, dx2, dy2)
    A = []
    B = []
    A += [ax1+ay1, bx1+by1, cx1+cy1, dx1+dy1]
    B += [ax2+ay2, bx2+by2, cx2+cy2, dx2+dx2]
    C = A.index(max(A))
    D = B.index(max(B))
    E = A.index(min(A))
    F = B.index(min(B))
    if C == D and E == F:
        break
    
if (max(cx1, cx2) <= min(ax1, ax2)) and (max(cy1, cy2) <= min(ay1, ay2)):
    print('TRUE')
else:
    print('FALSE')