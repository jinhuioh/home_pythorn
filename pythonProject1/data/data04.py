good_rate = 2.5 #값을 넣을 때 변수의 타입이 결정됨.
bad_rate2 = input('나쁜 이자율 입력 ') #무조건 string
print(type(good_rate))
print(type(bad_rate2))

money = 100000
#이자 금액을 계산해봅시다.
print('좋은 이자금액은 ', int(money*good_rate))
print('나쁜 이자금액은 ', money*float(bad_rate2))

#아래 데이터는 연산의 대상이 됩니까? :아니요
tel = '01045678901' #연산의 대상이 된다라는 표현은 사칙연산. 자리수를 고려할 수 있는 데이터가 연산의 대상이다.

sn = '990909' #수치형 (대상에게 부여된 숫자)

#논리형
food = True
rain = False