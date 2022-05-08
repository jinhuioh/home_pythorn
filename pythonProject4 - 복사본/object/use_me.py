from object.me import Day

if __name__ == '__main__':
    #객체가 생성될 때 이니셜라이저 함수가 자동호출
    #멤버변수가 복사된다.!
    day1 = Day('자바공부', 10, '강남')#알트엔터하면 자동임포트
    print(Day.count)
    print('시간누적1 ',Day.time)
    day2 = Day('여행', 15, '강원도')#스택영역에 day1,2,3 3개의변수가 힙영역에 '자바공부', 10, '강남'이 값들이 전부 들어있는상태 긜고 init로 초기화까지 된 상태
    print(Day.count)
    print('시간누적1 ',Day.time)
    day3 = Day('운동', 11, '피트니스')
    print(Day.count)
    print('시간누적1 ',Day.time)
    print('시간평균', int(Day.time)/int(Day.count))

    #어디서 무엇을 했을까?
    print(day1)
    print(day2)
    print(day3)

    #전체 하는일의 시간은?
    print()