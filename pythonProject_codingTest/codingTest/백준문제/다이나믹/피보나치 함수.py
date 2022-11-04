# fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.
#
# fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
# fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
# 두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
# fibonacci(0)은 0을 출력하고, 0을 리턴한다.
# fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
# 첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
# fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
# 1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때,
# 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
#
# 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.
#
# 출력
# 각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.
#
# 예제 입력 1
# 3
# 0
# 1
# 3
# 예제 출력 1
# 1 0
# 0 1
# 1 2
# 예제 입력 2
# 2
# 6
# 22
# 예제 출력 2
# 5 8
# 10946 17711
from sys import stdin
n = int(input())

for i in range(n):
    m = int(stdin.readline())
    # 0일때 초기값은 변수에 따로 넣어주지 않음
    b0 = 0# 1일 때 초기값
    b=1# 1일 때 리턴되는 값
    if m == 0:
        print(1,b0)
    elif m == 1:
        print(0,b)
    else:
        # 피보나치 수열을 사용하기 위한 초기값
        # 0일때 초기값은 i-1일때 1의 초기값과 같으므로 따로 지정해주지 않았다.
        c11 = b0
        c1 = b
        for i in range(2,m+1):
            # i번째 피보나치수
            c_z = c1
            c_o = c11+c1
            ## 변수 갱신
            # m-2번째 값. i-2번째 값을 i-1번째 값으로 변경
            c11 = c1
            # m-1번째 값. i-1번째 값을 i번째 값으로 변경
            c1 = c_o
            # print('갱신한 값',c00,c0,c11,c1)
        print(c_z, c_o)





