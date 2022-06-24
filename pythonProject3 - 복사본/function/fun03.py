#function.fun02에있는 call1()함수를 호출하고 싶다!!
#python은 다른 모듈에 있는 함수, 클래스를
#사용할 때는 import해주어야 어디에 있는지 위치를 찾는다.
import function.fun02 as f02
#import 패키지.모듈명(파이썬파일명)
f02.call1()
#실행해보면 fsun02에서 실행한 값까지 여기서 호출되버린다.
print('-------------')
#main을 생성하면 fum02와 상관없이 fun03에 call1() 함수가 돌아간다.
if __name__ == '__main__':
    f02.call1()

