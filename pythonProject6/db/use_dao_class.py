from db.dao_class import *

if __name__ == '__main__':
    dao = DAO()#__init__()호출함.db연결->cursor객체 생성
    dao.create()#sql문을 만들어서 전송, 결과 받아오면 됨.
    vo = input('id,name,url,img 입력>> ').split(',')  # 4개의 값을 리스트로 넣어줌
    print(vo)
    dao.create(vo)
