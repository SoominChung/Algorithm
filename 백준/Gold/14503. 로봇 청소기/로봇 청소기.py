
N, M = map(int, input().split())
x, y, direction = map(int, input().split())

# 전진, 후진시의 dx,dy
forward = {0: [-1,0], 1: [0,1], 2: [1,0], 3: [0,-1]}
backward = {0: [1,0], 1:[0,-1], 2:[-1,0], 3:[0,1]}
rotation = {0: 3, 1:0, 2:1, 3:2}

# 주변 둘러보기 위함
dx = [0,0,-1,1]
dy = [1,-1,0,0]

room = []
for i in range(N):
    room.append(list(map(int, input().split())))



over = False # 청소 종료
cleaned_room = 0 # 청소한 방의 개수
while not over:
    curr = room[x][y] # 현재 방의 상태

    if curr == 0: # (1) 현재 칸이 청소 안됐다면 청소
        room[x][y] = 2
        cleaned_room += 1

    # 주변 4칸을 확인함
    check_surround = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if 0<=nx<N and 0<ny<M and room[nx][ny]==0: # 청소 안된 칸 존재
            check_surround =1
            break

    if check_surround: # (3) 주변 4칸 중 청소안된 칸 존재
        # 1. 반시계 방향 회전
        direction = rotation[direction]

        # 2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
        nx, ny = x+forward[direction][0], y+forward[direction][1] # 다음 칸 정의

        if 0<=nx<N and 0<=ny<M: # 접근 가능한지 확인
            if room[nx][ny] == 0: # 청소되지 않은 빈칸이라면 전진
                x, y = nx, ny
            #else:
            #    over = True
        #else: # 접근 불가면 
        #    over = True

    else: # (2) 주변 4칸 중 청소 안된 빈 칸이 없을 경우
        # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.

        nx, ny = x+backward[direction][0], y+backward[direction][1] # 다음 칸 정의 

        if 0<=nx<N and 0<=ny<M: # 갈 수 있으면
            if room[nx][ny] != 1: # 벽 아니면 후진 가능
                x, y = nx, ny
            else: # 벽이면
                over =True
        #else: # 못가면 
        #    over = True


print(cleaned_room)