# 창업문제
# ------
# 직원을 뽑으려고 합니다.
# Worker('홍길동', 25, '남')
# Worker('김길동', 23, '여')
# Worker('박길동', 28, '남')
# Worker('이길동', 21, '남')
# Worker('장길동', 29, '여')
# ------
# 1. 전체 직원에 대한 정보를 프린트
# 2. 직원을 채용할 때마다 지금까지의 직원수를 프린트
# 3. 직원 나이의 평균 프린트
# 4. 성별 직원 수 프린트
class Worker:
    name = ''
    age = 0
    gender = ''
    count = 0
    age = 0
    f_gender = 0
    m_gender = 0
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Worker.count += 1
        Worker.age += age
        #if문을 이용해 gender에 여자와 남자를 따로 세어준다.
        if gender =='여':
            Worker.f_gender +=1
        else :
            Worker.m_gender +=1

    def __str__(self):
        return self.name +' '+ \
                str(self.age) +' '+ \
                self.gender

