import random
import turtle

def click(x, y):
    print(x, y)
    x2 = random.randint(-300, 300)
    y2 = random.randint(-300, 300)
    pen_size = random.randint(5, 30)
    color_list = ['yellow','red', 'purple','pink']
    # color_color = color_list[random.randint(0,5)]#리스트 값을 빼오려면 인덱스를 램덤하게 써줘야함.
    color_choice = random.choice(color_list)#리스트 값을 빼오려면 인덱스를 램덤하게 써줘야함.
    my_turtle.pensize(pen_size)
    my_turtle.pencolor(color_choice)
    # my_turtle.penup()#펜 들고 이동(그리진않음) pendown:그림을 그리겠다.
    # my_turtle.goto(x, y)
    # my_turtle.pendown()
    my_turtle.goto(x,y)

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