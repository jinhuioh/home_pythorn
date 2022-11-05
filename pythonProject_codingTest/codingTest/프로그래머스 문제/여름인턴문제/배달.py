# 문제 설명
# N개의 마을로 이루어진 나라가 있습니다.
# 이 나라의 각 마을에는 1부터 N까지의 번호가 각각 하나씩 부여되어 있습니다.
# 각 마을은 양방향으로 통행할 수 있는 도로로 연결되어 있는데, 서로 다른 마을 간에 이동할 때는 이 도로를 지나야 합니다.
# 도로를 지날 때 걸리는 시간은 도로별로 다릅니다. 현재 1번 마을에 있는 음식점에서 각 마을로 음식 배달을 하려고 합니다.
# 각 마을로부터 음식 주문을 받으려고 하는데, N개의 마을 중에서 K 시간 이하로 배달이 가능한 마을에서만 주문을 받으려고 합니다.
# 다음은 N = 5, K = 3인 경우의 예시입니다.
# 위 그림에서 1번 마을에 있는 음식점은 [1, 2, 4, 5] 번 마을까지는 3 이하의 시간에 배달할 수 있습니다.
# 그러나 3번 마을까지는 3시간 이내로 배달할 수 있는 경로가 없으므로 3번 마을에서는 주문을 받지 않습니다.
# 따라서 1번 마을에 있는 음식점이 배달 주문을 받을 수 있는 마을은 4개가 됩니다.
# 마을의 개수 N, 각 마을을 연결하는 도로의 정보 road, 음식 배달이 가능한 시간 K가 매개변수로 주어질 때,
# 음식 주문을 받을 수 있는 마을의 개수를 return 하도록 solution 함수를 완성해주세요.
# 제한사항
# 마을의 개수 N은 1 이상 50 이하의 자연수입니다.
# road의 길이(도로 정보의 개수)는 1 이상 2,000 이하입니다.
# road의 각 원소는 마을을 연결하고 있는 각 도로의 정보를 나타냅니다.
# road는 길이가 3인 배열이며, 순서대로 (a, b, c)를 나타냅니다.
# a, b(1 ≤ a, b ≤ N, a != b)는 도로가 연결하는 두 마을의 번호이며,
# c(1 ≤ c ≤ 10,000, c는 자연수)는 도로를 지나는데 걸리는 시간입니다.
# 두 마을 a, b를 연결하는 도로는 여러 개가 있을 수 있습니다.
# 한 도로의 정보가 여러 번 중복해서 주어지지 않습니다.
# K는 음식 배달이 가능한 시간을 나타내며, 1 이상 500,000 이하입니다.
# 임의의 두 마을간에 항상 이동 가능한 경로가 존재합니다.
# 1번 마을에 있는 음식점이 K 이하의 시간에 배달이 가능한 마을의 개수를 return 하면 됩니다.

##!!!!! 다익스트라(Dijkstra)알고리즘 풀이방법
# 1. 출발 노드를 설정
# 2. 출발 노드를 기준으로 각 노드의 최소 비용을 저장 minCost = []함수 생성
# 3. 방문하지 않은 노드 중에서 가장 비용이 적은 노드를 선택
# 4. 해당 노드를 거쳐서 특정한 노드로 가는 경우를 고려하여 최소 비용 갱신
# 5. 위과정 3-4반복





















import heapq
from collections import deque

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3

# def solution(N,K,road):
#     min_list = [float('inf') for _ in range(N + 1)]
#     road_list = [[] for _ in range(N + 1)]
#     for r in road:
#         road_list[r[0]].append((r[1],r[2]))
#         road_list[r[1]].append((r[0],r[2]))
#
#     # 거리 갱신
#     heap = []
#     heapq.heappush(heap,[1,0])# 1로 갈 때 거리가 0 인 초기값
#     while heap:
#         road, node = heapq.heappop(heap)
#         for rr,nn in road_list[road]:
#             if min_list[rr] > int(nn) + int(node):
#                 min_list[rr] =int(nn) + int(node)
#                 heapq.heappush(heap,[rr, int(nn) + int(node)])
#     return len([i for i in min_list if i<=K])
#
# print(solution(N,K,road))

