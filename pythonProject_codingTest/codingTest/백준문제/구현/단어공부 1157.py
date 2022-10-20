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

word = stdin.readline()
word = word.upper()
word_set = set(word)
word_set = deque(word_set)
# print('wordset>',word_set)
word_set.remove('\n')
# print('wordset',word_set)
# print('word',word)
# word_set = ''.join(set(word))
# print('wordset>',word_set)
word_count = word.count(word_set[0])
one = word[0]
count_word = []
count_i_word = []
result = 0#단어가 중복으로 많으면 result를 증가시킴
for i in word_set:

    word_count_i = word.count(i)#문자 카운트
    count_word.append(word_count_i)
    count_i_word.append([i,word_count_i])
    # print('카운트월드',count_word)
    # print('카운트i월드',count_i_word)
for one in count_i_word:
    st, coun = one[0], one[1]
    if max(count_word) == coun:
        max_st = st
        result += 1
        # print('result>',result)
        # print('>>',st,coun)
if result > 1:
    print('?')
else:
    print(max_st)
