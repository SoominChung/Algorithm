#import copy
from collections import deque

## [속도 초과] 원인: deepcopy가 아주 비싼 연산임. 만약 list 크기가 10^6됐는데 deepcopy를 계속 반복하면 속도 초과 될 수 밖에..
# (1) prev_box: bool로 쉽게 대체가능
# (2) fullbox: full_box 정의 위한 deepcopy는 한 번 밖에 연산 안하지만 그래도 라이브러리 임포트 하는 등의 시간 모두 줄이기 위해 deepcopy 없이 수정했음 -> 얘 걍 n_raw로만 확인가능함
M, N, H = map(int, input().split())

box = [[] for _ in range(H)]
#full_box = [[[1 for _ in range(M)] for _ in range(N)] for _ in range(H)] # full box도 -1 고려했어야함! 전체가 1인 박스가 아니라 -1 아닌 0,1인 부분이 모두 1인게 full box임
#full_box = [[] for _ in range(H)]
tomatoes = deque()
raw_tomatoes = []
total_tomatoes = 0
for h in range(H):
    for i in range(N):
        box[h].append(list(map(int, input().split())))
        #full_box[h].append(box[h][i].copy())

        for j in range(M):
            if box[h][i][j] == 1:
                tomatoes.append((i,j,h))
            if box[h][i][j] == 0:
                raw_tomatoes.append((i,j,h))

# 익은 + 덜익은 토마토 개수 -> 그냥 n_raw만 있으면 됨
# total_tomatoes += len(tomatoes)
# total_tomatoes += len(raw_tomatoes)

# 풀박 = 0이었던 raw tomato들이 모두 1이 된 경우
#full_box = copy.deepcopy(box)
#for x,y,z in raw_tomatoes:
#    full_box[z][x][y] = 1
n_raw = len(raw_tomatoes)

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1 ,1]

def bfs(n_raw):
    #if len(tomatoes) == total_tomatoes: # 이미 모든 토마토가 익어있다면 0 출력 -> 다 익었을 경우는 HxNxM이 아니라 전체 토마토 개수만큼이었음!
    if n_raw == 0:
        return 0

    if len(tomatoes) == 0: # 익은 토마토가 하나도 없다면 익을 수 없음 (얘를 계속 놓쳤음 ㅠㅠ 극단적인 테스트케이스 고려하기)
        return -1
    
    days =0 
    while tomatoes:
        #prev_box = copy.deepcopy(box) # copy대신 bool로 확인
        is_updated = False 
        one_day_size = len(tomatoes)
        for i in range(one_day_size):
            x,y,z = tomatoes.popleft()
            for j in range(6):
                nx = x+dx[j]
                ny = y+dy[j]
                nz = z+dz[j]
                if 0<=nx<N and 0<=ny<M and 0<=nz<H and box[nz][nx][ny] == 0:
                    box[nz][nx][ny] = 1
                    tomatoes.append((nx,ny,nz))
                    is_updated = True
                    n_raw = n_raw-1
        if is_updated == False: # 하루 전이랑 변화가 없다면 가망 없는 박스
            return -1
        
        days += 1
        #if box == full_box: # 모두 찼다면 소요 일수 리턴
        if n_raw == 0:
            return days

    #return days

print(bfs(n_raw))