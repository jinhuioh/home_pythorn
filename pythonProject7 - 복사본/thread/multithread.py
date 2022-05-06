class RacingCar:
    #멤버변수
    name = ''

    #초기화함수
    def __init__(self, name):
        #self: 클래스로 생성한 객체!!
        #c1 = RacingCar('appleCar')#스택영역 변수
        #self == c1
        #c1.name = 'appleCar'
        self.name = name#힙영역변수

    #멤버함수
    def runCar(self):#멤버변수
        for _ in range(3):
            print(self.name + '~~달립니다.')
c1 = RacingCar('appleCar')
c2 = RacingCar('summerCar')
c3 = RacingCar('springCar')#6개의 변수 생성됨.. name까지 하면 7개 init self,name의 name말하는거
#스레드로 만들어서 자동차 경주를해보자!!!
c1.runCar()
c2.runCar()
c3.runCar()