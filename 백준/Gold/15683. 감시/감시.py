
from itertools import product

N, M = map(int, input().split())
office, cctv_indices,wall_indices, total_cctv_options = [], [], [], {1:[],2:[],3:[],4:[],5:[]}
for i in range(N):
    office.append(list(map(int, input().split())))
    for j in range(M):
        if 1<=office[i][j]<=5: # cctv index 미리 저장해둠
            cctv_indices.append((i,j,office[i][j]))
            total_cctv_options[office[i][j]].append((i,j))
        if office[i][j] == 6:
            wall_indices.append((i,j))

## 가능한 후보 조합을 미리 만들어두기
tt = list(product([0,1,2,3],repeat=4))
full_hubo = []
for ii in tt:
    for jj in tt:
        t_ = list(ii)
        t_.extend(list(jj))
        full_hubo.append(t_)
n_cctv = len(cctv_indices)
total_hubo = [tuple(lst[:n_cctv]) for lst in full_hubo]
total_hubo = list(set(total_hubo)) # 중복 제거 but 불가능한 조합도 좀 섞여있음

# 0: blank, 1~5: cctv, 6: wall, 7: looking
def right(x,y):
    looking_list = []
    for i in range(x+1,N):
        if office[i][y] == 0:
            #office[i][y] = 7 
            looking_list.append((i,y))
        elif office[i][y] == 6: #벽
            break
        else: # cctv 존재하면
            continue 
    return looking_list

def left(x,y):
    looking_list = []
    for i in reversed(range(0,x)):
        if office[i][y] == 0:
            #office[i][y] = 7 
            looking_list.append((i,y))
        elif office[i][y] == 6:
            break
        else: # cctv 존재하면
            continue     
    return looking_list            

def up(x,y):
    looking_list = []
    for j in reversed(range(0,y)):
        if office[x][j] == 0:
            #office[x][j] = 7
            looking_list.append((x,j))
        elif office[x][j] == 6:
            break
        else:
            continue
    return looking_list
def down(x,y):
    looking_list = []
    for j in range(y+1,M):
        if office[x][j] == 0:
            #office[x][j] = 7
            looking_list.append((x,j))            
        elif office[x][j] == 6:
            break
        else:
            continue
    return looking_list

option_dict = {1:[0,1,2,3], 2:[0,1], 3:[0,1,2,3], 4:[0,1,2,3], 5:[0]}

def one(option,x,y):
    lst = []
    if option == 0:
        lst.extend(up(x,y))
    elif option == 1:
        lst.extend(down(x,y))
    elif option == 2:
        lst.extend(left(x,y))
    else: # 3
        lst.extend(right(x,y))
    return lst

def two(option,x,y):
    lst = []
    if option == 0:
        lst.extend(up(x,y))
        lst.extend(down(x,y))
    else:
        lst.extend(left(x,y))
        lst.extend(right(x,y))
    return lst

def three(option,x,y):
    lst = []
    if option == 0:
        lst.extend(up(x,y))
        lst.extend(right(x,y))
    elif option == 1:
        lst.extend(right(x,y))
        lst.extend(down(x,y))
    elif option == 2:
        lst.extend(down(x,y))
        lst.extend(left(x,y))
    else:
        lst.extend(left(x,y))
        lst.extend(up(x,y))
    return lst
def four(option,x,y):
    lst = []
    if option == 0:
        lst.extend(up(x,y))
        lst.extend(left(x,y))
        lst.extend(right(x,y))
    elif option == 1:
        lst.extend(right(x,y))
        lst.extend(up(x,y))
        lst.extend(down(x,y))
    elif option == 2:
        lst.extend(down(x,y))
        lst.extend(right(x,y))
        lst.extend(left(x,y))
    else:
        lst.extend(left(x,y))
        lst.extend(down(x,y))
        lst.extend(up(x,y))
    return lst
def five(option,x,y):
    lst = []
    lst.extend(up(x,y))
    lst.extend(left(x,y))
    lst.extend(down(x,y))
    lst.extend(right(x,y))
    return lst
def looking(cctv_number,option,x,y):
    if cctv_number == 1:
        return one(option,x,y)
    elif cctv_number == 2:
        return two(option,x,y)
    elif cctv_number == 3:
        return three(option,x,y)
    elif cctv_number == 4:
        return four(option,x,y)
    else: 
        return five(option,x,y)

minimum_squre_zone = 100
for option_hubo in sorted(total_hubo):
    looked_indices = [] # 7인 index들 모음
    impossible = False
    for cctv_idx, cctv_option in enumerate(option_hubo): # 하나의 cctv에 접근
        info = cctv_indices[cctv_idx]
        x, y, what_cctv = info[0], info[1], info[2]
        options = option_dict[what_cctv]
        if cctv_option not in options: # 하나의 cctv에 대해서라도 불가능한 옵션이었다면 pass
            #print(option_hubo,':','불가능이요')
            impossible = True
            break

        looked_indices.extend(looking(what_cctv,cctv_option,x,y))


    if not impossible: # 가능한 조합이라면-> 사각지대 개수 확인
        total_looking = len(set(looked_indices))
        #print(total_looking)
        tmp_square_zone = N*M - len(cctv_indices) - total_looking - len(wall_indices) # 전체 구역 - cctv 설치된 곳 - cctv로 볼 수 있는 곳 - 벽 
        minimum_squre_zone = min(tmp_square_zone, minimum_squre_zone)

print(minimum_squre_zone)