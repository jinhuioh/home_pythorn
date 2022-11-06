# 문제 설명
# N개의 아파트가 일렬로 쭉 늘어서 있습니다. 이 중에서 일부 아파트 옥상에는 4g 기지국이 설치되어 있습니다.
# 기술이 발전해 5g 수요가 높아져 4g 기지국을 5g 기지국으로 바꾸려 합니다.
# 그런데 5g 기지국은 4g 기지국보다 전달 범위가 좁아, 4g 기지국을 5g 기지국으로 바꾸면 어떤 아파트에는 전파가 도달하지 않습니다.
#
# 예를 들어 11개의 아파트가 쭉 늘어서 있고, [4, 11] 번째 아파트 옥상에는 4g 기지국이 설치되어 있습니다.
# 만약 이 4g 기지국이 전파 도달 거리가 1인 5g 기지국으로 바뀔 경우 모든 아파트에 전파를 전달할 수 없습니다.
# (전파의 도달 거리가 W일 땐, 기지국이 설치된 아파트를 기준으로 전파를 양쪽으로 W만큼 전달할 수 있습니다.)
#
# 초기에, 1, 2, 6, 7, 8, 9번째 아파트에는 전파가 전달되지 않습니다.
# 기지국설치1_pvskxt.png
#
# 1, 7, 9번째 아파트 옥상에 기지국을 설치할 경우, 모든 아파트에 전파를 전달할 수 있습니다.
# 기지국설치2_kml0pb.png
#
# 더 많은 아파트 옥상에 기지국을 설치하면 모든 아파트에 전파를 전달할 수 있습니다.
# 기지국설치3_xhv7r3.png
#
# 이때, 우리는 5g 기지국을 최소로 설치하면서 모든 아파트에 전파를 전달하려고 합니다.
# 위의 예시에선 최소 3개의 아파트 옥상에 기지국을 설치해야 모든 아파트에 전파를 전달할 수 있습니다.
#
# 아파트의 개수 N, 현재 기지국이 설치된 아파트의 번호가 담긴 1차원 배열 stations,
# 전파의 도달 거리 W가 매개변수로 주어질 때,
# 모든 아파트에 전파를 전달하기 위해 증설해야 할 기지국 개수의 최솟값을 리턴하는 solution 함수를 완성해주세요
# N	stations	W	answer
# 11	[4, 11]	1	3
import math

N = 15
stations = [4,11,15]
w = 1
#답 = 3

# N = 16
# stations = [9]
# w = 2
#답 = 3
def solution(N,stations,w):
    W = w*2 +1
    #정답
    answer = 0
    start = 1
    #있는위치 갱신
    for s in stations:#기지국이 1,2,3,...이런식으로 설치 된 경우때문에 for문안에서 max(0,)과 비교해주어야한다.(밖으로 빼서 초기값 설정 ㄴㄴ)
        s = max(0,math.ceil((s - start -w) / W))

        #마지막 설치한 곳에서 +w+1칸 위치로 이동
        start = s + w + 1
    #마지막
    if start <= N:
        s = math.ceil((N-start+1)/W)
        answer += s
    return answer

print(solution(N,stations,w))











#
#
#
# from math import ceil
#
#
# def solution(n, stations, w):
#     answer = 0
#     W = 2 * w + 1
#
#     start = 1
#     for s in stations:
#         answer += max(ceil((s - w - start) / W), 0)#기지국이 붙어있는경우 음수가 나올 가능성이 있어 0과 max로 비교해준다.
#         start = s + w + 1
#
#     if n >= start:
#         answer += ceil((n - start + 1) / W)
#
#     return answer
#
# print(solution(N, stations, w))