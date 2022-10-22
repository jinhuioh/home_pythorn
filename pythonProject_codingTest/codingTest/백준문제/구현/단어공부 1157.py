# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.
#
# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
#
# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
#
# 예제 입력 1
# Mississipi
# 예제 출력 1
# ?

#문자열.upper()을 하면 대문자로 변경가능
#문자열.lower()을 하면 소문자로 변경가능
from collections import deque
from sys import stdin
#
# word = stdin.readline()#input보다 빠른 입력을 받기위해 사용
# word = word.upper()#입력받은 word를 전부 대문자로 바꿈
# word_set = set(word)#word_set변수에 순서는 없지만 중복을 제거한 word를 담음
# word_set = deque(word_set)#큐에 넣어 하나씩 꺼내서 for문 돌려 count할 예정
# word_set.remove('\n')#필요없는 단어 제거
# count_word = []#문자를 카운트 한 숫자들이 들어가는 리스트
# count_i_word = []#[단어,카운트 숫자]가 들어가는 리스트
# result = 0#단어가 중복으로 많으면 result를 증가시켜 result가 1보다 크면 print('?')를 출력
# for i in word_set:
#     word_count_i = word.count(i)#문자 카운트
#     count_word.append(word_count_i)#문자를 카운트 한 숫자들 append
#     count_i_word.append([i,word_count_i])#[단어,카운트 숫자]를 append
# for one in count_i_word:
#     st, coun = one[0], one[1]#단어를 st변수에 카운트한 숫자를 coun변수에 저장
#     if max(count_word) == coun:#coun에 들어간 카운트한 숫자가 가장 큰 수랑 같으면 result증가
#         #가장 개수가 많은 단어를 max_st변수에 저장
#         max_st = st
#         result += 1
# #카운트한 숫자가 최대인 단어가 1개 이상이면  print('?') 출력
# if result > 1:
#     print('?')
# #그렇지 않으면 최대빈도수 단어 출력
# else:
#     print(max_st)
#
#
#
# #비슷한 다른 풀이
# word = stdin.readline().upper()
# word_list = list(set(word))
# word_list.remove('\n')
# print('word',word)
# print('wordlist',word_list)
#
# cnt = []
# for i in word_list:
#     count = word.count
#     cnt.append(count(i))
#     print('cnt',cnt)
# if cnt.count(max(cnt)) > 1:
#     print('?')
# else:
#     print('인덱스',cnt.index(max(cnt)))
#     print(word_list[(cnt.index(max(cnt)))])


# n1 = int(input())
# n2 = int(input())
#
# print(f'{n1}은 {n2}보다 큽니까? {n1> n2}')
# print(f'{n1}은 {n2}보다 크거나 같습니까? {n1 >= n2}')
# print(f'{n1}은 {n2}와 다릅니까? {n1 != n2}')
# print(f'{n1}은 {n2}와 같습니까? {n1 == n2}')
