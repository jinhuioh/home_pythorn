# 깊이를 우선으로 하여 탐색하는 알고리즘
graph = [
    [],#1번부터 시작하는 경우가 많기 때문에, 0번째 인덱스는 빈 리스트로 냅두자.
    [2, 3, 8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False]*9
# dfs 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드가 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[v]:
            dfs(graph, i, visited)

dfs(graph,1,visited)