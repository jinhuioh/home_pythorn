##
# 떡만들기
# 떡볶이의 떡길이가 일정하지않다.
# 대신 한 봉지에 들어가는 떡 총길이는 절단기로 잘라서 맞춰줌
# 절단기에 높이h를 지정하면 줄지어진 떡을 한 번에 절단한다.
# 높이가 h보다 긴 떡은 h위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.
# 예를들어 높이 19,14,10,17cm인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면
# 자른뒤 떡 높이는 15,14,10,15가 될것이다.
# 잘린떡의 길이는 4,0,0,2이다. 손님은 6cm만큼의 떡길이를 가져간다.
# 손님이 왔을 때 요청한 총 길이가 m일 때,
# 적어도 m만큼의 떡을 얻기 위해 설정할 수 있는 높이의 최대값을 구하는 프로그램을 작성해보자.
#
# 입력조건: 첫째 줄에 떡의 개수n과 요청한 떡의 길이m이 주어진다.
#         둘째줄에 떡의 개별 높이가 주어진다.
# 출력조건: 적어도m만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최대값 출력.
#
#예시:
# 입력 : 4 6
#       19 15 10 17
# 출력 : 15
##
import time

# 떡의 개수와 길이 입력
n, h = map(int, (input().split()))
# 떡 개별 높이 입력
riceCake = list(map(int, input().split()))

# 내 풀이 방법
# 각 떡길이에 똑같이 -k만큼해서 k*n = h가 되면 for문멈추는 방식으로 풀어보자.
# 함수화
def cut(riceCake, h):
    result = 0
    while True:
        # 가지고있는 떡길이의 최대값에서 -1씩 해나갈 것이므로 riceCake[i] <= max(riceCake)-1인 경우에 대해서는 떡 길이를 감소시키지 않는다.
        # 그 외에 경우에 대해서는 -1씩 감소하고 그 값들을 더한후 총 자른 값이 고객이 원하는 길이(h)와 같은 경우 print(h)를 리턴한다.(result=h)
        for i in range(len(riceCake)):
            if riceCake[i] <= max(riceCake)-1:
                continue
            else:
                riceCake[i] -= 1
                result += 1
                print('riceCake',riceCake)
                print('result',result)
            if result == h:
                return print(riceCake[0])
# 시간복잡도 확인을 위한 시간 측정
start_time = time.time()

cut(riceCake, h)

# 시간복잡도 확인을 위한 시간 측정
end_time = time.time()

print(start_time)
print(end_time)
print('수행시간', f"{end_time-start_time:.5f} sec")