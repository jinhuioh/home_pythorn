#다른 모듈에서 쓰는 함수들을 자주쓸때 항상 앞에 주소 붙여주기 힘드니까
#아래처럼 from~~으로 임포트 하면 편하게 코드 칠 수 있다.
from function.internet.crawl import *
#from function.internet.crawl import connect, find

connect()
find()
