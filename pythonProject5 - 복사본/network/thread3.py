#현재 시각을 찍는 스레드 100번
#리스트에 있는 먹고 싶은 음식 목록 10개를 찍는 스레드
#1부터 500까지 카운트 하는 스레드
import datetime as dt
import threading#동시에 처리할 수 있게 해주는 함수
import time

dt_object = dt.datetime
def dt():
    for _ in range(100):
        time.sleep(5)#5초 단위로 시간 세기! 자바는 time.sleep(5000)
        print('현재시각', dt_object.now())#dt<-임포트한 객체.datetime()<-클래스

def food():
    food_list = ['사과', '물', '주수', '배추', '스프', '오이']
    for one in food_list:
        time.sleep(10)
        print('과일', one)
#1부터 500까지 카운트하는 스레드
def plus():
    for x in range(500):
        time.sleep(1)
        print('카운트>', x)

plus = threading.Thread(target = plus)
dt = threading.Thread(target = dt)
food = threading.Thread(target = food)

plus.start()#cpu 스캐줄링에 thread1대기줄에 세워줘
dt.start()#cpu 스캐줄링에 thread2대기줄에 세워줘
food.start()#cpu 스캐줄링에 thread3대기줄에 세워줘

