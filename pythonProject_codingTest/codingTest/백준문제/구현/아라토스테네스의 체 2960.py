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

# 큐를 이용하여 첫인덱스부터 값을 보고 소수의 배수값이면 popleft 아니면 append를 통해 문제를 품

n,k = map(int,input().split())
queue = deque()# 고정인덱스
queuelist = deque()# 배수값이면 popleft 아니면 append를 할 큐 리스트
for i in range(2,n+1):
    queuelist.append(i)
    queue.append(i)

count = 0#배수 값을 삭제할 때마다 카운트를 증가시켜 카운트가 k와 같아지면 print
while queuelist:#queue가 없어질때까지 while문 돌리기
    # one의 배수 전부 없애고 indexlist를 1씩 증가시키기
    qpop = queuelist[0]
    # print('qpop!!',qpop)
    for one in queue:#queue값은 변화하지 않는다.(변화하는 값으로 for문을 돌릴 수 없음)
        # 만약 one이 queue에 있지만 queuelist에 없는 값이면 pass
        # (예를들어 2를이미 지웠는데 queue에는 있으므로 popleft할 때 인덱스 순서가 맞지 않는다.)
        if one in queuelist:
            # one을 소수로 나누었을 때 0이면(소수의 배수이면)
            if one % qpop  == 0 :
                # 카운트 증가
                count += 1
                # 해당 배수 값 삭제
                queuelist.popleft()
                # 카운트 값이 k와 같다면 one이 답이므로 출력
                if count == k:
                    print(one)
                    # 답이 나왔으므로 break
                    break
            else:
                # one이 소수의 배수가 아니면 꺼내서 맨 뒤로 붙여준다.
                queuelist.append(queuelist.popleft())
        else:
            pass

