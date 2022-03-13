import random
import turtle
#클릭했을 때, 두가지 그림을 그리는 함수를 만들어보세요.
# 아무거나 둘 선택
# color,size가 변하게

def click(x,y):
    print(x, y)#x,y의 좌표 값
    while True:
        x2 = random.randint(-300, 300)
        y2 = random.randint(-300, 300)
        pen_size = random.randint(5, 20)
        color_list = ['yellow','red', 'pink','skyblue']
        # color_color = color_list[random.randint(0,5)]#리스트 값을 빼오려면 인덱스를 램덤하게 써줘야함.
        color_choice = random.choice(color_list)#리스트 값을 빼오려면 인덱스를 램덤하게 써줘야함.
        my_turtle.pensize(pen_size)
        my_turtle.pencolor(color_choice)

        if random.randint(1,2) ==1:#1,2를 랜덤하게 발생시키기
            size = random.randint(5, 100)

            my_turtle.penup()
            my_turtle.goto(x2,y2)
            my_turtle.pendown()
            for _ in range(4):
                my_turtle.right(90)
                my_turtle.forward(size)

        else:
            size = random.randint(5, 100)

            my_turtle.penup()
            my_turtle.goto(x2, y2)
            my_turtle.pendown()
            for _ in range(5):
                my_turtle.right(145)
                my_turtle.forward(size)

my_turtle = turtle.Turtle('turtle')#거북이만들기
#class Turtle:
#   def__init__(self):
#       거북이 화면 가운데에 보이게 해줘
turtle.title('거북이로 객체지향 사각형 그리기')
turtle.onscreenclick(click, 1)
# my_turtle.pensize(20)
# my_turtle.pencolor('skyblue')
turtle.done()

    # w = Tk()

    # 여러 설정값들
    # 여러 설정값들
    # 여러 설정값들

    # w.mainroof()#여러 설정값들을 마지막에 끝내주는 함수. turtle.done()이랑 비슷한 맥락