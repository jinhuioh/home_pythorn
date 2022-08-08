# 숫자카드게임
# 여러개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
# 먼저 뽑고자 하는 카드가 포함된 행을 선택
# 해당 행 중에서 가장 숫자가 낮은 카드를 뽑아야한다.
# 최종적으로는 행에서 가장 숫자가 낮은 카드를 뽑을때 그 중에서 가장 크기가 큰 카드를 뽑아야한다.
#
# 입력조건
# 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어진다 (1<=N, M<=100).
# 둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1 이상 10000이하의 자연수이다.

# 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.

# 1.행렬 개수 입력
n,m = map(int, input().split())
# 2. nxm 행렬 입력
data = [map(int,input().split()) for _ in range(n)]
print('data',data)
# 3.행에서 가장 작은수들 중에서, 가장 큰 수 뽑기
i=0
min_list = []
for i in range(n):
    # 각 행에서 가장 작은 값 추출
    min_data = min(data[i])
    print('min_data',min_data)
    # 각 행에서 가장 작은 값만 리스트에 담아주기
    min_list.append(min_data)
    print('min_list',min_list)
    # 리스트 값 정렬(큰 수부터 오도록)
    min_list.sort(reverse=True)
    print('min_list정렬: ',min_list)
# 가장 작은 값들만 모아놓은 리스트에서 가장 큰 값 추출
print(min_list[0])