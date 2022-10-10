a= 2

def A(a):
    a = 5
    return print('1', a)
def main1():
    A(a)#여기서 리턴받은 a와 아래 main함수에서 return 하는 a는 다른 a이다.(변수만 똑같이 씀)
    return a
print(main1())


a,b = map(int,input('A,B상품 정가 입력(공백을 기준으로 입력해주세요!)',).split())
sale = int(input('할인율은? ',))
def get_fixed_price(A,Sale):
    print(A,'상품의 할인된 가격은? ',round(A*(100-Sale)/100))

get_fixed_price(a,sale)
get_fixed_price(b,sale)

def get_fixed_price():
    a,b = map(int,input('A,B상품 정가 입력(공백을 기준으로 입력해주세요!)',).split())
    sale = int(input('할인율은? ',))
    print('a 상품의 할인된 가격은? ',round(a*(100-sale)/100))
    print('b 상품의 할인된 가격은? ',round(b*(100-sale)/100))
get_fixed_price()
