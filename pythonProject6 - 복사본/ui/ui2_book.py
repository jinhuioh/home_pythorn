from tkinter import *
from tkinter import messagebox

from db.dao2_class import DAO

def save():
    #입력한 값 가져오기
    id = id_entry.get()
    name = name_entry.get()
    url = url_entry.get()
    img = img_entry.get()

    #vo에 넣어보자.
    vo = (id,name,url,img)
    #dao객체생성 후 해당 함수 호출
    dao = DAO()
    result = dao.create(vo)

    if result == 1:
        id_entry.delete(0, END)
        name_entry.delete(0, END)
        url_entry.delete(0, END)
        img_entry.delete(0, END)
        messagebox.showinfo('결과','db에 저장 성공!!!@@@')
    else:
        messagebox.showinfo('결과','db에 저장 실패!!!@@@')

def read():
    id = id_entry.get()
    dao = DAO()
    row = dao.read(id)
    print('검색결과는`~!~~', row)
    name_entry.insert(0, row[1])
    url_entry.insert(0, row[2])
    img_entry.insert(0, row[3])


window = Tk()
window.geometry('600x700')
icon = PhotoImage(file='r7.png')
top = Label(window, image=icon)
top.pack()#pack을 이용해 top을 label에 넣어줌

id_label = Label(window, text='id입력!!!')
id_label.pack()
id_entry = Entry(window, font=('애플 고딕', 20), bg='yellow', fg='red')
id_entry.pack()
name_label = Label(window, text='name입력!!!')
name_label.pack()
name_entry = Entry(window,font=('애플 고딕',20), bg='yellow', fg='red')
name_entry.pack()
url_label = Label(window,text='url입력!!!')
url_label.pack()
url_entry = Entry(window, font=('애플 고딕',20), bg='yellow', fg='red')
url_entry.pack()
img_label = Label(window, text='img입력!!!')
img_label.pack()
img_entry = Entry(window,font=('애플 고딕',20), bg='yellow', fg='red')
img_entry.pack()

save2 = Button(window, width='30',height='3', font=('애플 고딕',20),
               bg='pink', fg='skyblue',text='db에서 저장',command=save)
save2.pack()

read2 = Button(window, width='30', height='3', font=('애플 고딕',20),
               bg='pink', fg='skyblue', text='db에서 읽기',command=read)
read2.pack()

window.mainloop()