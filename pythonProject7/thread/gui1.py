import turtle
t = turtle.Pen()

# for _ in range(10):
#     t.right(115)
#     t.forward(300)

while True:
    c = input('왼쪽 left, 오른쪽 right>> ')#방향설정
    a = int(input('각도입력>> '))#각도설정
    if c == 'left':
        t.left(a)
        t.forward(250)
    if c == 'right':
        t.right(a)
        t.forward(250)

# while True:
#     i = input('선택해! 1)네모 2)삼각형 >>')
#     if i == '1':
#         t.right(90)
#         t.forward(150)
#         t.right(90)
#         t.forward(150)
#         t.right(90)
#         t.forward(150)
#         t.right(90)
#         t.forward(150)
#     if i == '2':
#         t.right(120)
#         t.forward(100)
#         t.right(120)
#         t.forward(100)
#         t.right(120)
#         t.forward(100)