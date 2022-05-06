import pymysql

try:
    conn = pymysql.connect(
        #파라메터 #리턴이 있기 때문에 연결통로역할을 하는 conn을 써준다.
        #conn을 프린트하면 주소가 나옴!
        host= 'localhost',
        port= 3366,
        user='root',
        password='1234',
        db='big',
        charset='utf8'
    )
    print('1. 연결성공~!~!',conn.host_info)
    #연결된 통로(stream)을 통해, SQL문을 보내보자.
    #2. 연결된 통로를 지정(접근할 수 있는) 커서 객체를 획득
    cur = conn.cursor()#접근할 수 있는 커서를 가져가락! 꼭 써줘야함

    #3. sql문을 보내보자
    sql = "insert into book values ('5','hi','http://www.himedia.com','hi.png')"

    #커서로 sql문을 보냄
    result = cur.execute(sql)
    print('sql문 전송 결과> ',result)

    conn.commit()#내가 실행한 insert한 거 반영해줘! 꼭 써야함
    conn.close()#lam 과 cpu 용량을 위해 내가 쓴거 닫아줌.






except Exception as e:
    print('에러정보는 e')
    print('db연결 중 에러발생')