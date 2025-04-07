from collections import deque

n, k = map(int, input().split())

maps = []
#virus_dict = {i: deque() for i in range(0,k+1)}
virus_dict = {i: [] for i in range(0,k+1)}
for i in range(n):
    maps.append(list(map(int, input().split())))
    for j in range(n):
        val = maps[i][j]
        virus_dict[val].append((i,j)) # virus 종류별로 어디 index에 있는지 정보 모아두기
s, final_x, final_y = map(int, input().split())
final_x -=1
final_y -=1

dx = [0,0,-1,1]
dy = [-1,1,0,0]
for second in range(s):
    new_virus_dict = {i: [] for i in range(0, k+1)} 
    for k_ in range(1,k+1):
        for x,y in virus_dict[k_]: # k_ 바이러스가 존재하는 인덱스들을 모두 순회
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<n and 0<=ny<n and maps[nx][ny] == 0:
                    maps[nx][ny] = k_
                    '''
                    # 아래처럼 순회 도중에 deque 수정하면 RuntimeError: deque mutated during iteration
                    virus_dict[k_].popleft() # 이미 증식한건 굳이 또 안돌아도되니까
                    virus_dict[k_].append((nx,ny))
                    '''
                    new_virus_dict[k_].append((nx,ny))
        #virus_dict[k_] = virus_dict[k_][len(virus_dict[k_]):] # 원래 있던건 없애고 새로운 것만 남게 -> 그냥 새로운 걸 만들어서 갱신하기
        virus_dict[k_] = new_virus_dict[k_]
if maps[final_x][final_y]:
    print(maps[final_x][final_y])
else:
    print(0)    