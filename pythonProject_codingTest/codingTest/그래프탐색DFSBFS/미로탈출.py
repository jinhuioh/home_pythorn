##BFS문제(미로문제, 터널문제, 너비탐색(선입선출))
# 동빈이는 n*m 크기의 직사각형 형태의 미로에 갇혔습니다.
# 미로를 탈출해야 합니다.
# 동빈이의 위치는(1,1)이며 미로의 출구는 (n,m)의 위치에 존재하며 한 번에 한 칸씩 이동가능합니다.
# 이때 괴물이 위치한 부분은 0 없는 부분은 1로 되어있습니다.
# 미로는 반드시 탈출 할 수 있는 형태로 제시됩니다.
# 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하세요.
# 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산합니다.
#
# 입력조건: 첫째 줄에 두 정수 n,m(4<=n, m<=200)이 주어집니다.
# 다음 n개의 줄에는 각각 m개의 정수(0또는 1)로 미로의 정보가 주어집니다.
# 각각 수들은 공백 없이 입력으로 제시됩니다. 또한 시작 칸과 마지막 칸은 항상 1입니다.
# 출력조건: 첫째 줄에 최소 이동 칸의 개수를 출력합니다.


#위치한 곳의 좌표가 1이면 이전꺼+좌표값(1)을 해서 카운트를 늘려감
#범위를 벗어나거나, 0인경우 return false를 반환
from collections import deque

# queue = deque([1,2])
# one = queue.popleft()
# one2 = queue.popleft()
# print(one)
# print(one2)


n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))



#이동시킬 좌표값
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def miro(y,x):
    queue = deque()
    queue.append((y,x))
    print('큐~',queue)
    while queue:
        yy,xx = queue.popleft()
        print('yy',yy)
        print('xx',xx)
        #상하좌우로 채크해서 자리값이 1이면 카운트 증가시켜 이동시키기. 만약 자리값이 1이아니면 return False
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            if ny >= n or ny < 0 or nx >= m or nx < 0:
                continue
            print('ny nx', ny, nx)
            if graph[ny][nx] == 1:
                print('1인 좌표로 이동')
                graph[ny][nx] = graph[yy][xx] + 1
                queue.append((ny, nx))
                print('if문 안에queue append> ',queue)
            else:
                pass
        print('queue append확인>> ',queue)
    return print('답',graph[n-1][m-1])

miro(0,0)













#
#
# # ##
# from collections import deque
# n,m = map(int,input().split())#세로가로입력
# graph = []
# for i in range(n):
#     graph.append(list(map(int,input())))
# print(graph)
#
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
# def bfs(x,y):#x는 가로 y는 세로
#     # 상하좌우에 대해 for문 돌리기
#     queue = deque()
#     queue.append((x,y))
#     while queue:
#         print('queue',queue)
#         x,y = queue.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if nx < 0 or nx >= m or ny < 0 or ny >= n:
#                 continue
#             if graph[ny][nx] == 0:
#                 continue
#             if graph[ny][nx] == 1:
#                 graph[ny][nx] = graph[y][x] + 1
#                 queue.append((nx,ny))
#     return graph[n-1][m-1]
# print(bfs(0,0))
#
#
# # bfs(0,0)으로 시작해야함
#
#
#
#
#
#







# # 너비를 계산하여 최단거리를 찾아보자
# def miro(x,y):
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     # 괴물이 없는 길인 경우
#     if graph[x][y] == 1:
#         # 최단거리를 가기위해 괴물이 있는 칸으로 바꾼다.
#         graph[x][y] = 0
#         # 재귀함수로 처리하여 아래 행으로 한 칸 옮기면서 최단거리 계산
#         miro(x,y+1)
#         return True
#     return False
#
# # 행렬입력받기
# n,m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int,input())))
#
# result = 0
#
# for a in range(n):
#     for b in range(m):
#         if miro(a,b) == True:
#             result +=1
# print(result)