from inherit.animal import *

d1 = Dog('m')#아래에 a1 = Animal('hong')처럼
             # init name안에 m이 들어감.(상속받았기때문에가능)
d2 = Dog('m2')
d1.move()
d1.speak()
print('@@@',d1.name)
du1 = Duck('d')#dul1.name은 d가 된다.
du2 = Duck('d2')
print('dul1의 이름은',du1.name)
du1.move()
du1.speak()


a1 = Animal('hong')
#animal.py
#    def __init__(self, name):# hong이 name 안에 들어감.
#         self.name = name#<-이 name안에hong이 들어감!
a2 = Animal('happy')
print(a1.name+'!!')# . 은 접근연산자이다.
print(a2.name)
a1.move()