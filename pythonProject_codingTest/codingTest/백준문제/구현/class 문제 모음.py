# 별그리기 문제
# import math
# from sys import stdin
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

# n = int(stdin.readline())
# word = []
# word_len_list = []
# for i in range(n):
#     word.append(input())
# word_list = list(set(word))
# # print(word_list)
# for i in (word_list):
#     word_len_list.append((len(i),i))
#     # print(word_len_list)
# result = sorted(word_len_list)
#
# for num, wordone in result:
#     print(wordone)
#




# # # new============================================================================================================
# 영화감독 숌
# 문제
# 666은 종말을 나타내는 숫자라고 한다. 따라서, 많은 블록버스터 영화에서는 666이 들어간 제목을 많이 사용한다.
# 영화감독 숌은 세상의 종말 이라는 시리즈 영화의 감독이다.
# 조지 루카스는 스타워즈를 만들 때, 스타워즈 1, 스타워즈 2, 스타워즈 3, 스타워즈 4, 스타워즈 5, 스타워즈 6과 같이 이름을 지었고,
# 피터 잭슨은 반지의 제왕을 만들 때, 반지의 제왕 1, 반지의 제왕 2, 반지의 제왕 3과 같이 영화 제목을 지었다.
#
# 하지만 숌은 자신이 조지 루카스와 피터 잭슨을 뛰어넘는다는 것을 보여주기 위해서 영화 제목을 좀 다르게 만들기로 했다.
#
# 종말의 숫자란 어떤 수에 6이 적어도 3개이상 연속으로 들어가는 수를 말한다.
# 제일 작은 종말의 숫자는 666이고, 그 다음으로 큰 수는 1666, 2666, 3666, .... 과 같다.
#
# 따라서, 숌은 첫 번째 영화의 제목은 세상의 종말 666, 두 번째 영화의 제목은 세상의 종말 1666 이렇게 이름을 지을 것이다.
# 일반화해서 생각하면, N번째 영화의 제목은 세상의 종말 (N번째로 작은 종말의 숫자) 와 같다.
#
# 숌이 만든 N번째 영화의 제목에 들어간 숫자를 출력하는 프로그램을 작성하시오. 숌은 이 시리즈를 항상 차례대로 만들고, 다른 영화는 만들지 않는다.
#
# 입력
# 첫째 줄에 숫자 N이 주어진다. N은 10,000보다 작거나 같은 자연수이다.
#
# 출력
# 첫째 줄에 N번째 영화의 제목에 들어간 수를 출력한다.
#
# 예제 입력 1
# 2
# 예제 출력 1
# 1666

# # <code>---------------------------------------------------------------------
# n = int(input())
# a = 666
# cnt = 0
#
# while n:
#     if "666" in str(a):
#         n -= 1
#         print(n)
#     a += 1
#     print('a',a)
#
# print(a-1)




# # # new============================================================================================================
# 문제
# 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다.
# 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)
#
# 둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다. 나이는 1보다 크거나 같으며,
# 200보다 작거나 같은 정수이고, 이름은 알파벳 대소문자로 이루어져 있고, 길이가 100보다 작거나 같은 문자열이다.
# 입력은 가입한 순서로 주어진다.
#
# 출력
# 첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순,
# 나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.
#
# 예제 입력 1
# 3
# 21 Junkyu
# 21 Dohyun
# 20 Sunyoung
# 예제 출력 1
# 20 Sunyoung
# 21 Junkyu
# 21 Dohyun
# # # <code>---------------------------------------------------------------------

#튜플로 저장해서 정렬하자
# n = int(stdin.readline())
# word = []
# for i in range(n):
#     age, name = map(str, input().split())
#     word.append((int(age),name))
# # print(word)
# #알파벳 순서로 정렬=sort()사용
# # word.sort(key= lambda x:x[1])
# # print('단어로 정렬',word)
# # sorted_word = sorted(word)
# word.sort(key= lambda x:x[0])
# # print(word)
# for age, name in word:
#     print(age,name)




# # # new============================================================================================================
#좌표 정렬하기
# 문제
# 2차원 평면 위의 점 N개가 주어진다.
# 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다.
# 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000)
# 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.
#
# 출력
# 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
#
# 예제 입력 1
# 5
# 3 4
# 1 1
# 1 -1
# 2 2
# 3 3

