#data access module(dao처럼)
#crud기능
#def 4개 필요!
#버튼하나당! 함수하나!
#함수로 모듈화시키는 작업!
import pymysql

def create(vo):
    try:
        conn = pymysql.connect(
            # 파라메터 #리턴이 있기 때문에 연결통로역할을 하는 conn을 써준다.
            # conn을 프린트하면 주소가 나옴!
            host='localhost',
            port=3366,
            user='root',
            password='1234',
            db='big',
            charset='utf8'
        )
        print('1. 연결성공~!~!', conn.host_info)#socket localhost:3366이주소가 프린트.
        # 연결된 통로(stream)을 통해, SQL문을 보내보자.
        # 2. 연결된 통로를 지정(접근할 수 있는) 커서 객체를 획득
        cur = conn.cursor()  # 접근할 수 있는 커서를 가져가락! 꼭 써줘야함

        # 3. sql문을 보내보자
        sql = "insert into book values (%s, %s, %s, %s)"#자바에서(?,?,?,?)랑 같음.

        # 커서로 sql문을 보냄
        result = cur.execute(sql,vo)#튜플()로 묶은 vo를 넣어주면
        #알아서 하나씩 sql문에 들어감.(%s, %s, %s, %s)여기에 순서대로.
        print('sql문 전송 결과> ', result)

        conn.commit()  # 내가 실행한 insert한 거 반영해줘! 꼭 써야함
        conn.close()  # lam 과 cpu 용량을 위해 내가 쓴거 닫아줌.

    except Exception as e:
        print('에러정보는 e')
        print('db연결 중 에러발생')

def read(id):#readOne
    try:
        conn = pymysql.connect(
            # 파라메터 #리턴이 있기 때문에 연결통로역할을 하는 conn을 써준다.
            # conn을 프린트하면 주소가 나옴!
            host='localhost',
            port=3366,
            user='root',
            password='1234',
            db='big',
            charset='utf8'
        )
        print('1. 연결성공~!~!', conn.host_info)
        # 연결된 통로(stream)을 통해, SQL문을 보내보자.
        # 2. 연결된 통로를 지정(접근할 수 있는) 커서 객체를 획득
        cur = conn.cursor()  # 접근할 수 있는 커서를 가져가락! 꼭 써줘야함

        # 3. sql문을 보내보자
        sql = "select * from book where id = %s"

        # 커서로 sql문을 보냄
        result = cur.execute(sql, (id))  # 튜플()로 묶은 vo를 넣어주면
        # 알아서 하나씩 sql문에 들어감.(%s, %s, %s, %s)여기에 순서대로.
        print('sql문 전송 결과> ', result)#1개 가져왔다고 결과값 나옴. 우리가 원하는 row내용을 주지 않는다.
        #select는 commit할 필요가 없다. read만 하니까!
        #!!!read 인 경우, 커서에 있는 연결통로(stream)검색 결과를 꺼내야 우리가 불러오는 내용을 받아볼 수 있다.
        row = cur.fetchone()#fetchone꺼낼 때 쓰는 함수.row 하나만 꺼내와라!
        print(row)
        conn.close()  # lam 과 cpu 용량을 위해 내가 쓴거 닫아줌.
        return row #검색결과를 return!

    except Exception as e:
        print('에러정보는 e')
        print('db연결 중 에러발생')

