# function패키지 내에 exam 패키지내에
# tour.py를 만들어서 spring(), summer()함수 정의(def사용)
#
# 호출은 move.py에서!
# spring(3, '제주도')
# =>3월에 제주도에 가요! 프린트
# summer('울릉도', 8) #default값 10000
# =>8월에 울릉도를 가는 비용은 10000
# if 원입니다:
#     =>조건처리 6이면 비용이 -2000원할인해서 8000원이 되도록
#       7이면 -1000원 할인해서 9000원이 되도록
#       나머지 월이면 +2000원해서 12000원이 되도록.

def spring(month , location):
    # spring(3, '제주도')
    data = str(month) +'월에 '+ str(location)+'에 가요!'
    print(data)

    #default로 설정하고 싶으면 파라메터 위치를
    #뒤에서부터 써주어야 한다.
    #앞의 파라메터는 입력해주고, 입력해주지 않은 뒤의 파라메터를
    #default값으로 입력해주라고 처리되기 때문!!
    #location, month, price = 10000 이런식으로

def summer(location, month =8, price = 10000):
    if month == 6:
        price -= 2000
    elif month ==7:
        price -= 1000
    elif month ==8:
        pass
    else :
        price += 2000
    data = str(month) +'월에'+ str(location) +'에 가는 비용은'+ str(price) +"원 입니다."
    return data

if __name__ == '__main__':
  #spring함수는 값이 (3, '제주도')로 한개이므로 변수에 따로 넣어주지 않아도 된다.
    spring(3, '제주도')
  #summer함수는 값이 월에 따라 다양하므로 변수(result,result1)에 각각 넣어 프린트 해준다.
    result = summer('울릉도', 8)
    print(result)

    result2 = summer('울릉도', 6)
    print(result2)
    