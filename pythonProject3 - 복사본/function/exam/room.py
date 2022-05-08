# 클래스 정리문제
# 1.exam 패키지내 room.py에 Tv클래스를 정의하고
# class 패키지 내에 my_room.py객체를 2개 생성해보세요
# 멤버변수는 3개, 맴버함수는 3개
# 객체마다 멤버변수의 값들을 프린트

class Tv:
    name = None
    price = 0
    def __str__(self):
        return str(self.name)+', '+str(self.price)

if __name__ == '__main__':
    my_room1 = Tv()
    my_room2 = Tv()

    my_room1.price = 100000000
    my_room1.name = 'jini'
    my_room2.price = 20000000
    my_room2.name = 'sena'
    print(my_room1)
    print(my_room2)