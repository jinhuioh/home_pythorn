from object.work import Worker

if __name__ == '__main__':
    worker1 = Worker('홍길동', 25, '남')
    print(worker1)
    print('채용인원', Worker.count)
    worker2 = Worker('김길동', 23, '여')
    print(worker2)
    print('채용인원', Worker.count)
    worker3 = Worker('박길동', 28, '남')
    print(worker3)
    print('채용인원', Worker.count)
    worker4 = Worker('이길동', 21, '남')
    print(worker4)
    print('채용인원', Worker.count)
    worker5 = Worker('장길동', 29, '여')
    print(worker5)
    print('채용인원', Worker.count)

    #전체 인원 구해보자.
    print('전체인원', Worker.count)

    #나이평균구해보자.
    print('나이평균은 ', Worker.age/Worker.count)

    #여성은 몇명인가?
    print('여성 전체인원: ', Worker.f_gender)
    print('남성 전체인원: ', Worker.m_gender)

