# 내가 원하는 건 0번째 리스트 안에 0번째 인덱스만 1로 바꾸는건데 실행해보면 모든 0번째인덱스가 1로 바뀌어있다.
path = [0] * 10
graph = []
for i in range(10):
    graph.append(path)
graph[0][0] = 1
print(graph)