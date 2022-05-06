#북마크 테이블에 대한 크루드 기능 처리를 하고 싶음.
import sys
from tkinter import messagebox

from db.dao import *
#from 패키지명.모듈명 import *

#from db   import dao
#from 패키지 import 모듈
#-->모듈.함수(), 모듈.클래스명()
if __name__ == '__main__':#여기서부터 시작이니까 첫 실행은 여기서 하면 됨.
    choice = input('crud중 선택 1)c 2)u 3)d, 4)r(one) 5)r(all) >> ')
    if choice == '1':
        vo = input('id,name,url,img 입력>> ').split(',')#4개의 값을 리스트로 넣어줌#튜플은 split쓸 수 없다.
        # id = input('id입력>> ')
        # name = input('name입력>> ')
        # url = input('url입력>> ')
        # img = input('img입력>> ')
        # vo = (id, name, url, img)
        #create(id, name, url, img)
        create(vo)#튜플로 묶은 vo 가방만 넘겨준다.
    elif choice == '2':
        # id가 1이면, name은 naver2로 변경
        id = input('id입력>> ')
        name = input('name입력>> ')
        vo = (name,id)#튜플로 묶어서 vo가방에 넣어준다.
        print(vo)
        update(vo)#아이디 업데이트

    elif choice == '3':
        #id가 1이면 삭제
        vo = input('id입력>> ')
        print(vo)
        delete(vo)#아이디 삭제
        
    elif choice == '4':
        id = input('id>> ')
        print('id: ',id)
        row = read(id)#아이디를 주면서 검색해와라.
    #messagebox는 이 모듈안에 응집도를떨어트려서 안좋다. messagebox를 다른곳으로 분리시켜서 쓰던지 안써야 다른 사람들이 어디서든지 쓸 때 편함.꼭 필요한 코드가 아니기 때문에
        messagebox.showinfo('결과', '검색 결과는' + row[0]+', '+row[1]+', '+row[2]
                            +', '+row[3])

    elif choice == '5':
        all = all()#튜플에 튜플형태((),(),(),...)
        #전체리스트를 출력해주세요
        print('id     name      url                   img')
        print('---------------------------------------')
        for one in all:
            print('%s     %s    %s        %s' % one)
    else:
        sys.exit(0)#프로그램 종료