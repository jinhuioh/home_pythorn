#영화예매싸이트!
seat = [0]*10
while True :
    # 기본UI
    print('/n영화 예매 사이트입니다~')
    print('------------------------------')
    for x in range(0, 10):
        print(x, end='  ')
    print(x, end='  ')# end=' '를 넣으면 한 줄에 range(0,10)을 차례대로 나타내줌
    print()
    print('------------------------------')
    for x in seat:
        print(x, end='  ')
    print()
    print('/n------------------------------')
    #입력받는 부분
    no = int(input('예매좌석 선택~ (종료는 -1)'))

    if no == -1:# -1을 넣으면 while문이 break로 종료되게 하기.
        seat_count = seat.count(1)#좌석 개수 구하기,seat 배열에 1이 몇개 있는지 카운트
        print('좌석개수는 ',seat_count)

        price = 5000
        print('총 영화표 가격은 %d ' % (price*seat_count))
        seat_list = []#seat_list배열을 만들기. 값은 안넣은 상태
        for i in range(len(seat)):
            if seat[i] == 1:
                seat_list.append(i)#seat[i] == 1:라면 i값을 seat_list에 붙이기.
                print('예약된 좌석은 %s' % seat_list)
        break
    else:
        if seat[no] == 0:
            seat[no] =1#if문을 이용해 seat = [0]*10에서 0의 값을 1로 바꿔주기.
            print('좌석예약이 완료되었습니다.')
        else :
            print('이미 예약된 자리입니다. 다른 좌석을 선택해주세요')
            print('--=------=--=--------------')
