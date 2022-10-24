# 별그리기 문제
import math
from collections import deque
from sys import stdin
# <code>---------------------------------------------------------------------
# n = int(stdin.readline())
#
# star = '*'
# for i in range(n):
#     print(star)
#     star = star + '*'


# new============================================================================================================
#최대값 찾기
# 문제
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
#
# 예를 들어, 서로 다른 9개의 자연수
#
# 3, 29, 38, 12, 57, 74, 40, 85, 61
#
# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.
#
# 입력
# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.
#
# 출력
# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.
#
# 예제 입력 1
# 3
# 29
# 38
# 12
# 57
# 74
# 40
# 85
# 61
# 예제 출력 1
# 85
# 8
# <code>---------------------------------------------------------------------
# numlist = []
# for i in range(9):
#     numlist.append(int(stdin.readline()))
# #최대값의 인덱스를 찾아보서 출력해주자.
# print(max(numlist))
# print(numlist.index(max(numlist))+1)#인덱스가 0부터 시작하므로 +1을 해준다.


# new============================================================================================================
# 문자열반복
# 문제
# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.
#
# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다.
#
# 출력
# 각 테스트 케이스에 대해 P를 출력한다.
#
# 예제 입력 1
# 2
# 3 ABC
# 5 /HTP
# 예제 출력 1
# AAABBBCCC
# /////HHHHHTTTTTPPPPP

# <code>---------------------------------------------------------------------
# n = int(stdin.readline())#총 문자들의 개수
# for i in range(n):
#     r,p = map(str, stdin.readline().split())#반복할 숫자 횟수와 문자
#     pr = ''
#     for p_one in p:
#         for i in range(int(r)):
#             pr += p_one
#     print(pr)
#
#
# n = int(stdin.readline())#총 문자들의 개수
# for i in range(n):
#     r,p = map(str, stdin.readline().split())#반복할 숫자 횟수와 문자
#     for p_one in p:
#         print(p_one*int(r),end='')#end연산자를 통해 그 뒤의 출력값과 이어서 출력한다. (즉, 줄바꿈을 하지 않게 된다.)



# new============================================================================================================
# 문제
# 다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다. 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다. c는 1로, d는 2로, ..., C를 8로 바꾼다.
#
# 1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.
#
# 연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 8개 숫자가 주어진다. 이 숫자는 문제 설명에서 설명한 음이며, 1부터 8까지 숫자가 한 번씩 등장한다.
#
# 출력
# 첫째 줄에 ascending, descending, mixed 중 하나를 출력한다.
#
# 예제 입력 1
# 1 2 3 4 5 6 7 8
# 예제 출력 1
# ascending

# <code>---------------------------------------------------------------------
#첫번째 숫자를 변수에 넣어서 for문을 돌려 다음 값들과 비교하여 클 때마다 result 를 증가시켜 ascending, descending, mixed인지 판단
# n = list(map(int, stdin.readline().split()))
# n_one = n[0]#초기값 넣기
# result = 0
# result1 = 0
# for i in n[1:]:
#     # print('i',i)
#     #ascending이면 result +=1
#     if n_one+1 == i:
#         n_one = i
#         result += 1
#         continue
#     if n_one-1 == i:
#         n_one -= 1
#         result1 +=1
# if result == 7:
#     print('ascending')
# elif result1 == 7:
#     print('descending')
# else:
#     print('mixed')

#다른풀이
# def scale(n):
#     answer = 'mixed'
#     max_num, min_num = max(n), min(n)
#     if list(range(1,max_num+1)) == n:
#         answer = 'ascending'
#     elif list(range(max_num,0,-1)) == n:
#         answer = 'descending'
#     return answer
# print(scale(n))

# numbers = list(map(int, stdin.readline().split()))
# def scale(numbers):
#     answer = "mixed"
#     start_num, end_num = min(numbers), max(numbers)
#
#     if list(range(start_num, end_num + 1)) == numbers:
#         answer = "ascending"
#     elif list(range(end_num, start_num - 1, -1)) == numbers:
#         answer = "descending"
#
#     return answer
#
# if __name__ == "__main__":
#     numbers = list(map(int, input().split()))
#     print(scale(numbers))



