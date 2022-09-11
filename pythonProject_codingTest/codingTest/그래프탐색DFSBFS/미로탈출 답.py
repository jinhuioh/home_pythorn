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

# 행렬입력받기
n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# 이동할 4가지 방향 정의
dx = [-1,1,0,0]#좌우
dy = [0,0,-1,1]#상하

# 함수구현
def miro(x,y):
    # 큐 구현을 위해 deque라이브러리 사용
    queue = deque()
    queue.append((x,y))
    while queue:
        # popleft()로 맨 앞 원소 1개씩 빼내기.
        x,y = queue.popleft()
        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <0 or nx >= n or ny <0 or ny >= m:
                continue
            # 괴물이 있는 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
            # 가장 오른쪽 아래까지의 최단 거리 반환
        return graph[n-1][m-1]
print(miro(0,0))