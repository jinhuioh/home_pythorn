from collections import deque

worldmap = ['..XXX', '..XXX', '...XX', 'X....', 'XXX..']

def solution(worldmap):
    N = len(worldmap)
    M = len(worldmap[0])
    graph = [[] for _ in range(N)]
    for i in range(N):
        for k in range(M):
            if worldmap[i][k] == '.':
                graph[i].append(0)
            else:
                graph[i].append('X')
    # print(graph)
    # 시작 위치 입력받기
    queue = deque()
    queue.append((0, 0))
    dx = [1, 0, 1]  # 우
    dy = [1, 1, 0]  # 상
    x, y = 0, 0  # 초기값
    while queue:
        # while문을 통해 입력받은 위치를 차례대로 꺼냄
        x, y = queue.popleft()
        # 갈 수 있는 좌표를 선택하기 위해 상하좌우 4번 좌표를 이동시킴
        for i in range(3):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            # # 매트릭스를 넘어가면 continue로 넘기기
            # if nx == -1 or nx == n or ny == -1 or ny == m:
            #     continue
            if graph[ny][nx] == 'X':
                continue
            # 갈 수 있는 좌표인 경우
            if graph[ny][nx]  == 0:

                queue.append((nx, ny))
                # 한칸씩 이동하므로 +1로 크기를 키운다.
                graph[nx][ny] = graph[x][y] + 1
                # print('nynx', ny, nx)
                # print('graph[nx][ny]', graph[nx][ny])
            if ny == N-1 and nx == M-1:
                break
    return graph[N-1][M-1]+1
print(solution(worldmap))