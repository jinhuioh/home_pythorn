#Car 클래스를 만들어보자.
class Car:
    color = None
    speed = 0

    #self == this(java)
    #해당class, Car
    def start(self):
        print('차가 출발하다')
    def stop(self):
        print('차가 멈추다')

    def __str__(self):
        return str(self.color) + ", " + str(self.speed)

if __name__ == '__main__':
    car1 = Car()#변수car1,변수 color,변수 speed #Car car = new Car() 와 같음(객체생성)
    car2 = Car()#변수car2, color, speed
    car1.color = 'red'
    car1.speed = 300

    car2.color = 'black'
    car2.speed = 400
    print(car1)
    print(car2)