# new============================================================================================================
# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
#
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
#
# 입력의 마지막에는 0 두 개가 들어온다.
#
# 출력
# 각 테스트 케이스마다 A+B를 출력한다.

# <code>---------------------------------------------------------------------
# while True:
#     a,b = map(int, stdin.readline().split())
#     if a == 0 and b == 0:
#         break
#     print(a+b)


# new============================================================================================================
# 문제
# 알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.
#
# 입력
# 알파벳 소문자, 대문자, 숫자 0-9 중 하나가 첫째 줄에 주어진다.
# <code>---------------------------------------------------------------------
# ord함수를 사용하면 아스키코드로 변환 할 수 있다.
# n = input()
# print(ord(n))



# new============================================================================================================
# 문제
# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.
#
# 출력
# 입력으로 주어진 숫자 N개의 합을 출력한다.
#
# 예제 입력 1
# 1
# 1
# 예제 출력 1
# 1
# 예제 입력 2
# 5
# 54321
# 예제 출력 2
# 15
# # <code>---------------------------------------------------------------------
# n = int(stdin.readline())
# num = list(map(int, input()))
# result = 0
# for i in num:
#     result += i
# print(result)

# n = list((stdin.readline()))
# n1 = list((input()))
# print(n)
# print(n1)


# # new============================================================================================================
# 문제
# 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오. 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.
#
# 입력
# 첫 줄에 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열의 길이는 1,000,000을 넘지 않는다. 단어는 공백 한 개로 구분되며, 공백이 연속해서 나오는 경우는 없다. 또한 문자열은 공백으로 시작하거나 끝날 수 있다.
#
# 출력
# 첫째 줄에 단어의 개수를 출력한다.
#
# 예제 입력 1
# The Curious Case of Benjamin Button
# 예제 출력 1
# 6
# # # <code>---------------------------------------------------------------------
# word = list(map(str, stdin.readline().split()))
# print(len(word))


# # new============================================================================================================
# 별찍기문제
# # # <code>---------------------------------------------------------------------
# n = int(input())
# for i in range(n):
#     air = ' '
#     star = '*'
#     print(air*(n-(i+1))+star*(1+i))




# # new============================================================================================================
# 직사각형에서 탈출
# <code>---------------------------------------------------------------------
# x, y, w, h = map(int, input().split())
# minList = [x,y,abs(x-w),abs(y-h)]
# print(min(minList))



# # new============================================================================================================
#펠린드롬수
# 문제
# 어떤 단어를 뒤에서부터 읽어도 똑같다면 그 단어를 팰린드롬이라고 한다. 'radar', 'sees'는 팰린드롬이다.
#
# 수도 팰린드롬으로 취급할 수 있다. 수의 숫자들을 뒤에서부터 읽어도 같다면 그 수는 팰린드롬수다. 121, 12421 등은 팰린드롬수다. 123, 1231은 뒤에서부터 읽으면 다르므로 팰린드롬수가 아니다. 또한 10도 팰린드롬수가 아닌데, 앞에 무의미한 0이 올 수 있다면 010이 되어 팰린드롬수로 취급할 수도 있지만, 특별히 이번 문제에서는 무의미한 0이 앞에 올 수 없다고 하자.
#
# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있으며, 각 줄마다 1 이상 99999 이하의 정수가 주어진다. 입력의 마지막 줄에는 0이 주어지며, 이 줄은 문제에 포함되지 않는다.
#
# 출력
# 각 줄마다 주어진 수가 팰린드롬수면 'yes', 아니면 'no'를 출력한다.

# 예제 입력 1
# 121
# 1231
# 12421
# 0
# 예제 출력 1
# yes
# no
# yes
# <code>---------------------------------------------------------------------
#홀짝 나누어서 계산
#마지막에는 0을 넣어줘서 끝낸다.
# while True:
#     result = 0
#     word = list(input())
#     n = len(word)
#     if word == ['0']:
#         break
#     # n이 짝수라면
#     # if int(n) % 2 == 0:
#     for i in range(n//2+1):
#         if word[i] == word[-i-1]:
#             pass
#         else:
#             result = 1
#     if result != 1:
#         print('yes')
#     else:
#         print('no')



