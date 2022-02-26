N = int(input())
a_list = list(map(int, input().split()))
ans_list = []
box_list = ["a"]

def aa (ans_list):
    box = 0
    box_list = []
    for i in range(len(ans_list)):
        if i == 0:
            box = ans_list[i]
        else:
            box = ans_list[i-1]
        if box == ans_list[i]:
            box_list.append("b")
            if box == len(box_list) and box != 1:
                for _ in range(box):
                    del ans_list[-1]
            else:
                box_list = []
                box_list.append("b")
    return(ans_list)

for i in range(N):
    ans_list.append(a_list[i])
    aa(ans_list)
    print(len(ans_list))
