# 상하좌우
# 입력조건

# 첫째줄에 공간의 크기를 나타내는 N이 주어진다.
# 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다. L:왼쪽 1칸, R:오른쪽 1칸, U:위로 1칸, D:아래로 1칸
# 최소가(1,1)이므로 0의 값은 없다.
# 출력조건
# 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표(x,y)를 공백으로 구분하여 추출한다.시작은(1,1)이고 x가 상하, y가 좌우

# 공간의 크기 n*n매트릭스
n = int(input())
# 여행자가 이동할 계획서
data = list(map(str,input().split()))
x = 1
y = 1
i = 0
for i in range(len(data)):
    if data[i] == 'L':
        if y==1:
            y=1
        else:
            y -= 1
        print('1:',x, y)
    elif data[i] == 'R':
        if y == n:
            y = n
        else:
            y += 1
        print('2:',x, y)
    elif data[i] == 'U':
        if x == 1:
            x =1
        else:
            x -= 1
        print('3:',x, y)
    else :
        if x == n:
            x = n
        else:
            x += 1
        print('4:',x, y)
    i += 1
print('결론',x,y)