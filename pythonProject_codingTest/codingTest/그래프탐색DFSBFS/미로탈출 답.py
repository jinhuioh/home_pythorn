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
# ##
# 큐
# 큐 넣기(맨뒤에 원소1삽입)=enqueue =파이썬의 append()
# 큐 빼기(맨 앞에서 원소1개 빼내기)=dequeue=파이썬의 popleft()

# 선입선출로 입구와 출구가 터널 형태로 되어있는 문제는 queue 함수를 이용한다.
from collections import deque
# 행렬 입력받기
n, m = map(int, input().split())
# 그래프 모양 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
# 이동할 수 있는 좌우/상하 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# bfs함수화
def bfs(x, y):
    # 시작 위치 입력받기
    queue = deque()
    queue.append((x,y))
    while queue:
        # while문을 통해 입력받은 위치를 차례대로 꺼냄
        x,y = queue.popleft()
        # 갈 수 있는 좌표를 선택하기 위해 상하좌우 4번 좌표를 이동시킴
        for i in range(4):
            nx = x + dx[i]# 서있는 좌표x에서 좌우로 dx[i]만큼 이동
            ny = y + dy[i]
            # 매트릭스를 넘어가면 continue로 넘기기
            if nx == -1 or nx == n or ny == -1 or ny == m:
                continue
            # 0이면 괴물이 있으므로 continue로 넘기기
            if graph[nx][ny] == 0:
                continue
            # 갈 수 있는 좌표인 경우
            if graph[nx][ny] == 1:
                # 큐에 갈 수 있는 좌표 append
                # 이동한 좌표를 서있는 좌표로 변경
                queue.append((nx, ny))
                # 한칸씩 이동하므로 +1로 크기를 키운다.
                graph[nx][ny] = graph[x][y]+1
    # 해당 함수의 리턴은 매트릭스의 마지막 좌표인 [n-1][m-1]
    return graph[n-1][m-1]
print(bfs(0,0))