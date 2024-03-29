# 문제
# 여러분도 알다시피 여러분의 프린터 기기는 여러분이 인쇄하고자 하는 문서를 인쇄 명령을 받은 ‘순서대로’,
# 즉 먼저 요청된 것을 먼저 인쇄한다. 여러 개의 문서가 쌓인다면 Queue 자료구조에 쌓여서
# FIFO - First In First Out - 에 따라 인쇄가 되게 된다. 하지만 상근이는 새로운 프린터기 내부 소프트웨어를 개발하였는데,
# 이 프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다.
#
# 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
# 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면,
# 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
# 예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고,
# 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.
#
# 여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때,
# 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.
#
# 입력
# 첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.
#
# 테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 몇 번째로 인쇄되었는지 궁금한 문서가
# 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다. 이때 맨 왼쪽은 0번째라고 하자.
# 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 중요도는 1 이상 9 이하의 정수이고,
# 중요도가 같은 문서가 여러 개 있을 수도 있다.
#
# 출력
# 각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.

# 입력
# 3
# 1 0
# 5
# 4 2
# 1 2 3 4
# 6 0
# 1 1 9 1 1 1

# 출력
# 1
# 2
# 5

## 최신 수정
## 아래와 같은 방법으로 풀면(pop(0), insert(0,x)등 사용) 무작위 접근에 최적화된 자료인 list에 의해
## 시간복잡도가 o(n) = 선형시간(n이커질때 n에 비례해서 연산횟수 증가)이 되므로 비효율적이다.

## deque의 popleft()와 appendleft(x)메서드는 모두 O(1)의 시간복잡도로 매우 효율적으로 문제를 해결할 수 있다.
# appendleft(x) = append(list_imp[x][0])와 같은 효과로 첫번째 인덱스에 원소를 입력할 수 있다.

from collections import deque

k = int(input())
n_index = []
n_num = []
n_imp = []

for i in range(k):
    m, n = map(int, input().split())
    n_num.append(n)
    n_imp.append(list(map(int, input().split())))
    n_index.append(list(l for l in range(len(n_imp[i]))))
    n_index[i][n] = "t"
def printerQueue(n_imp,n_index):
    for x in range(k):
        n_impX = n_imp[x]
        n_indexX = n_index[x]
        count = 0# 프린트 수 초기화
        queue_imp = deque()
        queue_index = deque()
        queue_imp = deque(n_impX)# 큐 초기화 하여
        queue_index = deque(n_indexX)# 큐 초기화 하여
        while queue_imp:# queue_imp에 대해 while문 돌리기
            a = (queue_imp.popleft())
            b = queue_index.popleft()
            if a == max(n_impX) and b == "t":
                count+=1
                print(count)
                break
            elif a == max(n_impX):
                n_impX.remove(a)
                n_indexX.remove(b)
                count+=1
            else:
                queue_imp.append(a)
                queue_index.append(b)
printerQueue(n_imp,n_index)


# from collections import deque
#
# k = int(input())
# n_index = []
# n_num = []
# n_imp = []
#
# for i in range(k):
#     m, n = map(int, input().split())
#     n_num.append(n)
#     n_imp.append(list(map(int, input().split())))
#     n_index.append(list(l for l in range(len(n_imp[i]))))
#     n_index[i][n] = "t"
# print(n_index)
# print(n_imp)
#
# def printerQueue(n_imp,n_index):
#     for x in range(k):
#         n_impX = n_imp[x]
#         n_indexX = n_index[x]
#         count = 0# 프린트 수 초기화
#         queue_imp = deque()
#         queue_index = deque()
#         queue_imp = deque(n_impX)# 큐 초기화 하여
#         queue_index = deque(n_indexX)# 큐 초기화 하여
#         while queue_imp:# queue_imp에 대해 while문 돌리기
#             # 첫번째 인덱스 수 꺼내기
#             a = (queue_imp.popleft())
#             b = queue_index.popleft()
#             print('ab>> ',type(a),type(b),a,b)
#             #정답일시
#             if a == max(n_impX) and b == "t":
#                 count+=1
#                 print('답!! ',count)
#                 break
#             #찾고있는 target은 아니지만 max값인 경우
#             elif a == max(n_impX):
#                 # n_imp에서 최대값 삭제
#                 n_impX.remove(a)
#                 n_indexX.remove(b)
#                 count+=1
#                 print('count 증가 시키고 최대값 지우기',count)
#             #target도 max도 아닌경우
#             else:
#                 queue_imp.append(a)
#                 queue_index.append(b)
#                 print('else append', queue_imp)
#                 print('else append',queue_index)
#
# printerQueue(n_imp,n_index)
#



# ### 문제 풀었을때 느낀점
# ### 리스트에서 값을 꺼내고 없애고 옮기는 문제는
# ### 값을 지우는 과정에서 index가 계속 변하기 때문에 잘생각하고 로직을 짜야할 것 같다.
# k = int(input())
# list_nm = []#문서의 개수 n과 몇번째 인쇄 값이 궁금한지 나타내는 m값을 담을 리스트
# list_imp = []#중요도 입력받을 리스트
# list_idx = []#입력받은 중요도의 인덱스를 담을 리스트
# for i in range(k):
#     n,m = list(map(int, input().split(" ")))
#     list_nm.append(m)
#     list_imp.append(list(map(int, input().split(" "))))
#     list_idx.append(list(range(len(list_imp[i]))))
#     list_idx[i][m] = 'target' #(인덱스에서 m번째 값을 target으로 지정)
# for x in range(k):
#     count = 0 #카운트는 for문을 돌때마다 초기화 해준다.
#     while True:
#         #첫번째 값이 최대값인데 해당값의 index가 target(우리가 답으로 출력해야 할 값)인 경우
#         if list_imp[x][0] == max(list_imp[x]) and list_idx[x][0] == 'target':
#             #최대값인 경우 첫번째 값(최대값)을 제거
#             list_imp[x].pop(0)
#             #인덱스도 맞춰줘야 하기 때문에 같이 제거
#             list_idx[x].pop(0)
#             #제거했으므로 count+=1(m번째 값을 출력했을 때, 몇번째 출력인지 구해야하므로 최대값을 없앨때마다 카운트를 증가시켜준다.)
#             count += 1
#             #답 출력
#             print(count)
#             #답이 나왔으므로 break로 while문을 멈춰준다. 다음 x에 대해 while문을 실행시킨다.
#             break
#         # 0번째 값이 최대값이지만 index가 target은 아닌경우
#         elif list_imp[x][0] == max(list_imp[x]):
#             # 각 첫번째 값 제거 후 count+=1을 해준다.
#             list_imp[x].pop(0)
#             list_idx[x].pop(0)
#             count += 1
#         else:
#             # 0번째 값이 최대값도 아니고, index가 target도 아닌 경우
#             # 각 0번째 값을 append로 마지막에 붙여준다.
#             # 그 후 0번째 값을 지워준다.
#             # 0번째 값을 먼저 지우고 append를 실행하면 list_imp[x][0]값이 이미 지워서 두번째 값이 들어가므로 오류가 발생한다. 주의하자!!
#             list_imp[x].append(list_imp[x][0])
#             list_idx[x].append(list_idx[x][0])
#             list_imp[x].pop(0)
#             list_idx[x].pop(0)