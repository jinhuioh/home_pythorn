import turtle

t = turtle.Pen()

while True:
    choice = input('선택 1)네모 2)별 >> ')
    if choice == '1':
        for _ in range(4):
            t.right(90)
            t.forward(250)
    else:
        for _ in range(50):
            t.right(110)
            t.forward(250)