import random
import threading
#실처럼 작게 프로그램을 나누어 처리
#동시 프로그램
#1부터 100까지 증가
def plus():
    for x in range(101):
        print('증가', x)
#100부터 1로 감소
def minus():
    for x in range(100, 0, -1):
        print('감소', x)
def text():
    text = ['@','#','$','%','*','&']
    for _ in range(100):
        print('특수문자', random.choice(text))

plus = threading.Thread(target = plus)
minus = threading.Thread(target = minus)
text = threading.Thread(target = text)

plus.start()#cpu 스캐줄링에 thread1대기줄에 세워줘
minus.start()#cpu 스캐줄링에 thread2대기줄에 세워줘
text.start()#cpu 스캐줄링에 thread3대기줄에 세워줘