def all():#readAll
    try:
        conn = pymysql.connect(
            # 파라메터 #리턴이 있기 때문에 연결통로역할을 하는 conn을 써준다.
            # conn을 프린트하면 주소가 나옴!
            host='localhost',
            port=3366,
            user='root',
            password='1234',
            db='big',
            charset='utf8'
        )
        print('1. 연결성공~!~!', conn.host_info)
        # 연결된 통로(stream)을 통해, SQL문을 보내보자.
        # 2. 연결된 통로를 지정(접근할 수 있는) 커서 객체를 획득
        cur = conn.cursor()  # 접근할 수 있는 커서를 가져가락! 꼭 써줘야함

        # 3. sql문을 보내보자
        sql = "select * from book"

        # 커서로 sql문을 보냄
        result = cur.execute(sql)  # 튜플()로 묶은 vo를 넣어주면
        # 알아서 하나씩 sql문에 들어감.(%s, %s, %s, %s)여기에 순서대로.
        print('sql문 전송 결과> ', result)#1개 가져왔다고 결과값 나옴. 우리가 원하는 row내용을 주지 않는다.
        #select는 commit할 필요가 없다. read만 하니까!
        #!!!read 인 경우, 커서에 있는 연결통로(stream)검색 결과를 꺼내야 우리가 불러오는 내용을 받아볼 수 있다.
        #row = cur.fetchone()#fetchone꺼낼 때 쓰는 함수.row 하나만 꺼내와라!
        row = cur.fetchall()#많이꺼내!
        #row = cur.fetchmany(5)#row 개수를 정해서 꺼내
        print(row)
        conn.close()  # lam 과 cpu 용량을 위해 내가 쓴거 닫아줌.
        return row #검색결과를 return!

    except Exception as e:
        print('에러정보는 e')
        print('db연결 중 에러발생')

def update(vo):
    try:
        conn = pymysql.connect(
            # 파라메터 #리턴이 있기 때문에 연결통로역할을 하는 conn을 써준다.
            # conn을 프린트하면 주소가 나옴!
            host='localhost',
            port=3366,
            user='root',
            password='1234',
            db='big',
            charset='utf8'
        )
        print('1. 연결성공~!~!', conn.host_info)
        # 연결된 통로(stream)을 통해, SQL문을 보내보자.
        # 2. 연결된 통로를 지정(접근할 수 있는) 커서 객체를 획득
        cur = conn.cursor()  # 접근할 수 있는 커서를 가져가락! 꼭 써줘야함

        # 3. sql문을 보내보자
        sql = "update book set name = %s where id = %s"

        # 커서로 sql문을 보냄
        result = cur.execute(sql, vo)  # 튜플()로 묶은 vo를 넣어주면
        # 알아서 하나씩 sql문에 들어감.(%s, %s, %s, %s)여기에 순서대로.
        print('sql문 전송 결과> ', result)

        conn.commit()  # 내가 실행한 insert한 거 반영해줘! 꼭 써야함
        conn.close()  # lam 과 cpu 용량을 위해 내가 쓴거 닫아줌.

    except Exception as e:
        print('에러정보는 e')
        print('db연결 중 에러발생')

def delete(vo):
    try:
        conn = pymysql.connect(
            # 파라메터 #리턴이 있기 때문에 연결통로역할을 하는 conn을 써준다.
            # conn을 프린트하면 주소가 나옴!
            host='localhost',
            port=3366,
            user='root',
            password='1234',
            db='big',
            charset='utf8'
        )
        print('1. 연결성공~!~!', conn.host_info)
        # 연결된 통로(stream)을 통해, SQL문을 보내보자.
        # 2. 연결된 통로를 지정(접근할 수 있는) 커서 객체를 획득
        cur = conn.cursor()  # 접근할 수 있는 커서를 가져가락! 꼭 써줘야함

        # 3. sql문을 보내보자
        sql = "delete from book where id = %s"

        # 커서로 sql문을 보냄
        result = cur.execute(sql,vo)  # 튜플()로 묶은 vo를 넣어주면
        # 알아서 하나씩 sql문에 들어감.(%s, %s, %s, %s)여기에 순서대로.
        print('sql문 전송 결과> ', result)

        conn.commit()  # 내가 실행한 insert한 거 반영해줘! 꼭 써야함
        conn.close()  # lam 과 cpu 용량을 위해 내가 쓴거 닫아줌.

    except Exception as e:
        print('에러정보는 e')
        print('db연결 중 에러발생')