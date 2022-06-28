# 논리연산자
# and, or, !

# if 조건1 and 조건2 and 조건3:
# 처리 내용
# 조건1이 false면 조건2,3을 체크할 필요없으므로
# 조건1에 false일 가능성이 제일 큰 것을 넣음


# if 조건1 or 조건2 or 조건3:
# 처리 내용
# 조건1이 true이면, 조건2,3을 체크할 필요없으므로
# 조건1에 true일 가능성이 제일 큰 것을 넣음

#비교연산자
# ==, !=, >=, >, <=, <
# 스트링도 비교연산자로 비교 가능

import tkinter.messagebox as box

saved_id = 'root' #할당 연산자
saved_pw = '1234'

data_id = input('your id ')
data_pw = input('your password ')

if saved_id == data_id and saved_pw ==data_pw :
    print('seccess login~~!~!')
   # box.showinfo('result','success login~~')
else:
    #pass (else쓰고 안에 값을 안쓰고 싶으면 pass라고 써줘야한다.)
    box.showerror('result', '로그인실패')



