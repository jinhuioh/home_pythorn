# 문제
# N×M크기의 직사각형이 있다. 각 칸에는 한 자리 숫자가 적혀 있다.
# 이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램을 작성하시오.
# 이때, 정사각형은 행 또는 열에 평행해야 한다.
#
# 입력
# 첫째 줄에 N과 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 수가 주어진다.
#
# 출력
# 첫째 줄에 정답 정사각형의 크기를 출력한다.
# 예제 입력 1
# 3 5
# 42101
# 22100
# 22101
# 예제 출력 1
# 9

# 9시30분
#10시 13분
n,m = map(int,input().split())#세로 가로 입력
graph = []
same_list = []#꼭지점이 같은 사각형 크기를 모은 것
for i in range(n):
    graph.append(list(map(int,input())))

def square(x,y):
    i = 0
    while True:
        if n == 1 or m == 1:
            same_list.append(1)
            break
        print('i>> ', i)
        print('x,y//',x,y)
        # #i가 graph범위를 벗어난다면 continue
        # if y>n or y<0 or x>m or x<0:
        #     continue
        if x == m-1 or y == n-1:
            print('xy가 범위를 벗어남!!break')
            break
        # i가 n,m이면 break
        if i+y>=n or i+x>=m:
            print('continue',i+y,i+x)
            break

        num1 = graph[y+i][x]
        num2 = graph[y][x+i]
        num3 = graph[y+i][x+i]
        print('graph,num=======',graph[y][x],num1,num2,num3)

        if graph[y][x] == num1 and num1 == num2 and num2 == num3:
            same_list.append((i+1)*(i+1))
            print('same_list',same_list)
        i += 1


#x,y증가
for i in range(n):
    for k in range(m):
        square(k,i)
print('답//>>',max(same_list))#꼭지점이 같은 사각형 크기를 모은 것 중에 최대값




n,m = map(int,input().split())#세로 가로 입력
graph = []
same_list = []#꼭지점이 같은 사각형 크기를 모은 것
for i in range(n):
    graph.append(list(map(int,input())))

def square(x,y):
    i = 0
    while True:
        if n == 1 or m == 1:
            same_list.append(1)
            break
        # #i가 graph범위를 벗어난다면 continue
        # if y>n or y<0 or x>m or x<0:
        #     continue
        if x == m-1 or y == n-1:
            break
        # i가 n,m이면 break
        if i+y>=n or i+x>=m:
            break

        num1 = graph[y+i][x]
        num2 = graph[y][x+i]
        num3 = graph[y+i][x+i]

        if graph[y][x] == num1 and num1 == num2 and num2 == num3:
            same_list.append((i+1)*(i+1))
        i += 1


#x,y증가
for i in range(n):
    for k in range(m):
        square(k,i)
print(max(same_list))#꼭지점이 같은 사각형 크기를 모은 것 중에 최대값