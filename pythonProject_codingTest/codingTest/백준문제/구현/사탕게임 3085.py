# 문제
# 상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.
#
# 가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다.
# 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다.
# 이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.
#
# 사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)
#
# 다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다. 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.
#
# 사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.
#
# 출력
# 첫째 줄에 상근이가 먹을 수 있는 사탕의 최대 개수를 출력한다.

# 1시18분시작
from collections import deque

n = int(input())
graph1 = []# 값 입력받기
graph2 = []#값을 숫자로 바꾸기
graph = []#값을 숫자로 바꾸기
for i in range(n):
    graph.append(list((input())))
# for q in range(n):
#     for w in range(n):
#         if graph[q][w] == 'C':
#             graph[q][w] = 1
#         elif graph[q][w] == 'P':
#             graph[q][w] = 2
#         elif graph[q][w] == 'Z':
#             graph[q][w] = 3
#         else:
#             graph[q][w] == 4
print(graph)
dx = [0,0,-1,1]#상하좌우
dy = [1,-1,0,0]
def bomboni(x,y):#가로세로입력
    count = []
    count1,count2 = 0,0
    #주어진 위치에서 상하좌우에 있는 단어와 바꿈
    while True:
        print('while문 시작~ ',graph)
        for i in range(4):#상하좌우
            nx = x + dx[i]
            ny = y + dy[i]
            print('nxny',nx,ny)
            print('graph[y][x] graph[ny][nx]', graph[y][x], graph[ny][nx])

            #범위를 벗어날 경우
            if nx<0 or nx>n or ny<0 or ny>n:
                continue
            # 만약 인접한 단어와 같다면
            if graph[y][x] == graph[ny][nx]:
                return bomboni(nx, ny)
                continue
            # 만약 인접한 단어와 다르다면 위치 바꿈
            if graph[y][x] != graph[ny][nx]:
                print('graph[y][x] graph[ny][nx]',graph[y][x],graph[ny][nx])
                graph[y][x], graph[ny][nx] = graph[ny][nx], graph[y][x]
                queue = deque()
                queue1 = deque()
                queue.append((x,y))
                queue1.append((nx,ny))
                print('큐',queue,queue1)
                while True:
                    x,y = queue.popleft()
                    nx,ny = queue1.popleft()
                    print('xy',x,y)
                    print('nxny',nx,ny)
                    for k in range(4):#바꾼 후 상하좌우로 같은 단어 탐색
                        k1x = x + dx[i]
                        k1y = y + dy[i]
                        k2x = nx + dx[i]
                        k2y = ny + dy[i]
                        print('k1x,k1y',k1x,k1y)
                        print('k2x,k2y',k2x,k2y)
                        if k1y < 0 or k1y > n or k1x < 0 or k1x > n:
                            continue
                        if k2x < 0 or k2x > n or k2y < 0 or k2y > n:
                            continue
                        print('graph[k1y][k1x]graph[y][x]',graph[k1y][k1x],graph[y][x])
                        print('graph[k2y][k2x]graph[ny][nx]',graph[k2y][k2x],graph[ny][nx])
                        if graph[k1y][k1x] == graph[y][x]:
                            # 인접한 값이 같은 경우 count+=1
                            count1 += 1
                            count.append(count1)
                            #리턴으로 다음 값에 대해 같은지 수행
                            queue.append((k1y,k1x))

                        if graph[k2y][k2x] == graph[ny][nx]:
                            count2 += 1
                            count.append(count2)
                            queue1.append((k2y,k2x))
                            print('else 큐',queue, queue1)
                        #인접한 단어가 다른경우
                        else:
                            break
                print(max(count))
    return graph[n-1][n-1]

# bomboni(0,0)에서 시작, 재귀 사용 안됨!! 한 번만 단어 위치 옮겨야 하므로(여러번 해서 값을 받는게 아님)
bomboni(0,0)



