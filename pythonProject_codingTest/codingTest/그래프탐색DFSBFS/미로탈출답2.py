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
from collections import deque

n,m = map(int, input().split())
graph = []
for i in range(m):
    graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    # 위치를 넣은 x,y좌표가 사라질 때까지 while문 반복
    while queue:
        x,y = queue.popleft()#위에서 넣은 x,y좌표를 꺼내주자.
        
        for i in range(4):#동서남북으로 좌표 이동 시키기
            nx = x+dx[i]
            ny = y+dy[i]
            # 만약 이동시킨 좌표가 매트릭스를 벗어나거나 0이라면 패스
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == 0:
                continue
            # 만약 이동한 좌표가 1이라면(갈 수 있는 곳)
            if graph[nx][ny] == 1:
                # 한 칸 이동할 때마다 +1씩 해주어 이동한 거리를 계산
                graph[nx][ny] = graph[x][y] + 1
                # 이동칸에서 다시 함수 불러옴
                queue.append((nx,ny))
    return graph[n-1][m-1]
print(bfs(0,0))