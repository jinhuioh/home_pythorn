#콘도 예약 사이트

section = [0]*5
while True:
    print('------------------콘도 예약을 진행합니다.-------------------')
    print('원하는 지역을 신청해주세요(각 지역은 2명까지 신쳥 가능)')
    print('1)강원도 2)전라도 3)파주 4)제주도 5충청도')
    print('------------------------------')
    for x in section:
        print('  ',x, end='   ')
    print()
    no = int(input('원하시는 지역코드를 입력하세요 (종료를 원하면 0)  '))
    if no ==0:
        break

    elif section[no] < 2:
        # 예매처리
        section[no] += 1
        print('신청 가능합니다. ')
        print('신청이 완료되었습니다. ')

    else :
        print('====================================')
        print('!!!이미예약된 좌석입니다. 재입력 해주세요!!!')
        print('====================================')
