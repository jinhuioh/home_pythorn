# 문제
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다.
# 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.
#
# 출력
# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

#입력받을 숫자의 개수 입력하기
n = int(input())
# 값을 담을 리스트 생성
list1 = []
#키 벨류 형태의 map으로 input으로 받은 값들을, 모두 공백으로 잘라, 각각 int로 형변환해주자.
list1 = list(map(int, input().split(" ")))
# 처음 값으로 n_max. n_min을 지정
# list1의 값중에 최대 최소값을 n_max, n_min으로 지정
n_max = max(list1)
n_min = min(list1)

# for i in range(n):
#     n_min = min(list1[i])
#     n_max = max(list1[i])
#     # if -1000000<list1[i]<1000000:
#     #     if n_max < list1[i]:
#     #         n_max = list1[i]
#     #     n_min = list1[0]
#     #     if n_min > list1[i]:
#     #         n_min = list1[i]
print(n_min, n_max)
