class Food:
    name = ''
    price = 0
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def size(self):
        print('size')

class Banana(Food):
    color = ''
    def __init__(self,color):
        self.color = color

    def size(self,color):
        print(color+'인 바나나가 크다.')