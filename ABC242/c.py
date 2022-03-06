N = int(input())
start_num = 10**(N-1)
goal_num = 10**(N)
ans = 0
def aa (num_list, flag, danger, ans):
    for j in range(len(num_list)-1):
            a_num = int(num_list[j])
            b_num = int(num_list[j+1])
            c_num = a_num - b_num
            d_num = num_list.count('0')
            if d_num >= 1:
                continue
                
            #print(a_num, b_num, c_num)
            if c_num == 0 or c_num == -1 or c_num == 1:
                flag = 1
            else:
                danger = 1

print(start_num, goal_num)
for i in range(start_num, goal_num):
    n_str = str(i)
    num_list = list(n_str)
    flag = 0
    danger = 0
    flag, danger, ans = aa(num_list, flag, danger, ans)
    if flag == 1 and danger == 0:
        print(i)
        ans = ans + 1
if ans >= 998244353:
    ans = ans // 998244353

print(ans)