# 문제 설명
# xx 회사의 2xN명의 사원들은 N명씩 두 팀으로 나눠 숫자 게임을 하려고 합니다.
# 두 개의 팀을 각각 A팀과 B팀이라고 하겠습니다. 숫자 게임의 규칙은 다음과 같습니다.
#
# 먼저 모든 사원이 무작위로 자연수를 하나씩 부여받습니다.
# 각 사원은 딱 한 번씩 경기를 합니다.
# 각 경기당 A팀에서 한 사원이, B팀에서 한 사원이 나와 서로의 수를 공개합니다. 그때 숫자가 큰 쪽이 승리하게 되고,
# 승리한 사원이 속한 팀은 승점을 1점 얻게 됩니다.
# 만약 숫자가 같다면 누구도 승점을 얻지 않습니다.
# 전체 사원들은 우선 무작위로 자연수를 하나씩 부여받았습니다.
# 그다음 A팀은 빠르게 출전순서를 정했고 자신들의 출전 순서를 B팀에게 공개해버렸습니다.
# B팀은 그것을 보고 자신들의 최종 승점을 가장 높이는 방법으로 팀원들의 출전 순서를 정했습니다.
# 이때의 B팀이 얻는 승점을 구해주세요.
# A 팀원들이 부여받은 수가 출전 순서대로 나열되어있는 배열 A와 i번째 원소가 B팀의 i번 팀원이 부여받은 수를 의미하는 배열 B가 주어질 때,
# B 팀원들이 얻을 수 있는 최대 승점을 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# A와 B의 길이는 같습니다.
# A와 B의 길이는 1 이상 100,000 이하입니다.
# A와 B의 각 원소는 1 이상 1,000,000,000 이하의 자연수입니다.

# A	B	result
# [5,1,3,7]	[2,2,6,8]	3
# [2,2,2,2]	[1,1,1,1]	0
from collections import deque

# a= [5,1,3,7]
# b= [2,2,6,8]
# a= [2,2,2,2]
# b= [1,1,1,1]
a= [1,3,3,5,6,7,8,9]
b= [2,2,5,5,7,7,7,8]

#
# def solution(a, b):
#     a.sort()
#     b.sort()
#     answer = 0
#     queueA = deque(a)
#     queueB = deque(b)
#
#     #한개씩 꺼내서 비교
#     while queueA:
#         que_a_pop= queueA.popleft()
#         que_b_pop= queueB.popleft()
#         if len(queueA) > 0 and que_b_pop <= que_a_pop and queueB[0] <= queueA[0] and queueB[0]> que_a_pop:
#             answer += 1
#         elif que_b_pop > que_a_pop:
#             answer += 1
#
#     return answer
#
# print(solution(a,b))

# a= [5,1,3,7]
# b= [2,2,6,8]
# a= [2,2,2,2]
# b= [1,1,1,1]
a= [1,3,3,5,6,7,8,9]
b= [2,2,5,5,7,7,7,8]

def solution(a, b):
    a.sort()
    b.sort()
    answer = 0
    for A in a:
        if len(b) <= 0:
            break
        if A >= b[0]:
            for i in range(len(b)):
                # print('b[0]',b[0])
                if len(b) <0:
                    break
                if b[0] > A:
                    answer +=1
                    break
                else:
                    b.remove(b[0])

        else:
            answer+=1
            # print('else',A,b[0])
            # print('answer',answer)
            b.remove(b[0])
    return answer
#
# def solution(a, b):
#     a.sort(reverse=True)
#     b.sort(reverse=True)
#     answer = 0
#     for A in a:
#         if A >= b[0]:
#             continue
#         else:
#             answer+=1
#             b.remove(b[0])
#     return answer

print(solution(a,b))