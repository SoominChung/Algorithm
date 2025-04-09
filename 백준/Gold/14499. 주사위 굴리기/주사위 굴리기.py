
N,M,x,y,K = map(int,input().split())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))
movement = list(map(int, input().split())) # 오:1, 왼:2, 위:3, 아래:4

dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

dice = [0 for _ in range(7)]  # 1~6: 위,뒤,오른,왼,앞,아래

def right(dice):
    return [0,dice[4],dice[2],dice[1],dice[6],dice[5],dice[3]]
def left(dice):
    return [0,dice[3],dice[2],dice[6],dice[1],dice[5],dice[4]]
def up(dice):
    return [0,dice[5],dice[1],dice[3],dice[4],dice[6],dice[2]]
def down(dice):
    return [0,dice[2],dice[6],dice[3],dice[4],dice[1],dice[5]]

for mv in movement:
    x,y = x+dx[mv], y+dy[mv] # 지도에서의 도착지
    if x<0 or x>=N or y<0 or y>=M: # 지도 벗어나면 다음 움직임으로 넘어감
        x -= dx[mv]
        y -= dy[mv]
        continue
    value = maps[x][y] # 지도 값

    # 주사위 굴리기
    if mv == 1:
        dice = right(dice)
    elif mv == 2:
        dice = left(dice)
    elif mv == 3:
        dice = up(dice)
    elif mv == 4:
        dice = down(dice)

    if value == 0: # 칸에 쓰인 수가 0이면
        #주사위 바닥면이 칸에 복사됨
        maps[x][y] = dice[6]

    else: # 칸에 쓰인 수가 0이 아니면
        # 칸에 쓰인 수가 주사위 바닥에 복사됨
        dice[6] = maps[x][y]
        # 칸이 0됨
        maps[x][y] = 0

    print(dice[1]) # 윗면 