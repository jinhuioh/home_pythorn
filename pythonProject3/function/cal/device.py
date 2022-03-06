#입력, 처리내용, 반환
#add(100,200)
def add(x, y=555): #=>실행, x, y => 매개변수(파라메터)
    return x + y

def minus(x, y):
    return x - y

# def minus(x):
#     return x - 100
#이렇게 함수를 같은 이름으로 재사용(오버로딩)할 수 없다.

def mul(x, y):
    return x * y

def div(x, y):
    return x // y
