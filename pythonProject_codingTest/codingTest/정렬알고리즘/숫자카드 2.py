# 문제
# 숫자 카드는 정수 하나가 적혀져 있는 카드이다.
# 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때,
# 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다.
# 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
#
# 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다.
# 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다.
# 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
# 출력
# 첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.
#
# 예제 입력 1
# 10
# 6 3 2 10 10 10 -10 -10 7 3
# 8
# 10 9 -5 2 3 4 5 -10
# 예제 출력 1
# 3 0 0 1 2 0 0 2

#이진탐색으로 했는데 시간초과남 ㅜㅜ
# from sys import stdin
# n = int(stdin.readline())
# n_num = list(map(int, stdin.readline().split()))
# #시간초과를 피하기 위해 set과 sorted로 중복제거, 크기순으로 재배치 함.
# n_set_sort = sorted(set(n_num))
# # print(n_set_sort)
#
# m = int(stdin.readline())
# m_num = list(map(int, stdin.readline().split()))
#
# def num(start, end, m_one, n_set_sort):
#     # print('start_end============================',start,end)
#     if start > end:
#         return 0
#     #중간값 인덱스
#     mid = (start+end)//2
#     # print('mid',mid)
#     # print('m_one> ',m_one)
#     # print('n_set_sort[mid]',n_set_sort[mid])
#     if n_set_sort[mid] == m_one:
#         count_n_num = n_num.count(m_one)
#         return count_n_num
#     elif n_set_sort[mid] > m_one:
#         return num(start, mid-1, m_one, n_set_sort)
#     else:
#         # print('else>>', m_one)
#         return num(mid+1, end, m_one, n_set_sort)
#
# for m_one in m_num:
#     start = 0
#     end = len(n_set_sort)-1
#     print(num(start, end, m_one, n_set_sort),end=" ")


# 위에 시간초과 나서 다른 방법으로 구현
#Counter함수 사용! 리스트를 값으로 주게 되면 해당 원소들이 몇 번
# 등장했는지 세어 딕셔너리 형태로 반환해주는 함수이다.

from collections import Counter
from sys import stdin
n = int(stdin.readline())
n_num = list(map(int, stdin.readline().split()))

m = int(stdin.readline())
m_num = list(map(int, stdin.readline().split()))

count = Counter(n_num)

for i in range(len(m_num)):
    if m_num[i] in count:
        print(count[m_num[i]], end=" ")#count[k]를 입력하면 k가 몇 번 등장하는지를 반환해줌
    else:
        print(0,end=" ")