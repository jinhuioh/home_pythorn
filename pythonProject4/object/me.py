class Day:
    #클래스 인스턴스인 객체가 만들어질때마다
    # 메모리에 계속 생성됨.인스턴스 변수(클래스변수의 반대말)day1,day2,day3각각 생성.
    doing = ''
    time = 0
    location = ''
    count = 0 #누적용 변수
    time = 0#시간 누적해보자.

    def __init__(self,doing,time,location):
        self.doing = doing
        self.time = time
        self.location = location
        #이니셜라이저가 호출될 때마다
        #몇개의 객체가 생성되었는지 누적해보자.
        #self.count = self.count + 1#아래랑 똑같은 코드
        Day.count +=1#self.count +=1로 쓰면 객체당 따로따로 카운트하는거
        # Day로 쓰면 Day클래스에 변수가 뭐든지
        # 누적+1되게 만드는거(클래스변수)
        Day.time += self.time

    #함수를 한 개 만들어보자.
    def study(self):
        print(self.doing + '을 열심히 하다.')

    def __str__(self): #\를 쓰지 않으면 한줄 엔터쓰고 한줄 아래로 쓸 수 없다
        return self.doing + " " +\
                str(self.time) + "" + \
                self.location

