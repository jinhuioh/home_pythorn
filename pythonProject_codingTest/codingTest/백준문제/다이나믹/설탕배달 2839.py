# 문제
# 상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다.
# 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
#
# 상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다.
# 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면,
# 더 적은 개수의 봉지를 배달할 수 있다.
#
# 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)
#
# 출력
# 상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.


# 반복작업과 최대효율을 구하는 문제이므로 점화식을 사용해야하는 다이나믹 알고리즘 이용 문제이다!!
# min사용




n = int(input())

# 다이나믹은 초기화된 0으로된 리스트를 만들어주어야한다.(최대효율값을 넣을)
d = [0]*((n+1))
# n의 범위가 3이상이므로 그 전까지의 인덱스 값들을 넣어준다.
d[1] = 1
d[2] = -1
d[3] = 1
for i in range(4, n+1):
    # i = 4,7..과 같은 인덱스는 -1이 출력되도록 함.
    if d[i-5] == -1 and d[i-3] == -1:
        d[i] = -1
        continue
    # d[i]가 -1의 값이 아닌경우 -5와 -3중 최소연산값을 선택해 d[i]에 넣어준다.
    d[i] = min(d[i-5]+1, d[i-3]+1)
    # 만약 9라면 -5일때 4이고 -3일때 6이므로 이 경우 d[9] = -1이 들어가있으므로 d[6]+1로 바꾸어준다.
    if i%3 == 0:
        d[i] = d[i-3]+1
    # 5로 나누어떨어지지만 -3을했을 때 d[i]가 -1이 나오는 경우에 대해 아래와 같이 d[i]+1을 덮어 씌어 연산해준다.
    if i%5 == 0:
        d[i] = d[i-5]+1
    # 4에 대해 연산 값이 없으므로 직접 입력해준다.
    d[4] = -1
print(d[n])
