from inherit.animal1 import *

d1 = Tiger('k',10)
#     name =''
#     size = 0
#     def __init__(self,name,size):
#         self.name = name
#         self.size = size
#에 d1 = Tiger('k',10)의 값이 순서대로 들어감.
print(d1.name)
print(d1.size)
d1.move()#Tiger클래스에 move는 정의되어있지 않지만 부모클래스(Animal)에 있는 move를 사용할 수 있다.
d1.speak()

a1 = Animal('jini',20)#init__name,size 값에 jini가 들어가므로 프린트해주면 jini가 출력
print(a1.name)
a1.move()
a1.speak()