# 예제 출력 1
# 1 -1
# 1 1
# 2 2
# 3 3
# 3 4
# # # <code>---------------------------------------------------------------------
#3시 45분
#튜플로 받아서 sort하자!
#
# n = int(stdin.readline())
# graph = []
# for i in range(n):
#     x,y = map(int, stdin.readline().split())
#     graph.append((x,y))
# graph.sort()
#
# for x,y in graph:
#     print(x,y)



# # # new============================================================================================================
# 문제
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.
#
# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
#
# 예제 입력 1
# 24 18
# 예제 출력 1
# 6
# 72
# # # <code>---------------------------------------------------------------------
# mi, ma = map(int, stdin.readline().split())
# gcd_num = math.gcd(mi,ma)
# print(gcd_num)
# def lcm(a,b,gcd_num):
#     lc = (a*b)/gcd_num
#     return lc
# print(int(lcm(mi,ma,gcd_num)))


# # # new============================================================================================================
# 문제
# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)
#
# 출력
# 첫째 줄에 구한 0의 개수를 출력한다.
# # # <code>---------------------------------------------------------------------

#1.N!를 구한다.
#2.뒤에서부터 0이면 answer+=1을 해서 연산

# n = int(input())
# n_pak = 1
# for i in range(1,n+1):
#     n_pak *= i
# str_n_pak = str(n_pak)
#
# answer = 0
# i = -1
# while True:
#     if str_n_pak[i] == '0':
#         answer +=1
#     else:
#         break
#     i -= 1
# print(answer)


# new============================================================================================================
# 듣보잡
#
# 문제
# 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.
#
# 듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.
#
# 출력
# 듣보잡의 수와 그 명단을 사전순으로 출력한다.
# <code>---------------------------------------------------------------------
# n,m = map(int, stdin.readline().split())
# #명단의 중복을 없애고 교집합으로 중복된 사람이름을 찾기 위해 set()자료형을 이용
# #append대신 add를 사용하면 된다.
# name1 = set()
# name2 = set()
# for i in range(n):
#     name1.add(stdin.readline().rstrip())
# for i in range(m):
#     name2.add(stdin.readline().rstrip())
# result = sorted(list(name1&name2))
# print(len(result))
# for i in result:
#     print(i)
#



# new============================================================================================================
# 문제
# 2019 HEPC - MAVEN League의 "비밀번호 만들기"와 같은 방식으로 비밀번호를 만든 경민이는 한 가지 문제점을 발견하였다.
# 비밀번호가 랜덤으로 만들어져서 기억을 못 한다는 것이었다! 그래서 경민이는 메모장에 사이트의 주소와 비밀번호를 저장해두기로 했다.
# 하지만 컴맹인 경민이는 메모장에서 찾기 기능을 활용하지 못하고 직접 눈으로 사이트의 주소와 비밀번호를 찾았다.
# 메모장에 저장된 사이트의 수가 늘어나면서 경민이는 비밀번호를 찾는 일에 시간을 너무 많이 쓰게 되었다.
# 이를 딱하게 여긴 문석이는 경민이를 위해 메모장에서 비밀번호를 찾는 프로그램을 만들기로 결심하였다!
# 문석이를 도와 경민이의 메모장에서 비밀번호를 찾아주는 프로그램을 만들어보자.
#
# 입력
# 첫째 줄에 저장된 사이트 주소의 수 N(1 ≤ N ≤ 100,000)과 비밀번호를 찾으려는 사이트 주소의 수 M(1 ≤ M ≤ 100,000)이 주어진다.
#
# 두번째 줄부터 N개의 줄에 걸쳐 각 줄에 사이트 주소와 비밀번호가 공백으로 구분되어 주어진다. 사이트 주소는 알파벳 소문자, 알파벳 대문자, 대시('-'), 마침표('.')로 이루어져 있고, 중복되지 않는다. 비밀번호는 알파벳 대문자로만 이루어져 있다. 모두 길이는 최대 20자이다.
#
# N+2번째 줄부터 M개의 줄에 걸쳐 비밀번호를 찾으려는 사이트 주소가 한줄에 하나씩 입력된다. 이때, 반드시 이미 저장된 사이트 주소가 입력된다.
# <code>---------------------------------------------------------------------
# from sys import stdin
# n,m = map(int, stdin.readline().split())
# # 딕셔너리 자료형 이용
# N = {}
# for i in range(n):
#     a,b = map(str, stdin.readline().split())
#     #a를 key로 value를 b로 넣어준다.
#     N[a] = b
# # print(N)
# #
# for i in range(m):
#     #a에 해당하는 b값을 출력
#     print(N[stdin.readline().rstrip()])
#



