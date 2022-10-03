# 문제
# 나코더 기장 재민이는 동아리 회식을 준비하기 위해서 장부를 관리하는 중이다.
#
# 재현이는 재민이를 도와서 돈을 관리하는 중인데, 애석하게도 항상 정신없는 재현이는 돈을 실수로 잘못 부르는 사고를 치기 일쑤였다.
#
# 재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킨다.
#
# 재민이는 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다. 재민이를 도와주자!
#
# 입력
# 첫 번째 줄에 정수 K가 주어진다. (1 ≤ K ≤ 100,000)
#
# 이후 K개의 줄에 정수가 1개씩 주어진다. 정수는 0에서 1,000,000 사이의 값을 가지며,
# 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.
#
# 정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.
#
# 출력
# 재민이가 최종적으로 적어 낸 수의 합을 출력한다. 최종적으로 적어낸 수의 합은 2^31-1보다 작거나 같은 정수이다.

# 예
# 4
# 3
# 0
# 4
# 0
# 출력: 0
import time
k = int(input())
num_list1 = []#입력값을 담을 리스트
num_list = []#입력값을 담은 리스트 값 중 최종적으로 더할 값만 넣을 리스트
for i in range(k):
    num_list1.append(int(input()))# 입력값 리스트에 저장

for i in range(k):
    if num_list1[i] != 0:#입력값에 저장 된 값 중 0이 아니면 최종 더할 값에 넣기
        num_list.append(num_list1[i])
    else:#0이면 이전 값 지우기(remove쓰면 인덱스가 달라지는데 리스트 길이가 줄어들어 인덱스 오류가 난다.)
        num_list.pop()#마지막 값 제거
print(sum(num_list))#최종적으로 더한 값 프린트

## 오류 고치기 
## num_list에 input받아서 받을 때마다 0인지 아닌지 처리해서 sum구하는 방법으로 풀었는데, 
## 입력받는 시간이 있다보니 시간초과 오류나서
## num_list1에 입력값 전부 받고, num_list에 처리할 값 넣는걸로 나누어 처리함! => 시간초과 없앰
