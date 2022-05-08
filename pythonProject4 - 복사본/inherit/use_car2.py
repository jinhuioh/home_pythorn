#새로운 클래스를 만들 때
#기존의 있던 클래스를 "재사용"해서
#만드는 것을 상속이라고함
from object.moving import Car

class Sedan(Car):
    person = 0

    def tour(self):
        print('편안하게 여행을 가다.')

class Truck(Car):
    #기존에 있던 멤버변수2개, 멤버함수 2개를 가지고 태어남
    weight = 0#멤버변수3개

    def move(self):#멤버함수3개
        print('짐을 싣고 가다.')