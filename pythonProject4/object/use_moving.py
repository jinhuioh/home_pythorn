import object.moving as m  # 임포트 할 때 모듈까지는 써줘야함.

if __name__ == '__main__':
    # class instance(실제)인 object!
    c1 = m.Car('네모','red')  # new_Car()이랑 같음!!# 변수명 c1은 램의 저장공간이다!!
    # 객체 생성시 자동으로 멤버변수값을 초기화 해주는 함수를 하나 만들자(__str같은 것 )
    #셍상지 메서드,초기화해주는 것(initializer)
    # c1.shape = '네모'
    # c1.color = 'red'
    c2 = m.Car('세모','green')
    # c2.shape = '세모'
    # c2.color = 'green'
    print(c1)
    print(c2)
    c1.speed_up()#c1이라는 부품에는 speed_up만한거
    c2.speed_down()

if __name__ == '__main__':
    #객체 1개 생성
    b1 = m.Bike(100,'1001','동그라미')
    # b1.speed = 100
    # b1.size = '1001'
    # b1.shape = '동그라미'
    print(b1)# init를 이용!

    #리턴있는거 함수호출
    result = b1.sound_up()#10
    print(str(result))