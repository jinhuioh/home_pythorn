## 개미 전사는 부족한 식량을 충당하고자 메뚜기 마을의 식량창고를  공격할 예정
# 식량창고는 일직선으로 이어져있다.
# 각 식량창고에는 정해진 수의 식량을 저장하고 있으며 개미전사는 식량창고를 선택적으로 약탈하여 식량을 뺏을 예정
# 이때 메뚜기 정찰병들은 일직선상에 존재하는 식량창고 중에서 서로 인접한 식량창고가 공격받으면 바로 알아챌 수 있다.
# 따라서 개미 전사가 정찰병에게 들키지 않고 식량창고를 약탈하기 위해서는
# 최소한 한 칸 이상 떨어진 식량창고를 약탈해야한다.
# 예시: 1 3 1 5
# 이때 개미전사는 두번째와 네번째 식량창고를 선택했을 때 총 8개의 식량을 뺏을 수 있다.
# 개미전사를 위해 식량창고 n개에 대한 정보가 주어졌을 때 얻을 수 있는 식량의 최댓값을 구하는 프로그램을 작성하세요
#
# 입력조건: 첫째 줄에 식량창고 개수n이 주어진다.(3~100사이)
#           둘째 줄에 공백을 기준으로 식량창고에 저장된 식량의 개수 k가 주어진다.(0~1000)
# 출력조건: 첫째 줄에 개미 전사가 얻을 수 있는 식량의 최댓값을 출력하세요

# 2n 인덱스를 선택할지 2n-1인덱스를 선택할지 반복적으로 작업해야하고, 최적의 해를 구해야하므로 다이나믹 알고리즘을 사용해보자.

# 식량창고 개수 n입력받기
n = int(input())
k = list(map(int, input().split()))
# 초기화한 0으로 이루어진 리스트(최적의 해를 d에 넣을것이기 때문에 최대 101개까지 0을 생성한다.
d = [0]*101
d[0] = k[0]
d[1] = max(k[0], k[1])
for i in range(2,n):#n-1까지만 연산하면 되므로 2부터 n까지 range한다.(d의 인덱스가 0부터 시작하므로)
    d[i] = max(d[i-1], d[i-2]+k[i])
print(d[n-1])#n-1까지만 하는 이유는 k의 인덱스가 0부터 시작하기 때문이다.