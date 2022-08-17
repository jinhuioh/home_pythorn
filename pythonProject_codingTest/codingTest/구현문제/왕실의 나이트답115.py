# 행복 왕국의 왕실 정원은 체스판과 같은 8*8좌표평면이다.
# 왕실 정원의 특정한 한 칸에 나이트가 서 있다.
# 나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동을 할 수 있으며
# 정원 밖으로는 나갈 수 없다. 나이트는 특정한 위치에서 다음과 같은 2가지 경우로 분류할 수 있다.
# 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
# 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
# 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오.
# 행위치는 1부터8로 표현, 열 위치는 a부터h로 표현한다.

# 현재위치
# n = input()
# step = [(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
# text = ['a','b','c','d','e','f','g','h']
# num = [1,2,3,4,5,6,7,8]
#
# i,count = 0, 0
# for i in range(len(text)):
#     if n[0]== text[i]:
#         nx = int(num[i])
# print('nx', nx)
#
# nx2 = int(n[1])
# print(step[0])
# for step_one in step:
#     stepNx = step_one[0] + nx
#     stepNx2 = step_one[1] + nx2
#     if stepNx > 0 and stepNx2 > 0 and stepNx < 9 and stepNx2 < 9:
#         count += 1
#
# print(count)

# 책 방법
# 나이트 위치
input_data = input()
row = input_data[1]
#  ord(문자)
# 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환합니다.
# ord('a')를 넣으면 정수 97을 반환합니다.
colum = int(ord(input_data[0]))-int(ord('a'))+1
# ex) 97 - 97 + 1 = 1이 a일때의 열 값

# 이동가능한 방향 8가지
steps = [(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

result = 0
for step in steps:
    # 이동하고자하는 위치 확인
    next_row = int(row) + step[0]
    next_colum = int(colum) + step[1]
    if next_row >= 1 and next_colum >= 1 and next_row <= 8 and next_colum <= 8:
        result +=1
print(result)