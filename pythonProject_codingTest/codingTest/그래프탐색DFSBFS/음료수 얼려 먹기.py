##DFS문제(입구와 출구가 같은 문제. 깊이탐색)
# n*m크기의 얼음틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다.
# 구멍이 뚫려 있는 부분끼리 상,하,좌,우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주합니다.
# 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.
# 입력조건
# 첫번째 줄에 얼음 틀의 세로 길이n과 가로길이m이 주어집니다.
# 두번째 줄부터 n+1번째 줄까지 얼음 틀의 형태가 주어집니다.
# 이때 구멍이 뚫려있는 부분은0 그렇지 않은 부분은 1 입니다.
# 출력조건
# 한 번에 만들 수 있는 아이스크림 개수를 출력합니다.
#

n,m = map(int,input().split())#세로가로
print(n,m)
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
print(graph)

def ice(y,x):
    # 범위를 벗어난다면
    if x>=m or x<=-1 or y<=-1 or y>=n:
        return False
    if graph[y][x] == 0:
        graph[y][x] = 1
        print(graph)
        ice(y+1,x)
        ice(y-1,x)
        ice(y,x+1)
        ice(y,x-1)
        return True
    return False

result = 0
for i in range(n):
    for k in range(m):
        if ice(i,k) == True:
            result += 1
print(result)














#
# 풀이방법: 특정 지점의 주변 상하좌우를 살펴본 뒤에 주변 지점 중에서 값이0이면서 아직 방문하지 않은 지점이 있다면 방문
# 방문한 지점에서 다시 상하좌우를 살펴보면서 방문을 진행하는 과정을 반복하면 연결된 모든 지점을 방문할 수 있다.
# 모든 노드에 대해 위에 방법 반복 그리고 지점의 수를 카운트
# #
#
# n,m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int,input())))
#
# def ice(x,y):#x가 열(가로), y가 행(세로)
#     if x<=-1 or x>=m or y<=-1 or y>=n:
#         return False
#     if graph[y][x] == 0:
#         graph[y][x] = 1
#         ice(x+1,y)
#         ice(x-1,y)
#         ice(x,y+1)
#         ice(x,y-1)
#         return True
#     return False
# result =0
# for a in range(n):
#     for b in range(m):
#         if ice(a,b) == True:
#             result+=1
#
# print(result)






#
# # dfs함수 만들기
# # dfs로 특정 노드를 방문하고 연결된 모든 노드들도 연결
def dfs(x,y):
    #     주어진 범위를 벗어나는 경우 종료
    if x<=-1 or x>=n or y <=-1 or y>=m:
        return False
    # 현재 노드를 아직 방문하지 않은 경우
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상하좌우 위치들도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        # return = 결과값을 돌려주는 명령어
        # graph[x][y] == 1 에 대해 return True로 결과값을 반환
        return True
    # dfs()함수를 재귀적으로 호출하는 경우에 대해서는 결과값을 리턴할 필요가 없으므로 False를 반환한다.
    return False

# 얼음틀 입력받기
n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
# graph = [map(int, input()) for _ in range(n)]
# print(graph)

# 모든 노드에 대해 음료수 채우기
result = 0
for i in range(n):#행
    for j in range(m):#열
        # 현재 위치에서 dfs 수행
        #dfs()함수가 True인 경우에 대해 result값을 증가시킨다.
        if dfs(i,j) == True:
            result +=1
print(result)


#
# n,m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
# def ice(x,y):
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     if graph[x][y] == 0:
#         graph[x][y] == 1
#         ice(x-1, y)
#         ice(x, y-1)
#         ice(x+1, y)
#         ice(x, y+1)
#         return True
#     return False
# result = 0
# for i in range(n):
#     for j in range(m):
#         if ice(i,j) == True:
#             result +=1
# print(result)