from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

n, k = map(int, input().split())

maps = []
queue = []
for i in range(n):
    maps.append(list(map(int, input().split())))
    for j in range(n):
        val = maps[i][j]
        if val != 0: # 바이러스라면 정보 저장해둠!
            queue.append((val, i, j))
S, final_x, final_y = map(int, input().split())
final_x -=1
final_y -=1

queue.sort() #sort 사용하기 위해서 우선 list로 정의하고 이후에 deque로 바꿔줌
queue = deque(queue)

time = 0 
while queue:
    if time == S:
        break

    for _ in range(len(queue)):
            
        k_, x, y = queue.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and maps[nx][ny] == 0:
                maps[nx][ny] = k_
                queue.append((k_, nx, ny))
    time += 1    
if maps[final_x][final_y]:
    print(maps[final_x][final_y])
else:
    print(0)    