import random
import threading
import time
from tkinter import *
from tkinter import messagebox
# 1.함수호출시: label,x,y 입력값을 넣어줌
#     def __init__()객체생성시 3개의 입력값을 넣어줌.
#car가 9개인 경우

class RacingCar:
    #멤버변수
    name = ''#인스턴스변수
    counter = 0 #클래스 변수 (클래스에서 공유할 목적으로 만든 변수)

    #초기화함수
    def __init__(self, name, label, x1, y1):
        #self: 클래스로 생성한 객체!!
        #c1 = RacingCar('appleCar')#스택영역 변수
        #self == c1
        #c1.name = 'appleCar'
        self.name = name#힙영역변수


    #멤버함수
    def runCar(self):#멤버변수args=(car_label1, 10, 100)의 값들이  label, x1, y1에 순서대로 들어감.
        while True:#range(10)으로 하면 10번가고 끝나니까 몇번갈지 모르니까 while True로 해준다.
            #랜덤하게 움직일 값을 생성해서
            #램덤생성한 jump값을 기존의 x에 더해준다.
            #y축은 불변
            jump = random.randint(1, 20)
            print(jump)
            x1 = x1 + jump
            if x1>=400:
                RacingCar.counter +=1

                messagebox.showinfo('결과',
                str(RacingCar.counter)+':'+str(self.name))
                break
            self.label.place(x=int(self.x1), y=int(self.y1))
            time.sleep(0.05)

    #경주할 수 있는 화면부터 만들어보자.

def run_start(self):
    #라벨 객체 만들어서 window에 끼워넣어야 함.
    print('call ok!! ')
    # 자동차가 달리는 것처럼 보이는 처리를 스레드로 만들어야 함.
   #자동차 3대 만들기
    c1 = RacingCar('appleCar')
    c2 = RacingCar('summerCar')
    c3 = RacingCar('springCar')  # 6개의 변수 생성됨.. name까지 하면 7개 init self,name의 name말하는거

    # 스레드로 만들어서 자동차 경주를해보자!!!
    t1 = threading.Thread(target=c1.runCar, args=(car_label1, 10, 100))#car_label1 ,10부터 시작(초기값), y축 값
    t2 = threading.Thread(target=c2.runCar, args=(car_label2, 10, 150))
    t3 = threading.Thread(target=c3.runCar, args=(car_label3, 10, 200))
    #start를 해서 경주하게 하기!!
    t1.start()
    t2.start()
    t3.start()

if __name__ == '__main__':
    window = Tk()
    window.geometry('500x300')
    window.title('멀티 스레드 자동차 경주')
    b = Button(window, text='멀티스레드 시작', command=run_start)
    b.pack(side= TOP,fill= X, ipadx= 10,
           ipady= 10, padx=10, pady=10 )#ipadx:버튼과 x축여백,padx: 창끝에서 떨어트리기
    car_img1 = PhotoImage(file='car1.gif')
    car_img2 = PhotoImage(file='car2.gif')
    car_img3 = PhotoImage(file='car3.gif')
    car_label1 = Label(window, image=car_img1)
    car_label1.place(x=10, y=100)
    car_label2 = Label(window, image=car_img2)
    car_label2.place(x=10, y=150)
    car_label3 = Label(window, image=car_img3)
    car_label3.place(x=10, y=200)

    window. mainloop()