# 문제
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
# 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.
# 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.
#
# 출력
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
#
# 예제 입력 1
# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5

# 예제 출력 1
# 1
# 1
# 0
# 0
# 1
from collections import deque
from sys import stdin

n = int(stdin.readline())
n_num = sorted(list(map(int,stdin.readline().split())))
m = int(stdin.readline())
m_num = list(map(int, stdin.readline().split()))
def num(start, end, n_num, m_one):
    if start > end:
        return 0
    mid = (start+end)//2
    if n_num[mid] == m_one:
        return 1
    elif n_num[mid] > m_one:
        return num(start,mid-1,n_num, m_one)
    else:
        return num(mid+1, end, n_num, m_one)


for m_one in m_num:
    start = 0
    end = len(n_num)-1
    print(num(start, end, n_num, m_one))




# def num(start, end, n_num, m_one):#시작 숫자,마지막 숫자, 숫자가 있는지 확인할 리스트, m_num안에 있는 확인할 숫자
#     if start > end:
#         return 0
#     mid_num = (start+end)//2
#     if n_num[mid_num] == m_one:
#         return 1
#     elif mid_num > m_one:
#         return num(start, mid_num-1, n_num, m_one)
#     else:
#         return num(mid_num+1, end, n_num, m_one)
#
# for m_one in m_num:
#     start = 0
#     end = len(n_num)-1 #start를 0부터 시작하므로 end도 -1을 해준다.
#     print(num(start, end, n_num, m_one))










# from sys import stdin, stdout
#
# n = int(stdin.readline())
# graph1 = sorted(stdin.readline().split())
#
# m = int(stdin.readline())
# graph2 = stdin.readline().split()
#
# for i in graph2:
#     stdout.write('1\n') if i in graph1 else stdout.write('0\n')





#
#
#
# from sys import stdin, stdout
#
# n = stdin.readline()
# N = sorted(map(int, stdin.readline().split()))
#
# m = stdin.readline()
# M = map(int, stdin.readline().split())
#
#
# def binary(l, N, start, end):#l은 M에 있는 숫자
#     if start > end:
#         return 0
#     m = (start + end) // 2
#     if l == N[m]:
#         return 1
#     elif l < N[m]:
#         return binary(l, N, start, m - 1)
#     else:
#         return binary(l, N, m + 1, end)
#
#
# for l in M:
#     start = 0
#     end = len(N) - 1
#     print(binary(l, N, start, end))