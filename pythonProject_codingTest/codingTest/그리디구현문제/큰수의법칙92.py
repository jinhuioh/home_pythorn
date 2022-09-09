# 큰 수의 법칙
# N개의 수 를 입력, 입력 받은 수들을 M번 더했을 때 가장 큰 결과 출력, 단 더할때 K번 초과하여 같은수를 더하는것은 불가능.
# 첫째 줄에 N(2<=N<=1000), M(1<=M<=10000), K(1<=K<=10000)의 자연수가 주어지며 각 자연수는 공백으로 구분한다.
# 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단 각각의 자연수는 1이상 10000이하의 수로 주어진다.
# 입력으로 주어지는 K는 항상 M보다 작거나 같다
# 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다

#3개의 값 한줄로 입력받기
N, M, K = map(int,input().split())
# N개의 수 입력받기. list로 한번에 N개 담음
data = list(map(int,input().split()))
print(data)

# 큰수부터 M번 더하고, K초과 중복 안됨
#   i 값 중 가장 큰 값을 찾아보자.
# 값 중복 없에고 내림차준으로 정렬해서 차례대로 큰 수 더하기

def set_list(x):
    set_data = set(x)
    sorted_data = sorted(set_data, reverse=True)#내림차순
    # print(sorted_data)
    return sorted_data
result1 = 0
result2 = 0
i =0
# M의 크기에 따라 다르게 계산
for i in range(K):
    if M==0:
        break
    if M<2:
        # sum_data는 i번째 큰 수
        sum_data = set_list(data)[i]
        # i번째 큰 수를 result1로 지정
        result1 += sum_data
        print('result1', result1)
        print('i1', i)
        # M에서 1빼줌
        M -= 1
    else:# M이 3이상인경우
        sum_data = set_list(data)[i]
        # K개수를 i번째 큰 수에 곱한것을 result2객체에 넣음
        result2 = sum_data*K
        print('result2', result2)
        print('i2',i)
        # M에서 K개수만큼 빼줌
        M = M-K
print(result1+result2)

# i=0
# t=0
# n=0
# # M번 더함. K번 초과안함
# while i<M+1:
#     if i>M:
#         break
#     sum_data = set_list(data)[i]
#     print('set: ', sum_data)
#     i = i+1
# sum_data += sum_data
# print('setLast: ', sum_data)
#
#
#


