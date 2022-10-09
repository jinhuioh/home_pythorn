# 문제
# 에라토스테네스의 체는 N보다 작거나 같은 모든 소수를 찾는 유명한 알고리즘이다.
#
# 이 알고리즘은 다음과 같다.
#
# 2부터 N까지 모든 정수를 적는다.
# 아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
# P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
# 아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.
# N, K가 주어졌을 때, K번째 지우는 수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ K < N, max(1, K) < N ≤ 1000)
#
# 출력
# 첫째 줄에 K번째 지워진 수를 출력한다.
#
# 예제 입력 1
# 7 3
# 예제 출력 1
# 6

#9:50
#11:12
from collections import deque

n,k = map(int,input().split())
indexList = []
queue = deque()
queuelist = deque()
for i in range(2,n+1):
    queuelist.append(i)
    queue.append(i)
    indexList.append(i)
# print('queuelist',queuelist)

count = 0
while queuelist:#queue가 없어질때까지 while문 돌리기
    # one의 배수 전부 없애고 indexlist를 1씩 증가시키기
    qpop = queuelist[0]
    # print('qpop!!',qpop)
    for one in queue:
        if one in queuelist:
            # print('pone,queuelist>> ','꺼낸거qpop',qpop,'pone',queuelist,'one',one)
            if one % qpop  == 0 :
                count += 1
                queuelist.popleft()
                # print('count k>>>>>>>>>>>',count,k)
                if count == k:
                    # print('count k',count,k)
                    print(one)
                # print('queuelist>>if ',queuelist)
            elif len(queuelist) == 0:
                    break
            else:
                queuelist.append(queuelist.popleft())
                # print('queuelist>>else ',queuelist)
        else:
            pass

