# # 좋은 방법이다!
# # n입력받기
# n= int(input())
# x, y = 1, 1
# plans = input().split()
# print('plans', plans)
# # LRUD에 대한 이동방향
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_type = ['L', 'R', 'U', 'D']
#
# # 이동계획을 하나씩 확인
# for plan in plans:
# #     이동 후 좌표 구하기
#     for i in range(len(move_type)):
#         if plan == move_type[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
# #   공간을 벗어나는 경우 무시
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
# #   이동수행
#     x, y = nx, ny
# print(x, y)
