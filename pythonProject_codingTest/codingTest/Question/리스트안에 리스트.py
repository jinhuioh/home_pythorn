# 내가 원하는 건 0번째 리스트 안에 0번째 인덱스만 1로 바꾸는건데 실행해보면 모든 0번째인덱스가 1로 바뀌어있다.
#이유 : path를 10번 붙였으므로 graph[0][0] = 1로 바꾸면
#graph[0]이 path이므로 모든path의 [0]이 1로 바뀌게 된다.
path = [0] * 10
graph = []
for i in range(10):
    graph.append(path)
graph[0][0] = 1
print(graph,'\n')

# 해결방법
# 5번 [0,0,0,0,0]를 붙인 후 그 전체를 5번 반복한다, 총 25번의 list가 붙는다.
graph3 = []
for i in range(5):
    for k in range(5):
        graph3.append([0,0,0,0,0])
graph3[0][1] = 1
print('graph3',graph3,'\n')

# 해결방법
# 아래와 같이 list를 input()으로 받아 연산해준다.
graph2 = []
for i in range(3):
    graph2.append(list(map(int,input())))
graph2[0][1] = 1
print(graph2,'\n')

