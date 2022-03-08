from inherit.animal import *

d1 = Dog('m')
d2 = Dog('m2')
d1.move()
d1.speak()

du1 = Duck('d')
du2 = Duck('d2')
du1.move()
du1.speak()


a1 = Animal('hong')
#animal.py
#    def __init__(self, name):# hong이 name 안에 들어감.
#         self.name = name#<-이 name안에hong이 들어감!
a2 = Animal('happy')
print(a1.name)# . 은 접근연산자이다.
print(a2.name)
a1.move()