# new============================================================================================================
# 입력
# 첫째 줄에는 도감에 수록되어 있는 포켓몬의 개수 N이랑 내가 맞춰야 하는 문제의 개수 M이 주어져.
# N과 M은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수인데, 자연수가 뭔지는 알지?
# 모르면 물어봐도 괜찮아. 나는 언제든지 질문에 답해줄 준비가 되어있어.
#
# 둘째 줄부터 N개의 줄에 포켓몬의 번호가 1번인 포켓몬부터 N번에 해당하는 포켓몬까지 한 줄에 하나씩 입력으로 들어와.
# 포켓몬의 이름은 모두 영어로만 이루어져있고, 또, 음... 첫 글자만 대문자이고, 나머지 문자는 소문자로만 이루어져 있어.
# 아참! 일부 포켓몬은 마지막 문자만 대문자일 수도 있어. 포켓몬 이름의 최대 길이는 20, 최소 길이는 2야.
# 그 다음 줄부터 총 M개의 줄에 내가 맞춰야하는 문제가 입력으로 들어와. 문제가 알파벳으로만 들어오면 포켓몬 번호를 말해야 하고,
# 숫자로만 들어오면, 포켓몬 번호에 해당하는 문자를 출력해야해. 입력으로 들어오는 숫자는 반드시 1보다 크거나 같고,
# N보다 작거나 같고, 입력으로 들어오는 문자는 반드시 도감에 있는 포켓몬의 이름만 주어져. 그럼 화이팅!!!
#
# 출력
# 첫째 줄부터 차례대로 M개의 줄에 각각의 문제에 대한 답을 말해줬으면 좋겠어!!!.
# 입력으로 숫자가 들어왔다면 그 숫자에 해당하는 포켓몬의 이름을, 문자가 들어왔으면 그 포켓몬의 이름에 해당하는 번호를 출력하면 돼.
# 그럼 땡큐~
# <code>---------------------------------------------------------------------
# from sys import stdin
# n,m = map(int, stdin.readline().split())
# N = {}
# N2 = {}
# for i in range(1,n+1):
#     name = stdin.readline().rstrip()
#     # 입력한 단어가 문자인 경우에 쓸 딕셔너리 key, value값
#     N[name] = i
#     # 입력한 단어가 숫자인 경우에 쓸 딕셔너리 key, value값
#     N2[i] = name
# # print(N)
#
# for i in range(m):
#     # 입력받기
#     one = stdin.readline().rstrip()
#     # 들어온값이 알파벳이라면
#     if one.isalpha() == True:
#         print(N[one])
#     else:
#         print(N2[int(one)])




# new============================================================================================================
# 파도반수열

# 문제
# 오른쪽 그림과 같이 삼각형이 나선 모양으로 놓여져 있다. 첫 삼각형은 정삼각형으로 변의 길이는 1이다.
# 그 다음에는 다음과 같은 과정으로 정삼각형을 계속 추가한다. 나선에서 가장 긴 변의 길이를 k라 했을 때,
# 그 변에 길이가 k인 정삼각형을 추가한다.
#
# 파도반 수열 P(N)은 나선에 있는 정삼각형의 변의 길이이다. P(1)부터 P(10)까지 첫 10개 숫자는 1, 1, 1, 2, 2, 3, 4, 5, 7, 9이다.
#
# N이 주어졌을 때, P(N)을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. (1 ≤ N ≤ 100)
#
# 출력
# 각 테스트 케이스마다 P(N)을 출력한다.
#
# 예제 입력 1
# 2
# 6
# 12
# 예제 출력 1
# 3
# 16
# <code>---------------------------------------------------------------------
# from sys import stdin
# n = int(input())
#
# for i in range(n):
#     m = int(stdin.readline())
#     answer = 0
#     p_list2 = [1,1,1,2] # 초기 값
#     pn1 = 2
#
#     if m == 1 or m == 2 or m == 3:
#         print(1)
#     elif m == 4 or m == 5:
#         print(2)
#     else:
#         for i in range(m-5):
#             pn = pn1 + p_list2[0+i]
#             # print('i>>',i,'pn',pn)
#             p_list2.append(pn1)
#             pn1 = pn
#         print(pn)


