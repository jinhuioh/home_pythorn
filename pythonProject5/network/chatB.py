#채팅프로그램을 만들어보자!
import socket#socket이 있어야 네트워크 통신이 가능하다.

#stream을 만들어야 하는데,
#한쪽으로만 흐른다.
#보내는 stream, 받는 stream
#socket은 3개를 따로 만든다.
#sock1는 보내는 용도, sock2는 받는 용도
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#AF_INET:IP를 말하는거. SOCK_DGRAM:UTP용 말하는거
sock2.bind(('192.168.219.101', 3000))#내 아이피와 4000이라는 주소가 생김
print('192.168.219.101, 3000 port node start!')
print('--------------------B------------------------')
while True:
    #b가 a에게 받는 부분
    data, addr = sock2.recvfrom(1024)
    print('간단 채팅B ', data.decode('utf-8'))

    data = input('간단채팅B ')
    sock1.sendto(data.encode('utf-8'),('192.168.219.101', 4000))