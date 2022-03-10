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
        print('연결성공!!!>> ', conn.host_info)
        cur = conn.cursor()
        #sql문 작성!!!
        sql = "insert into member values(%s,%s,%s,%s,%s)"
        result = cur.execute(sql, vo)
        print('sql문 전송 결과> ', result)

        conn.commit()
        conn.close()
    except:
        print('db연결 중 에러발생!')

def delete(id):
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
        print('연결성공!!!>> ', conn.host_info)
        cur = conn.cursor()
        # sql문 작성!!!
        sql = "delete from member where id = %s"
        result = cur.execute(sql, (id))
        print('sql문 전송 결과> ', result)

        conn.commit()
        conn.close()
    except:
        print('db연결 중 에러발생!')

def read(id):
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
        print('연결성공!!!>> ', conn.host_info)
        cur = conn.cursor()
        # sql문 작성!!!
        sql = "select * from member where id = %s"
        result = cur.execute(sql, (id))
        print('sql문 전송 결과> ', result)

        conn.close()
    except:
        print('db연결 중 에러발생!')
def all():
    pass