# new============================================================================================================
# 문제
# 라그랑주는 1770년에 모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현할 수 있다고 증명하였다.
# 어떤 자연수는 복수의 방법으로 표현된다. 예를 들면, 26은 52과 12의 합이다; 또한 42 + 32 + 12으로 표현할 수도 있다.
# 역사적으로 암산의 명수들에게 공통적으로 주어지는 문제가 바로 자연수를 넷 혹은 그 이하의 제곱수 합으로 나타내라는 것이었다.
# 1900년대 초반에 한 암산가가 15663 = 1252 + 62 + 12 + 12라는 해를 구하는데 8초가 걸렸다는 보고가 있다.
# 좀 더 어려운 문제에 대해서는 56초가 걸렸다: 11339 = 1052 + 152 + 82 + 52.
#
# 자연수 n이 주어질 때, n을 최소 개수의 제곱수 합으로 표현하는 컴퓨터 프로그램을 작성하시오.
#
# 입력
# 입력은 표준입력을 사용한다. 입력은 자연수 n을 포함하는 한 줄로 구성된다. 여기서, 1 ≤ n ≤ 50,000이다.
#
# 출력
# 출력은 표준출력을 사용한다. 합이 n과 같게 되는 제곱수들의 최소 개수를 한 줄에 출력한다.
#
# 예제 입력 1
# 25
# 예제 출력 1
# 1
# <code>---------------------------------------------------------------------
# import math
# def fourSquares(n):
#     # √n이 정수일 때
#     if int(math.sqrt(n)) == math.sqrt(n):
#         return 1
#     # √(n - i^2)이 정수일 때
#     for i in range(1, int(math.sqrt(n)) + 1):
#         if int(math.sqrt(n - i ** 2)) == math.sqrt(n - i ** 2):#n이 두 수의 제곱으로 표현되면 (int값으로 표현되면) return 2
#             return 2
#     # √(n - i^2 - j^2)이 정수일 때
#     for i in range(1, int(math.sqrt(n)) + 1):
#         for j in range(1, int(math.sqrt(n - i ** 2)) + 1):
#             if int(math.sqrt(n - i ** 2 - j ** 2)) == math.sqrt(n - i ** 2 - j ** 2):#n이 세 수의 제곱으로 표현되면 (int값으로 표현되면) return 3
#                 return 3
#     # 남은 경우는 4
#     return 4
#
#
# n = int(input())
# print(fourSquares(n))



# new============================================================================================================
# 문제
# 땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.
#
# 달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.
#
# 달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)
#
# 출력
# 첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.
#
# 예제 입력 1
# 2 1 5
# 예제 출력 1
# 4
# <code>---------------------------------------------------------------------
# from sys import stdin
# import math
# n,m,v = map(int, stdin.readline().split())
# answer=math.ceil((v-n)/(n-m))
# print(answer+1)


# new============================================================================================================
# 문제
# 세계는 균형이 잘 잡혀있어야 한다. 양과 음, 빛과 어둠 그리고 왼쪽 괄호와 오른쪽 괄호처럼 말이다.
#
# 정민이의 임무는 어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램을 짜는 것이다.
#
# 문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.
#
# 모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
# 모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
# 모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
# 모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
# 짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
# 정민이를 도와 문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단해보자.
#
# 입력
# 하나 또는 여러줄에 걸쳐서 문자열이 주어진다. 각 문자열은 영문 알파벳, 공백, 소괄호("( )") 대괄호("[ ]")등으로 이루어져 있으며, 길이는 100글자보다 작거나 같다. 각 줄은 마침표(".")로 끝난다.
#
# 입력의 종료조건으로 맨 마지막에 점 하나(".")가 들어온다.
# 출력
# 각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.
#
# 예제 입력 1
# So when I die (the [first] I will see in (heaven) is a score list).
# [ first in ] ( first out ).
# Half Moon tonight (At least it is better than no Moon at all].
# A rope may form )( a trail in a maze.
# Help( I[m being held prisoner in a fortune cookie factory)].
# ([ (([( [ ] ) ( ) (( ))] )) ]).
#  .
# .
#
# 예제 출력 1
# yes
# yes
# no
# no
# no
# yes
# yes
# <code>---------------------------------------------------------------------
# from sys import stdin
# from collections import deque
# while True:
#     queue = deque()
#     st = (stdin.readline().rstrip())
#     answer = True
#     if st =='.':
#         break
#
#     for s in st:
#
#         if s == '(' or s =='[':
#             queue.append(s)
#
#         elif s ==')':
#             if not queue or queue[-1] == '[':
#                 answer = False
#                 break
#             elif queue[-1] == '(':
#                 queue.pop()
#
#         elif s == ']':
#             if not queue or queue[-1] == '(':
#                 answer = False
#                 break
#
#             elif queue[-1] == '[':
#                 queue.pop()
#
#     if answer == True and not queue:#answer가 true고 queue가 비어있으면 yes프린트
#         print('yes')
#     else:
#         print('no')



