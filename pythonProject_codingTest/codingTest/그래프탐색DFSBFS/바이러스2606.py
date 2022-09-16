# 신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다.
# 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

# 예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자.
# 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐
# 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다.
# 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.

# 총 컴퓨터 개수
n = int(input())
# 연결된 컴퓨터 쌍의 개수
m = int(input())
# false로 이루어진 행렬 생성(연결된 컴퓨터를 세기위함)
graph = []
visited = [False]*(n+1)#컴퓨터 개수만큼 flase생성
for i in range(n+1):#컴퓨터 개수 1부터 n개까지 graph객체에 리스트로 담기
    graph.append([])
print('graph1',graph)
print('visited',visited)
for _ in range(m):#연결된 컴퓨터 쌍의 개수 입력
    i,j = map(int, input().split())#2개씩 입력 받을 때 왼쪽i,오른쪽j
    graph[i].append(j)#i번째 행에 j번째 열을 생성
    if i not in graph[j]:
        graph[j].append(i)
        print('graph i append j',graph)
print('graph',graph)

def dfs(n):#1부터 시작하므로 n=1을 넣을 예정
    # 현재 컴퓨터에 방문처리
    visited[n] = True#1번 방문처리
    print('visitedTrue', visited)
    # 연결되어 있는 컴퓨터 하나씩 방문
    for i in graph[n]:#1번째 리스트에 담긴 (1과 연결된 수들)이 차례대로 i가 되어 for문을 돌도록 함
        if not visited[i]:#1과 연결된 컴퓨터들도 방문처리
            dfs(i)#재귀적으로 1과 연결된 컴퓨터들이 dfs함수를 돌도록 구현
dfs(1)
count =-1
for i in visited:
    if i:
        count+=1
print(count)