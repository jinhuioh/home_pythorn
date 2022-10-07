# 문제
# 1부터 연속적으로 번호가 붙어있는 스위치들이 있다. 스위치는 켜져 있거나 꺼져있는 상태이다.
# <그림 1>에 스위치 8개의 상태가 표시되어 있다. ‘1’은 스위치가 켜져 있음을, ‘0’은 꺼져 있음을 나타낸다.
# 그리고 학생 몇 명을 뽑아서, 학생들에게 1 이상이고 스위치 개수 이하인 자연수를 하나씩 나누어주었다.
# 학생들은 자신의 성별과 받은 수에 따라 아래와 같은 방식으로 스위치를 조작하게 된다.
#
# 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다. 즉, 스위치가 켜져 있으면 끄고, 꺼져 있으면 켠다.
# <그림 1>과 같은 상태에서 남학생이 3을 받았다면, 이 학생은 <그림 2>와 같이 3번, 6번 스위치의 상태를 바꾼다.
#
# 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서,
# 그 구간에 속한 스위치의 상태를 모두 바꾼다. 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.
#
# 스위치 번호	①	②	③	④	⑤	⑥	⑦	⑧
# 스위치 상태	0	1	0	1	0	0	0	1
# <그림 1>
#
# 예를 들어 <그림 2>에서 여학생이 3을 받았다면, 3번 스위치를 중심으로 2번, 4번 스위치의 상태가 같고
# 1번, 5번 스위치의 상태가 같으므로, <그림 3>과 같이 1번부터 5번까지 스위치의 상태를 모두 바꾼다.
# 만약 <그림 2>에서 여학생이 4를 받았다면, 3번, 5번 스위치의 상태가 서로 다르므로 4번 스위치의 상태만 바꾼다.
#
# 스위치 번호	①	②	③	④	⑤	⑥	⑦	⑧
# 스위치 상태	0	1	1	1	0	1	0	1
# <그림 2>
#
# 스위치 번호	①	②	③	④	⑤	⑥	⑦	⑧
# 스위치 상태	1	0	0	0	1	1	0	1
# <그림 3>
#
# 입력으로 스위치들의 처음 상태가 주어지고, 각 학생의 성별과 받은 수가 주어진다.
# 학생들은 입력되는 순서대로 자기의 성별과 받은 수에 따라 스위치의 상태를 바꾸었을 때,
# 스위치들의 마지막 상태를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에는 스위치 개수가 주어진다. 스위치 개수는 100 이하인 양의 정수이다.
# 둘째 줄에는 각 스위치의 상태가 주어진다. 켜져 있으면 1, 꺼져있으면 0이라고 표시하고 사이에 빈칸이 하나씩 있다.
# 셋째 줄에는 학생수가 주어진다. 학생수는 100 이하인 양의 정수이다.
# 넷째 줄부터 마지막 줄까지 한 줄에 한 학생의 성별, 학생이 받은 수가 주어진다.
# 남학생은 1로, 여학생은 2로 표시하고, 학생이 받은 수는 스위치 개수 이하인 양의 정수이다.
# 학생의 성별과 받은 수 사이에 빈칸이 하나씩 있다.
#
# 출력
# 스위치의 상태를 1번 스위치에서 시작하여 마지막 스위치까지 한 줄에 20개씩 출력한다.
# 예를 들어 21번 스위치가 있다면 이 스위치의 상태는 둘째 줄 맨 앞에 출력한다.
# 켜진 스위치는 1, 꺼진 스위치는 0으로 표시하고, 스위치 상태 사이에 빈칸을 하나씩 둔다.

# 입력예시
# 8
# 0 1 0 1 0 0 0 1
# 2
# 1 3
# 2 3
# 출력예시
# 1 0 0 0 1 1 0 1
# 스위치 개수 입력받기
n = int(input())
# 스위치 상태 입력받기
switch = list(map(int,input().split()))
# 스위치 인덱스
sw_index = []
for i in range(1,n+1):
    sw_index.append(i)
# 사람수
people = int(input())
# 성별과 받은 숫자 입력
peopleList = []
for i in range(people):
    peopleList.append(list(map(int,input().split())))

#여자남자 나누어서 계산
# 남자인 경우
for peopleOne in peopleList:#peopleOne은 [1,3]과 같은 리스트
    # 남자인경우
    if peopleOne[0] == 1:
    #     받은 숫자의 배수인 경우 스위치를 변경
        for k in range(n):
            if sw_index[k] % peopleOne[1] == 0 and switch[k] == 0:
                switch[k] = 1
            elif sw_index[k] % peopleOne[1] == 0 and switch[k] == 1:
                switch[k] = 0
            else:
                pass
    # 여자인경우
    if peopleOne[0] == 2:
        #     받은 숫자를 기준으로 대칭인만큼 스위치 변경
        # 받은 숫자와 같은 위치의 스위치 바꾸기
        if switch[peopleOne[1]-1] == 0:
            switch[peopleOne[1] - 1] = 1
        else:
            switch[peopleOne[1]-1] = 0
        i=1
        while True:
            # 범위를 벗어나면 break
            if peopleOne[1]+i-1 > n-1 or peopleOne[1]-i-1 < 0:
                break
            elif switch[peopleOne[1]-i-1] == 0 and switch[peopleOne[1]+i-1] == 0:
                switch[peopleOne[1]-i-1],switch[peopleOne[1]+i-1] = 1, 1
                i+=1
            elif switch[peopleOne[1]-i-1] == 1 and switch[peopleOne[1]+i-1] == 1:
                switch[peopleOne[1]-i-1], switch[peopleOne[1]+i-1] = 0, 0
                i+=1
            else:
                break
# 한 줄에 20개씩 출력
if n<21:
    printSwitch = ' '.join(str(s) for s in (switch))
    print(printSwitch)
else:
    for i in range(1,(n//20)+1):
        switch20 = switch[20*(i-1):(20*i)]
        printSwitch = ' '.join(str(s) for s in (switch20))
        print(printSwitch)
    for k in range(n%20):
        # print('20*(n//20)+i',20*(n//20)+k)
        # print('switch[20*(n//20)+i]',switch[20*(n//20)+k])
        print(str(switch[20*(n//20)+k]),end=" ")



