#맴버변수 3개, 멤버함수 3개, 객체 1개만 생성해서, 맴버변수값 넣고 프린트
#멤버함수 2개 이상호출(리턴x,리턴o)
class Bike:
    #멤버변수(클래스변수)
    speed = 0
    size = ''
    shape = ''

    def __init__(self,speed, size, shape):
        self.speed = speed#self.speed 지역변수
        self.size = size
        self.shape = shape



    #맴버함수
    def start(self):
        print('start!')

    def stop(self):
        print('stop')

    def sound_up(self):
        return  10#리턴o
        print('바이크 소리를 업!')

    def __str__(self):
        return str(self.speed) +', '+ self.size +', '+ self.shape
class Car:
    #멤버변수
    color = '' #파이썬에서는 자동초기화 기능 없음. None으로 초기화 해줘야함
    shape = ''

    #이니셜라이저(멤버변수 초기화 목적으로 만들어두는 함수)
    #객체 생성시 자동호출됨.
    #객체가 2개가 만들어지면 2번 호출
    def __init__(self, color, shape1):#네모,레드 입력값 2개이므로 변수 2개.
        self.color = color
        self.shape = shape1


    #멤버함수
    def speed_up(self):   #나야! 카클래스꺼야 라는 의미의 self를써줘야함(자바의 this)
        print(self.color + '색인 자동차의 속도를 up!')
        #그냥color라고쓰면 어디에 있는 color인지 인식 못해서 꼭 self 를 써줘서
        #Car클래스 안에있는 color라는 것을 인식해주기 위해 self를 이용해 써줘야한다.


    def speed_down(self):
        print(self.color + '색인 자동차의 속도를 down!')

    def __str__(self):
        return self.color+ ', ' + self.shape