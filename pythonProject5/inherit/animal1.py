class Animal:
    name =''
    size = 0
    def __init__(self,name,size):
        self.name = name
        self.size = size
        
    def move(self):
        print('움직인다..')
    def speak(self):
        print('소리낸다.')

class Tiger(Animal):
    def speak(self):
        print('크와아앙')
        
class Bird(Animal):
    def speak(self):
        print('짹짹')