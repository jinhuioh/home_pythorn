
try:
    food = ['coffee', 'water']
    food[2] = 'juice'
except IndexError as index:
    food[0] = 'juice'
    print(index)#에러정보 확인할 수 있음.
    print(food)
except ZeroDivisionError:
    print('특별히 예외처리할 내용이 없음')
except:#위에서부터 차례대로 예외처리하므로 except:를 마지막에 써줘야함.
    pass
#인덱스 에러이면, 첫번째 인덱스에 juice라고 넣어 예외처리
#Zero나누는 에러이면,'특별히 예외처리할 내용이 없음'이라고 프린트
#마지막에 반드시 '필요한 예외처리를 하였음'이라고 프린트


