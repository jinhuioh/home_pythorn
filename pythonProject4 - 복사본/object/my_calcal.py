#객체지향 클래스를 만들때: 결합도가 낮고 응집도가 높은 코드가 좋다.
from functools import partial
from tkinter import *
from unittest import result
from object.cal_class import Cal

cal = Cal()
def result(op):
    #입력값 가져오고, 일치하는지 확인
    num11 = float(num1_entry.get())
    num22 = float(num2_entry.get())
    if op == '+':
        cal_result1 = cal.plus(num11, num22)
        result.config(text=cal_result1)
    elif op == '-':
        cal_result2 = cal.minus(num11,num22)
        result.config(text=cal_result2)
    elif op == '*':
        cal_result3 = cal.mul(num11,num22)
        result.config(text=cal_result3)
    elif op == '/':
        cal_result4 = cal.div(num11,num22)
        result.config(text=cal_result4)



def reset():
    num1_entry.delete(0, END)  # entry값 지움
    num2_entry.delete(0, END)  # entry값 지움

    result.config(text='')  # 라벨 text지우기

if __name__ == '__main__':
    w = Tk()
    w.geometry('500x250')
    #라벨을 만들어보자
    num1 = Label(w, text = '숫자를입력', font = ('궁서', 30)) #폰트는 튜플
    num1.pack()#pack을 이용해 num1라는 라벨을w에 넣어줌.
    num1_entry = Entry(w, font= '궁서', bg = 'blue', fg = 'white')
    num1_entry.pack()

    num2 = Label(w, text = '숫자를입력', font = ('궁서', 30)) #폰트는 튜플
    num2.pack()#pack을 이용해 num2라는 라벨을w에 넣어줌.
    num2_entry = Entry(w, font= '궁서', bg = 'blue', fg = 'white')
    num2_entry.pack()



    #덧셈을 해보자!
    b1 = Button(w, text = '+', font = ('궁서', 30), bg = 'yellow',
               command= partial(result, '+'))
    b1.pack()

    b2 = Button(w, text = '-', font = ('궁서', 30), bg = 'yellow',
               command= partial(result, '-'))
    b2.pack()

    b3 = Button(w, text = '*', font = ('궁서', 30), bg = 'yellow',
               command= partial(result, '*'))
    b3.pack()

    b4 = Button(w, text = '/', font = ('궁서', 30), bg = 'yellow',
               command= partial(result, '/'))#버튼 누르면 command 에 login함수를 자동으로 호출해준다.
    b4.pack()

    #리셋버튼!
    br = Button(w, text = '리셋', font = ('궁서', 30), bg = 'yellow',
               command= reset)
    br.pack()

    result = Label(w, font = ('궁서', 30), text = 'result')
    result.pack()
    w.mainloop()#계속 창 띄우고 있게 생성하기.(입력받고 창 없어지면 안되니까)