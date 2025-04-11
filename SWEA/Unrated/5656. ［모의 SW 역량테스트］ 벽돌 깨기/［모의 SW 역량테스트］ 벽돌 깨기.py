# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

#import sys


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#sys.stdin = open("input.txt", "r")
from collections import deque

dx,dy = [0,0,1,-1], [1,-1,0,0]

def clean_wall(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr[0])):
            p = i
            while p>=0 and arr[p][j] != 0 and arr[p+1][j] ==0:
                arr[p][j], arr[p+1][j] = arr[p+1][j], arr[p][j]
                p -= 1
    return arr          

def shoot(j, arr, column):
    x, y = column[j], j
    num = arr[x][y]    
    q= deque()
    q.append((x,y,num))
    while q:
        x,y,num = q.pop()
        arr[x][y] = 0
        for i in range(4):
            nx, ny = x, y
            for j in range(num-1):
                nx,ny = nx+dx[i], ny+dy[i]
                if nx<0 or nx>=H or ny<0 or ny>=W:
                    break
                #if arr[nx][ny] !=0:
                nnum = arr[nx][ny]
                q.append( (nx,ny,nnum) ) 
                arr[nx][ny] = 0
    updated_arr = clean_wall(arr)
    updated_column = first_wall_per_column(updated_arr)
    return updated_arr, updated_column

def copy_arr(arr):
    return [row[:] for row in arr]

def dfs(cnt, arr, column,for_check):
    global N,min_value

    if cnt == N:
        tmp_min = 0
        for i in range(H):
            for j in range(W):
                if arr[i][j] != 0:
                    tmp_min +=1
        #if for_check == [2,2,2]:
        #    for i in range(H):
        #        print(arr[i]) # 프린트문 지우기
        min_value = min(tmp_min,min_value)
        min_values.append(min_value)
        return
    
    tmp_arr = copy_arr(arr)
    tmp_column = column.copy()
    #print('cnt:',cnt)
    for j in range(W):
        if column[j] != -1:
            tmp_arr, tmp_column = shoot(j, tmp_arr, tmp_column)      
            if tmp_column == [-1 for _ in range(W)]:
                min_values.append(0)
                return
            dfs(cnt+1, tmp_arr, tmp_column,for_check+[j])
            tmp_arr = copy_arr(arr)
            tmp_column = column.copy()
            
def first_wall_per_column(arr): # 각 열별로 제일 위에 있는 벽의 x 좌표
    column = [-1 for _ in range(len(arr[0]))] 
    transpose_wall = list(map(list,zip(*arr)))
    for j in range(len(arr[0])):
        tt = transpose_wall[j]
        for i in range(len(arr)):
            if tt[i] != 0:
                column[j] = i
                break
    return column            


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,W,H = map(int, input().split())
    wall,min_values= [],[]
    min_value = 1e9
    for i in range(H):
        wall.append(list(map(int, input().split())))
    column = first_wall_per_column(wall)
    if column == [-1 for _ in range(W)] :
        min_value = 0
    else:
        dfs(0, wall, column,[])
        min_value = min(min_values)
    print(f'#{test_case} {min_value}')
"""
wall = []
min_value = 1e9
N,W,H = map(int, input().split())
for i in range(H):
    wall.append(list(map(int, input().split())))

column = first_wall_per_column(wall)        
if column == [-1 for _ in range(W)] :
    min_value = 0
else:    
    dfs(0, wall, column,[])
    print(min(min_values))
"""