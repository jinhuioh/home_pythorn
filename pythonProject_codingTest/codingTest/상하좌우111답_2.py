# 상하좌우
# 입력조건

# 첫째줄에 공간의 크기를 나타내는 N이 주어진다.
# 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다. L:왼쪽 1칸, R:오른쪽 1칸, U:위로 1칸, D:아래로 1칸
# 최소가(1,1)이므로 0의 값은 없다.
# 출력조건
# 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표(x,y)를 공백으로 구분하여 추출한다.시작은(1,1)이고 x가 상하, y가 좌우

# 공간의 크기 n*n매트릭스
n = int(input())
# dx,dy좌표를 지정
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

x = 1
y = 1
i = 0
move_list = (input().split())
print('move_list',move_list)

for move_one in move_list:
    for i in range(len(move)):
        if move_one == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 매트릭스 크기를 벗어나는 경우 continue함수를 통해 코드실행을 하지않고 넘긴다.(위에 연산 실행 안함)
    if ny < 1 or ny > n or nx < 1 or nx > n:
        continue
    x,y = nx, ny
print(nx, ny)