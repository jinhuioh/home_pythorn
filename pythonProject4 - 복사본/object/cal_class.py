    #2개의 값을 전달받아서 연산을 수행
    #plus(1,2)
    #버튼을 누를 때마다 연산을 수행
    #plus(1)

    # 이니셜라이저: 객체가 생성될 때 마다
    #             멤버변수의 값을 넣어줌(초기화)
    # 멤버변수
    # 멤버함수
class Cal:

    def plus(self,num1,num2):
        return num1 + num2

    def minus(self,num1,num2):
        return num1 - num2

    def mul(self,num1,num2):
        return num1 * num2

    def div(self,num1,num2):
        return num1 / num2