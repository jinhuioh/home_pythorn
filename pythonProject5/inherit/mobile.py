class Phone:

    def text(self):
        print('문자를 보내다.')

    def call(self):
        print('전화통화하다')

class SamsungPhone(Phone):
    name = ''
    # def __init__(self,name):
    #     self.name = name
    def game(self):
        print(self.name + '와 겜하다.')
    def internet(self,time):#time:지역변수
        print(str(time) + '시간 인터넷하다')

class ApplePhone(Phone):
    size = 0
    #int size;
    # def __init__(self, size):
    #     self.size = size

    def picture(self):
        print('사진을 찍다.')

    def youtube(self,time,subject):
        print(str(time) + '시간동안' + subject +'라는 주제로 유투브하다')