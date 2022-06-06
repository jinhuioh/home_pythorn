#영화표 예약사이트!
#while True를 돌려서 계속 예약 받게하자.
# if문 사용해서 만약 -1을 input하면 종료되게 하자
# 배열을 2개 만들어야함 좌석 번호 1~10까지랑
#                   예약 되었는지 아닌지 보여주는 0*10 배열
# 예약하면 0배열의 값을 1로 바꿔주고
# 1로 이미 되어있으면 다른 자리를 예약 하도록 하기.
seat = [0]*10
while True:
    #틀 만들기
    print('')
    print('=======================')
    print('영화관 예약 사이트입니다.!')
    print('=======================')
    for x in range(0,10):
        print(x, end=' ')
    print('')
    for x in seat:
        print(x, end=' ')
    print('')
    no = int(input('예약좌석을 선택해주세요(종료-1)'))
    if no == -1:
        break
    else :
        if seat[no] ==0:
            seat[no] = 1
        else:
            print('이미 예약된 좌석입니다.! 다른좌석을 선택해주세요')