def solution(N,K,road):
    min_list = [float('inf') for _ in range(N + 1)]
    road_list = [[] for _ in range(N + 1)]
    for r in road:
        road_list[r[0]].append((r[1],r[2]))
        road_list[r[1]].append((r[0],r[2]))

    # 거리 갱신
    queue = deque([1,0])
    while queue:
        road = queue.popleft()
        node = queue.popleft()
        for rr,nn in road_list[road]:
            if min_list[rr] > int(nn) + int(node):
                min_list[rr] =int(nn) + int(node)
                queue.appendleft(int(nn) + int(node))
                queue.appendleft(rr)
    return len([i for i in min_list if i<=K])

print(solution(N,K,road))



# #
# N = 5
# road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
# K = 3

# 최단 거리 갱신할 함수
# def dijkstra(roadList, minList):
#     heap = []
#     heapq.heappush(heap,[0,1])# 최단 거리가 0, 1로 갈 때
#     while heap:
#         cost, node = heapq.heappop(heap)#예를들어 node가 2라면, 2까지 왔을때의 최단거리=cost
#         for c,n in roadList[node]:#2에서의 이동값들 예를들어 [1,3]이면 2에서 3으로 이동할 때 거리가 1이라는 의미.
#             if cost + c < minList[n]:#기존의 3까지 갈때의 최소값이 들어있는 minList[3]보다
#                                     # 2까지왔을때의 최단거리인 cost에, 2에서 3으로 갈때의 값인 c의 합이 더 작으면 그 값으로 갱신
#                 minList[n] = cost + c
#                 #힙에 최단거리로 이동한 값을 넣어주자.
#                 heapq.heappush(heap,[cost + c, n])
#
# def solution(N,K,road):
#     minList = [float('inf') for _ in range(N+1)]
#     roadList = [[] for _ in range(N+1)]# 각 인덱스에 이동거리와 좌표(노드)넣을 리스트 생성
#     for r in road:
#         roadList[r[0]].append([r[2],r[1]])
#         roadList[r[1]].append([r[2],r[0]])
#         print(r,roadList)
#         # 갱신할 함수 생성
#     dijkstra(roadList, minList)
#     #k보다 거리가 작거나 같은 값들만 출력
#     return len([i for i in minList if i <= K])
#
# print(solution(N,K,road))





# 이전꺼 합해서 answer세기
# k보다 작거나 같으면 answer+=1
# heapq란 자료구조 queue의 일종으로, queue의 내부 구조가 heap으로 이루어져 있다.
# def dijkstra(dist, adj):
#     heap = []
#     #heap리스트에 [0,1]을 넣겠다는 의미
#     heapq.heappush(heap, [0,1])#거리,노드(위치)#1번으로 가는 거리 0.
#     print('힙1>>>',heap)
#     while heap:
#         cost,node = heapq.heappop(heap)#아래에서 넣었던 [최소거리, 위치]를 꺼내서 해당 위치를 중심으로 아래 while문을 돈다.
#         print('cost,node >>>',cost, node)#거리,위치
#         for c, n in adj[node]:# node가 1이면 adj의 1번째 리스트로 for문 돌림.
#             print('for문 cost,node >>>', c, n,'adj[node]>>',adj[node])  # 거리,위치
#
#             if cost + c < dist[n]:#c는 거리 cost는 기존거리(거쳐간 거리), dist는 갱신하고 있는 list
#                 print('c(거리)는>',c,'cost + c(총 거리)>> ',cost + c,'n(위치)은> ',n,'dist[n]>> ',dist[n])
#                 dist[n] = cost + c
#                 heapq.heappush(heap, [cost+c, n])#최소거리와 위치 heap에 넣기.
#                 print('갱신!! dijkstra dist>>> ',dist)
#
#
# def solution(N, road, K):
#     dist = [float('inf')]*(N+1) #dist 배열 만들고 최소거리 갱신
#     print('dist>> ',dist)
#     dist[1] = 0 #1번은 자기자신이니까 거리 0
#     adj = [[] for _ in range(N+1)]# 빈 리스트 생성! 인접노드 & 거리 기록할 배열
#     for r in road:
#         adj[r[0]].append([r[2], r[1]])#예)[1,4,2]이면, 1번째 리스트에 [2,4]를 append(1에서 4로 이동할 때 거리 2 라는 의미)
#         adj[r[1]].append([r[2], r[0]])#예)[1,4,2]이면, 4번째 리스트에 [2,1]를 append(4에서 1로 이동할 때 거리가 2라는 의미)
#         print('adj>> ','r[0],r[1]>>',r[0],r[1],'[r[2], r[1]]>>',[r[2], r[1]],adj)
#     dijkstra(dist,adj)
#     return len([i for i in dist if i <= K])

# print(solution(N, road, K))



