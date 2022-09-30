# 문제
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
#
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다.
# 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.
#
# 출력
# 첫째 줄에 그룹 단어의 개수를 출력한다.

# n = int(input())
# list1 = []
# for i in range(n):
#     list1.append('*'+(input()))
# print(list1)
# result = n
#
# for one in list1:
#     for i in range(1,len(one)):
#         #one에는 happy, year등이 담긴다.
#         #i에는 h,a,p,p,y등이 각각 담긴다.
#         if one[i] == one[i-1]:
#             print(i,'번째랑 i-1이 같을때,one[i]',one[i])
#             print(i-1,'번째랑 i이 같을때,one[i-1]',one[i-1])
#             # result += 1
#             print('result더해주기',result)
#             pass
#         for j in range(i+1,len(one)):
#             # if one[i] == one[i-1]:
#             #     print(i,'번째랑 i-1이 같을때,one[i]',one[i])
#             #     print(i-1,'번째랑 i이 같을때,one[i-1]',one[i-1])
#             #     result += 1
#             #     print('result더해주기',result)
#             if one[i] == one[j]:
#                 print(i,'번째 단어가 j번째랑 같을때>> ',one[i])
#                 print(j,'번째 단어가 j번째랑 같을때, one[j]>>>',one[j])
#                 result -= 1
#                 print('result빼주기',result)
#
# print(result)

N = int(input())
cnt = N

for i in range(N):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break

print(cnt)



