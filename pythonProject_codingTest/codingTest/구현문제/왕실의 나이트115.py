# 행복 왕국의 왕실 정원은 체스판과 같은 8*8좌표평면이다.
# 왕실 정원의 특정한 한 칸에 나이트가 서 있다.
# 나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동을 할 수 있으며
# 정원 밖으로는 나갈 수 없다. 나이트는 특정한 위치에서 다음과 같은 2가지 경우로 분류할 수 있다.
# 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
# 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
# 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오.
# 행위치는 1부터8로 표현, 열 위치는 a부터h로 표현한다.

# 현재위치
move = input()
count = 0
x = [1,2,3,4,5,6,7,8]
word = ['a','b','c','d','e','f','g','h']
step = [(-2,1),(-2,-1),(2,-1),(2,1),(1,2),(1,-2),(-1,2),(-1,-2)]
for i in range(len(word)):
    if move[0] == word[i]:
        nx = int(x[i])
print('nx',nx)
nx2 = int(move[1])
move_one = (nx,nx2)
for step_one in step:
    moveStep0 = move_one[0] + step_one[0]
    moveStep1 = move_one[1] + step_one[1]
    print('movestep0',moveStep0)
    print('movestep1',moveStep1)
    if moveStep0 > 0 and moveStep1 > 0:
        count+=1
        print(count)

print(count)
