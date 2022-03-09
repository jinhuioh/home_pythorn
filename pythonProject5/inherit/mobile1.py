class Phone:
    name = ''
    # def __init__(self,name):
    #     self.name = name

    def size(self):
        print('사이즈')

class Samsung(Phone):
    sound = 0
    # def __init__(self,sound):
    #     self.sound = sound
    def size(self,sound,name):
        print(str(sound)+'이고'+name+'이 이름인 폰이 작다')
        
    def price(self,name):
        print(name+'의 폰이 비싸다')
