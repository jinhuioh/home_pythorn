# 클래스 정리문제
# 2.exam 패키지내 shop.py에 Shop클래스를 정의하고
# 멤버변수 2개의 값을 확인하고, 함수 2개를 호출해보세요
# 멤버변수는 임의로, 함수는 다음과 같이 정의하여 호출
# total_price(5,3000) #5:주문수량, 3000:음료가격
# =>총결제금액은 15000원입니다. 라고 프린트
# total_count(200)
#200:오늘 방문객수, default 100는 평균 방문객수

class Shop:
    price = 0
    coun = 0
    count = 100

    def __str__(self):
        return str(self.price)+', '+str(self.coun)

if __name__ == '__main__':
    total = Shop()

    total.price = 3000
    total.coun = 5
    total_price = str(total.coun)+', '+str(total.price)
    print(total_price)
    print('총 결제금액은~ ', total.price*total.coun)
    total_count = 200
    print('오늘 방문객수 ',total_count)
    print('평균 방문객수 ',total.count)


