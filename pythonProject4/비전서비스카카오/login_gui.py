from tkinter import *
from tkinter import  messagebox
#버튼1개당 함수 1개를 연결
def login():
    messagebox.showinfo('제목','나를클릭!')
    #입력값 가져오고, 일치하는지 확인
w = Tk()
w.geometry('500x250')
#라벨을 만들어보자
id = Label(w, text = '아이디입력', font = ('궁서', 30)) #폰트는 튜플
id.pack()#pack을 이용해 id라는 라벨을w에 넣어줌.
id_entry = Entry(w, font= '궁서', bg = 'blue', fg = 'white')
id_entry.pack()

pw = Label(w, text = '암호입력', font = ('궁서', 30)) #폰트는 튜플
pw.pack()
pw_entry = Entry(w, font= '궁서', bg = 'blue', fg = 'white')
pw_entry.pack()

b = Button(w, text = '로그인처리', font = ('궁서', 30), bg = 'yellow',command= login)
b.pack()


w.mainloop()#계속 창 띄우고 있게 생성하기.(입력받고 창 없어지면 안되니까)
