# member_dao.py
# -crud함수 구현: 회원가입,회원탈퇴,회원정보,로그인처리
#               create delete  read   id,pw를 주고 read하면 됨!
# use_member.py
# -main
from db.member_dao import *
if __name__ == '__main__':
    choice = input('crud중 선택 1)c 2)d 3)r(one) 4)login >> ')
    if choice =='1':
        vo = input('id,pw,name,tel,email을 입력>>').split(',')
        create(vo)
    elif choice =='2':
        id = input('삭제할 아이디 입력>> ')
        print(id)
        delete(id)
    elif choice =='3':
        id = input('read할 아이디를 입력>> ')
        print('id: ', id)
        row = read(id)
        print(row)
