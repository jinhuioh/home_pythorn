# 각 자리가 0~9로만 이루어진 문자열 s가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며
# 숫자 사이에 x또는 +연산자를 넣어 결과적으로 가장 큰 수를 구하는 프로그램을 작성하시오
# 단 연산은 왼쪽부터 순서대로 실행됨
# 또한 만들어진 가장 큰 수는 항상 20억 이하의 정수가 되도록 입력이 주어집니다.

# 내풀이
# s = list(input())
# print(s)
# # 019012
# # 0인 원소를 모두 제거
# ss = []
# for s_one in s:
#     if int(s_one) != 0:
#         ss.append(s_one)
# # 첫번째 원소부터 마지막 원소까지 곱하기
# print(ss)
# sss = int(ss[0])
# if sss == 1:
#     sss = int(ss[0]) + int(ss[1])
#     for i in range(2,len(ss)):
#         if int(ss[i]) == 1:
#             sss = sss + int(s[i])
#             print('+',sss)
#         else:
#             sss = sss * int(ss[i])
#             print('x',sss)
#
# else:
#     for i in range(1, len(ss)):
#         if (ss[i]) == 1:
#             sss = sss + int(ss[i])
#             print('+',sss)
#         else:
#             sss = sss * int(ss[i])
#             print('x',sss)
#
# print(sss)


# 해설풀이-------------------------------------------------
# 공통되는 부분은 최대한 한 조건으로 묶어서 소요시간을 최소화 하자.
s = list(input())
print(s)
# ss[0]가 1보다 작거나 같으면을 조건으로 해서 풀기
s0 = int(s[0])
for i in range(1,len(s)):
    if int(s[i]) <= 1 or int(s0) <= 1:#첫번째 값 또는 i번째 원소값이 1 또는 0 인경우 덧셈
        s0 = int(s0)+int(s[i])
    else:
        s0 = int(s0)*int(s[i])
print(s0)