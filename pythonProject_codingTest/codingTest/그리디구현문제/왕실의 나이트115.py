# 행복 왕국의 왕실 정원은 체스판과 같은 8*8좌표평면이다.
# 왕실 정원의 특정한 한 칸에 나이트가 서 있다.
# 나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동을 할 수 있으며
# 정원 밖으로는 나갈 수 없다. 나이트는 특정한 위치에서 다음과 같은 2가지 경우로 분류할 수 있다.
# 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
# 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
# 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오.
# 행위치는 1부터8로 표현, 열 위치는 a부터 h로 표현한다.

# 입력조건: 첫째 줄에 8*8좌표 평면상에서 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력된다.
# 입력문자는 a1처럼 열과 행으로 이루어진다.

# 줄력조건: 첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오.


y = [1,2,3,4,5,6,7,8]#행=세로
x = ['a','b','c','d','e','f','g','h']#열=가로
m,i,result = 0,0,0
# x를 숫자로 변환
n = list(input())
x0 = n[0]#입력받은 수에서 행
y0 = n[1]#입력받은 수에서 열
for i in range(len(x)):
    if x0 == x[i]:
        x0 = i+1
a = [2,2,-2,-2,1,1,-1,-1]#이동할 수 있는 행렬 순서
b = [1,-1,1,-1,2,-2,2,-2]#이동할 수 있는 행렬 순서
for m in range(len(a)):
    xx, yy = 0,0
    xx = int(x0) + a[m]
    yy = int(y0) + b[m]
    if xx < 1 or xx > 8 or yy < 1 or yy > 8:
        continue
    result += 1
print(result)


#
# # 현재위치
# move = input()
# count = 0
# x = [1,2,3,4,5,6,7,8]
# word = ['a','b','c','d','e','f','g','h']
# step = [(-2,1),(-2,-1),(2,-1),(2,1),(1,2),(1,-2),(-1,2),(-1,-2)]
# for i in range(len(word)):
#     if move[0] == word[i]:
#         nx = int(x[i])
# print('nx',nx)
# nx2 = int(move[1])
# move_one = (nx,nx2)
# for step_one in step:
#     moveStep0 = move_one[0] + step_one[0]
#     moveStep1 = move_one[1] + step_one[1]
#     print('movestep0',moveStep0)
#     print('movestep1',moveStep1)
#     if moveStep0 > 0 and moveStep1 > 0:
#         count+=1
#         print(count)
#
# print(count)