# # new============================================================================================================
# 위의 그림과 같이 육각형으로 이루어진 벌집이 있다.
# 그림에서 보는 바와 같이 중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서 1씩 증가하는 번호를 주소로 매길 수 있다.
# 숫자 N이 주어졌을 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때
# 몇 개의 방을 지나가는지(시작과 끝을 포함하여)를 계산하는 프로그램을 작성하시오.
# 예를 들면, 13까지는 3개, 58까지는 5개를 지난다.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 1,000,000,000)이 주어진다.
#
# 출력
# 입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력한다

# <code>---------------------------------------------------------------------
# n = int(input())
# result = 1
# if n == 1:
#     print(n)
# else:
#     n = n - 1
#     for i in range(1,n+1):
#         n = n - (6*i)
#         result +=1
#         if n <= 0:
#             print(result)
#             break

# n = int(input())
#
# nums_pileup = 1  # 벌집의 개수, 1개부터 시작
# cnt = 1
# while n > nums_pileup :
#     nums_pileup += 6 * cnt  # 벌집이 6의 배수로 증가
#     cnt += 1  # 반복문을 반복하는 횟수
# print(cnt)



# # new============================================================================================================
# 수 중복
# <code>---------------------------------------------------------------------
# n = int(stdin.readline())
# num = []
# for i in range(n):
#     num.append(int(stdin.readline()))
# num.sort()
# for i in num:
#     print(i)

# # new============================================================================================================
# 이항계수
# <code>---------------------------------------------------------------------
# nCk에 대해 연산하면 됨..
# n,k = map(int, input().split())

# if n==k or k==0:
#     print(int(1))
# else:
#     n_pak = 1
#     n_k_pak = 1
#     k_pak = 1
#     for i in range(1,n+1):
#         n_pak = n_pak*i
#
#     for i in range(1,n-k+1):
#         n_k_pak = n_k_pak*i
#
#     for i in range(1,k+1):
#         k_pak = k_pak*i
#     print(int(n_pak/(k_pak*n_k_pak)))




# # new============================================================================================================
# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
#
# 출력
# 주어진 수들 중 소수의 개수를 출력한다.
# <code>---------------------------------------------------------------------
# n = int(stdin.readline())
# num = list(map(int, stdin.readline().split()))
# result = 0
# result_list = []
# for i in num:
#     #1인경우 소수가 아님
#     if i == 1:
#         result = 1#소수가 아닌경우 result 에 1 부여
#     #2인경우 소수
#     elif i == 2:
#         result = 0
#     #2보다 큰 경우 i를 i보다 작은 수들로 나눠서 나머지가 0인 경우가 있으면 result를 1로 부여하고 break
#     #result를 append한 후 전체 숫자 n에서 소수가 아닌 경우를 빼면(sum(result_list)) 소수인 경우만 남는다.
#     else:
#         for k in range(2,i):
#             # print('k,i',k,i,'i % k>',i % k)
#             if i % k == 0:
#                 result = 1
#                 break
#             else:
#                 result = 0
#     result_list.append(result)
#     # print(result_list)
# print(n-sum(result_list))



# # # new============================================================================================================
# 문제
# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
#
# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 입력
# 첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.
#
# 출력
# 조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.
#
# 예제 입력 1
# 13
# but
# i
# wont
# hesitate
# no
# more
# no
# more
# it
# cannot
# wait
# im
# yours
# 예제 출력 1
# i
# im
# it
# no
# but
# more
# wait
# wont
# yours
# cannot
# hesitate
# # <code>---------------------------------------------------------------------
#

# set로 중복없애기 set
#길이가 짧은 순서대로 출력 sorted
#길이가 같다면 알파벳 순서대로 정렬

n = int(stdin.readline())
word = []
word_len_list = []
for i in range(n):
    word.append(input())
word_list = list(set(word))
# print(word_list)
for i in (word_list):
    word_len_list.append((len(i),i))
    # print(word_len_list)
result = sorted(word_len_list)

for num, wordone in result:
    print(wordone)