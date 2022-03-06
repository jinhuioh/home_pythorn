import datetime

def get_list(food):
    if food =='korean':
        data = ['냉면','오미자차','팥빙수']
    elif food == 'japan':
        data = ['우동', '생면']
    else:
        data = ['라면', '커피']
    return data #반환은 list형!!

def get_day():
    return datetime.datetime.today()

def get_day2():
    today = datetime.datetime.today()
    return today.month,today.hour

if __name__ == '__main__':
#파라미터로 값을 넘겨,def get_list(food): 실행하면food='japan'으로 실행된다.
#리턴은 여러개일 수 있다.
#하나의 변수에 리턴값을 넣어주면 tuple로 묶어준다.
    result3 = get_day2()
    print(result3)
    print(result3[0])
    print(result3[1])
    print('------------')
    a, b = get_day2()#위 방법과 동일 a,b를 지정해서 값을 꺼낼 수 있다.
    print(a)
    print(b)

    a2, _=get_day2()#a2값만 가져오고 싶을 때
    print(a2)

#return 은 datetime객체
#맴버변수, 맴버함수
    result2 = get_day()
    print(type(result2))
    result = get_list('japan')
    print(result)