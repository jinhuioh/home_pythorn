#비교연산자
# ==, !=, >=, >, <=, <
# 스트링도 비교연산자로 비교 가능

import tkinter.messagebox as box

saved_id = 'root' #할당 연산자
data_id = input('your id ')
result = saved_id == data_id #비교의 결과는 무조건 bool!
print(result)
if(result) :# {}가 :이다. if조건문은 값이 무조건 bool이다.
    print('success login~~!') #꼭 tab키 눌러서 들여쓰기 해야 if 안에 들어가는걸로 인식한다.
    box.showinfo('result','success login~~')