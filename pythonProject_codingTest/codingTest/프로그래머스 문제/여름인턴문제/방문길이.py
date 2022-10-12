# 게임 캐릭터를 4가지 명령어를 통해 움직이려 합니다. 명령어는 다음과 같습니다.
#
# U: 위쪽으로 한 칸 가기
#
# D: 아래쪽으로 한 칸 가기
#
# R: 오른쪽으로 한 칸 가기
#
# L: 왼쪽으로 한 칸 가기
#
# 캐릭터는 좌표평면의 (0, 0) 위치에서 시작합니다.
# 좌표평면의 경계는 왼쪽 위(-5, 5), 왼쪽 아래(-5, -5), 오른쪽 위(5, 5), 오른쪽 아래(5, -5)로 이루어져 있습니다.
# 이때, 우리는 게임 캐릭터가 지나간 길 중 캐릭터가 처음 걸어본 길의 길이를 구하려고 합니다.
# 예를 들어, "ULURRDLLU"로 명령했다면,
# 위의 예시에서 게임 캐릭터가 움직인 길이는 9이지만, 캐릭터가 처음 걸어본 길의 길이는 7이 됩니다.
# (8, 9번 명령어에서 움직인 길은 2, 3번 명령어에서 이미 거쳐 간 길입니다)
#
# 단, 좌표평면의 경계를 넘어가는 명령어는 무시합니다.

# 2시55




#0으로 된 행렬 리스트를 하나 만들어서 방문했으면 1로 바꿈 그리고 만약 이미 1이라면 pass

# 상하좌우xy리스트를 만들어주자.

#for문을 돌려 주어진 dirs만큼 이동시키면서 행렬리스트의 0의 값을 1로 바꿔줌

#행렬리스트sum=answer을 리턴해줌
# dirs="ULURRDLLU"
dirs = "LULLLLLLU"
path = [0] * 5
graph = []
for i in range(5):
    graph.append(path)
graph[1][1] =1
print(graph)



# path = [0] * 25
# graph = []
# for i in range(5):
#     graph.append(path)
# # graph[5*ny + nx] =1
# print(graph)


def solution(dirs):
    move = ['U', 'D', 'L', 'R']  # i값을 증가시키면서 이동시키기 위해 리스트에 담음
    dx = [0, 0, -1, 1]  # 좌우
    dy = [1, -1, 0, 0]  # 상하

    # path = [0]*25
    graph = [0]*50
    graph1 = [0]*50#홀수인경우
    # for i in range(5):
    #     graph.append(path)
    answer = 0
    x,y = 0,0#시작 위치
    for one in dirs:
        for i in range(4):#상하좌우탐색
            if move[i] == one:
                if x + dx[i] > 5 or x + dx[i] < -5 or y + dy[i] > 5 or y + dy[i] < -5:
                    continue
                x = x + dx[i]
                y = y + dy[i]
                # 좌표평면의 경계를 넘어가는 명령어 무시
                if x<0 or y<0:
                    graph1[abs(5*y) + abs(x)] =1
                else:
                    graph[5*y + x] =1
        print('x,y>> ',x,y)
        print('graph>> ',graph)
        print('graph1>> ',graph1)
    # for i in range(5):
    #     answer1 = sum(graph[i])
    #     answer += answer1
    answer = sum(graph)+sum(graph1)
    if graph[0] == 0 and graph1[0] == 0:
        answer+=1
    return answer

print(solution(dirs))