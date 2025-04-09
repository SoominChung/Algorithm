
from collections import deque

N = int(input())
init_board = []
for _ in range(N):
    init_board.append(list(map(int,input().split())))

def up(board):
    new_board,tmp_list = [],[]
    max_value = 0
    for tmp_list_ in list(zip(*board)):
        new_list= []
        tmp_list = deque([x for x in list(tmp_list_) if x>0])

        while tmp_list:
            if len(tmp_list)==1:
                new_list.extend(list(tmp_list))
                break
            x1 = tmp_list.popleft()
            x2 = tmp_list[0]
            if x1==x2:
                new_list.append(x1*2)
                _ = tmp_list.popleft()
            else:
                new_list.append(x1)
        
        new_list.extend([0]*(N-len(new_list)))
        new_board.append(new_list)
        max_value = max(max_value, max(new_list))
    final_new = [list(col) for col in zip(*new_board)]
    return max_value, final_new

def down(board):
    new_board,tmp_list = [],[]
    max_value = 0
    for tmp_list_ in list(zip(*board)):
        new_list = []
        tmp_list = deque(reversed([x for x in list(tmp_list_) if x>0]))

        while tmp_list:
            if len(tmp_list)==1:
                new_list.extend(list(tmp_list))
                break
            x1 = tmp_list.popleft()
            x2 = tmp_list[0]
            if x1==x2:
                new_list.append(x1*2)
                _ = tmp_list.popleft()
            else:
                new_list.append(x1)
        
        new_list.extend([0]*(N-len(new_list)))
        new_board.append(list(reversed(new_list)))
        max_value = max(max_value, max(new_list))

    final_new = [list(col) for col in zip(*new_board)]
    return max_value, final_new

def right(board):
    new_board,tmp_list = [],[]
    max_value = 0
    for tmp_list_ in board:
        new_list = []
        tmp_list = deque(reversed([x for x in list(tmp_list_) if x>0]))

        while tmp_list:
            if len(tmp_list)==1:
                new_list.extend(list(tmp_list))
                break
            x1 = tmp_list.popleft()
            x2 = tmp_list[0]
            if x1==x2:
                new_list.append(x1*2)
                _ = tmp_list.popleft()
            else:
                new_list.append(x1)
        
        new_list.extend([0]*(N-len(new_list)))
        new_board.append(list(reversed(new_list)))
        max_value = max(max_value, max(new_list))

    return max_value, new_board

def left(board):
    new_board,tmp_list = [],[]
    max_value = 0
    for tmp_list_ in board:
        new_list= []
        tmp_list = deque([x for x in list(tmp_list_) if x>0])

        while tmp_list:
            if len(tmp_list)==1:
                new_list.extend(list(tmp_list))
                break
            x1 = tmp_list.popleft()
            x2 = tmp_list[0]
            if x1==x2:
                new_list.append(x1*2)
                _ = tmp_list.popleft()
            else:
                new_list.append(x1)
        
        new_list.extend([0]*(N-len(new_list)))
        new_board.append(new_list)
        max_value = max(max_value, max(new_list))

    return max_value, new_board

def move(number,board):
    if number == 0: # 위로 이동
        return up(board)
    elif number == 1: # 우로 이동
        return right(board)
    elif number == 2: # 아래로 이동
        return down(board)
    else: # 좌로 이동
        return left(board)

max_val = 0
for first in range(4):
    for second in range(4):
        for third in range(4):
            for fourth in range(4):
                for fifth in range(4):
                    #print('===== trial: ',trial)
                    #print(init_board)
                    # 1st trial
                    tmp_max, board = move(first,init_board)
                    #print(board)
                    max_val = max(max_val,tmp_max)

                    # 2nd trial
                    tmp_max, board = move(second,board)
                    #print(board)
                    max_val = max(max_val,tmp_max)    

                    # 3rd
                    tmp_max, board = move(third,board)
                    #print(board)
                    max_val = max(max_val,tmp_max)    
                    
                    # 4th
                    tmp_max, board = move(fourth,board)
                    #print(board)
                    max_val = max(max_val,tmp_max)    
                    
                    # 5th
                    tmp_max, board = move(fifth,board)
                    #print(board)
                    max_val = max(max_val,tmp_max)                                                                                               
print(max_val)