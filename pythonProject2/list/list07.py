#movie 예매 사이트

seat = [0]*10
while True:
    #기본UI
    print('/n영화 예매 사이트입니다~')
    print('------------------------------')
    print(' ',end='')
    for x in range(0,10):
        print(x, end='  ')
    print()
    print('------------------------------')
    print(' ',end='')
    for x in seat:
       print(x,end='  ')
    print()
    print('/n------------------------------')
    #입력받는 부분
    no = int(input('예매 좌석 번호 선택 (종료를 원하면 -1)  '))
    #-1을 입력하면 break로 종료됨.
    if no ==-1:
        #몇좌석 예매가 되었는지 프린트
        #list에 1이 몇개가 있는지 count
        seat_count = seat.count(1)
        print('좌석 개수  ',seat_count)

        #결제금액 한 자리당 1만원해서 프린트
        price = 10000
        print('예매금액 %d원' %(price*seat_count))

        #좌석 번호 프린트
        seat_list =[]
        for i in range(len(seat)):#좌석의 길의의 배열을 i 에 저장!!
            if (seat[i] == 1):
                seat_list.append(i)
        print('예매한 좌석은 %s' % seat_list)
        break
    else :
        # 예매가 이미 된 자리라면 재입력하라고 하기.
        if seat[no] == 0:
            seat[no] = 1
            print('예매가 완료되었습니다')
        else:
            print('이미예약된 좌석입니다. 재입력 해주세요!!')
            print('====================================')



