# 18분걸림
# 문제
# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다.
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
#
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
#
# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다.
# 문자열은 O와 X만으로 이루어져 있다.
# 출력
# 각 테스트 케이스마다 점수를 출력한다.
n = int(input())
array = []
for i in range(n):
    array.append(list(input()))
print(array)

for i in range(n):
    count = [0]*80
    array_one = array[i]
    if array_one[0] == 'O':
        count[0] = 1
    else:
        count[0] = 0
    for k in range(1, len(array[i])):
        if array_one[k-1] == 'O' and array_one[k] == 'O':
            count[k] = count[k-1] + 1
            print('이전에o이고 지금도 o인 경우',count)
        if array_one[k - 1] == 'X' and array_one[k] == 'O':
            count[k] = 1
            print('이전에x이고 지금 o인 경우:',count)
    print(sum(count),'\n')


# 제출한 답
# n = int(input())
# array = []
# for i in range(n):
#     array.append(list(input()))
# for i in range(n):
#     count = [0]*80
#     array_one = array[i]
#     if array_one[0] == 'O':
#         count[0] = 1
#     else:
#         count[0] = 0
#     for k in range(1, len(array[i])):
#         if array_one[k-1] == 'O' and array_one[k] == 'O':
#             count[k] = count[k-1] + 1
#         if array_one[k - 1] == 'X' and array_one[k] == 'O':
#             count[k] = 1
#     print(sum(count))