# new============================================================================================================
# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
#
# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
#
# 예제 입력 1
# 3 16
# 예제 출력 1
# 3
# 5
# 7
# 11
# 13
# <code>---------------------------------------------------------------------
# from sys import stdin
# import math
# n,m = map(int, stdin.readline().split())
# for i in range(m-n+1):
#     k=n+i
#     answer = 1
#     if k==1 or k==4 or k==6 or k==8:
#         answer =0
#     if k>=9:
#         for l in range(2,math.trunc(math.sqrt(k))+1):
#             # print('int(math.sqrt(k))',int(math.sqrt(k)))
#             # print('l',l)
#             if k%l==0:
#                 answer = 0
#                 break
#     if answer == 1:
#         print(k)

#아래방법은 에라토스테네스의 체 방법인데 .. 메모리가 너무 커서 m=1000000인 경우 실행이 안된다.
# graph = []
# for i in range(2,m+1):
#     graph.append(i)
# i=0
# for i in range(len(graph)-1):
#     k = graph[i]
#     for n1 in range(i + 1, len(graph)):
#         if k != 1:
#             if graph[n1] % k == 0:
#                 graph[n1] = 1
#
# for i in range(len(graph)):
#     if graph[i] < n:
#         graph[i] = 1
#
# for i in graph:
#     if i != 1:
#         print(i)



# new============================================================================================================
# 2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.
#
# 출력
# 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
# <code>---------------------------------------------------------------------
# from sys import stdin
#
# n = int(input())
# ablist = []
# for i in range(n):
#     a,b = map(int,stdin.readline().split())
#     ablist.append((a,b))
# ablist.sort(key=lambda x: (x[1], x[0]))#2번째 원소로 정렬 후 , 두번째 원소의 값이 같으면 첫번째 원소로 정렬
# for one in ablist:
#     a,b = one
#     print(a,b)

# new============================================================================================================
# 문제
# 재원이는 한 도시의 시장이 되었다. 이 도시에는 도시를 동쪽과 서쪽으로 나누는 큰 일직선 모양의 강이 흐르고 있다.
# 하지만 재원이는 다리가 없어서 시민들이 강을 건너는데 큰 불편을 겪고 있음을 알고 다리를 짓기로 결심하였다.
# 강 주변에서 다리를 짓기에 적합한 곳을 사이트라고 한다. 재원이는 강 주변을 면밀히 조사해 본 결과 강의 서쪽에는 N개의 사이트가 있고
# 동쪽에는 M개의 사이트가 있다는 것을 알았다. (N ≤ M)
#
# 재원이는 서쪽의 사이트와 동쪽의 사이트를 다리로 연결하려고 한다. (이때 한 사이트에는 최대 한 개의 다리만 연결될 수 있다.)
# 재원이는 다리를 최대한 많이 지으려고 하기 때문에 서쪽의 사이트 개수만큼 (N개) 다리를 지으려고 한다. 다리끼리는 서로 겹쳐질 수 없다고 할 때
# 다리를 지을 수 있는 경우의 수를 구하는 프로그램을 작성하라.
# 예제 입력 1
# 3
# 2 2
# 1 5
# 13 29
# 예제 출력 1
# 1
# 5
# 67863915
# <code>---------------------------------------------------------------------
from sys import stdin

n = int(input())
num = 0
for i in range(n):
    a,b = map(int, stdin.readline().split())
    if a==b:
        num = 1
        print(num)
        continue
    k = b-(a-1)
    print('k',k)
    while True:
        print('k', k)
        if k ==1:
            num +=1
            print('num',num)
            break
        for i in range(1,k+1):
            num += i
            print('num',num)
        k -=1
    print(num)

