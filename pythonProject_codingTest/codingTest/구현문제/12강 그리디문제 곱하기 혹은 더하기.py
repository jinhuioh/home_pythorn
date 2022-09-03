# 각 자리가 0~9로만 이루어진 문자열 s가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며
# 숫자 사이에 x또는 +연산자를 넣어 결과적으로 가장 큰 수를 구하는 프로그램을 작성하시오
# 단 연산은 왼쪽부터 순서대로 실행됨
# 또한 만들어진 가장 큰 수는 항상 20억 이하의 정수가 되도록 입력이 주어집니다.

# 내 풀이1
# 1. 리스트로 입력받아서 한개씩꺼내서 연산하기
# 2. 기존 입력값에서 0을 제외한 리스트를 만들음
# 3. 각 원소 전부 곱하기
# def cul():
#     s = list(input())
#     # 019012
#     # 0인 원소를 모두 제거
#     ss = []
#     for s_one in s:
#         if int(s_one) != 0:
#             ss.append(s_one)
#     # 첫번째 원소부터 마지막 원소까지 곱하기
#     sss = 1
#     # 12121123
#     for i in range(len(ss)):
#         sss0 = ss[0]
#         if ss[0] == 1:
#             sss = s[0]
#         elif ss[i] == 1:
#             sss = ss[i] + sss
#         else:
#             sss = int(ss[i])*sss
# cul()

# 내 풀이2(이게 더 나은듯 실행시간 줄일 수 있을 것 같다)
# 1. 리스트로 입력받아서 한개씩꺼내서 연산하기
# 2. 만약 0이 있으면 for문 continue로 패스하기.
# 3. 원소 하나씩 꺼내서 곱셈처리
# 4. try except문으로 감싸기. 기본 int형은 21억자리까지 출력 가능하기 때문.
# try:
#     s = list(input())
#     ss = 1
#     for s_one in s:
#         if int(s_one) == 0:
#             continue
#         if int(s_one) == 1:
#             # 0123
#             ss = ss + 1
#         ss = ss * int(s_one)
#     print(ss)
# except:
#     print('이상한 값이 들어가거나, 20억 이상의 정수가 출력되었습니다.')


s = list(input())
print(s)
# 019012
# 0인 원소를 모두 제거
ss = []
for s_one in s:
    if int(s_one) != 0:
        ss.append(s_one)
# 첫번째 원소부터 마지막 원소까지 곱하기
print(ss)
sss = int(ss[0])
if sss == 1:
    sss = int(ss[0]) + int(ss[1])
    for i in range(2,len(ss)):
        if int(ss[i]) == 1:
            sss = sss + int(s[i])
            print('+',sss)
        else:
            sss = sss * int(ss[i])
            print('x',sss)

else:
    for i in range(1, len(ss)):
        if (ss[i]) == 1:
            sss = sss + int(ss[i])
            print('+',sss)
        else:
            sss = sss * int(ss[i])
            print('x',sss)

print(sss)