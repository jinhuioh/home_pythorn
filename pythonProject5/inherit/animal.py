class Animal:
    name = ''
    def __init__(self, name):
        self.name = name
        #self =>생성된 객체(주소)
        #a1 = Animal('hong')
        #a1.name = 'hong'

    #기능(객체가 생성된 후 호출이 가능)
    #객체가 생성되면 주소가 생김
    #주소가 있어야 함수호출이 가능
    #객체가 생성되고, 주소가 있어야
    #이 기능을 쓸 수 있다.(함수호출을 할 수 있다.)
    def move(self):#멤버함수는 꼭 self넣어줘야함.!!
        print('moving')
    def speak(self):
        print('speak')
#상속!!!!
class Dog(Animal):#자바의 class Dog extends Animal 랑 같은 코드
    def speak(self):#재사용(=상속)
        print('멍멍')#재정의(override).

class Duck(Animal):
    def speak(self):
        print('꽥꽥!')