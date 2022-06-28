#str 확인문제
#주민번호 13자리 입력 받아서
#나이와 성별 프린트
#현재날짜
import datetime
today = datetime.datetime.today()

print(today.year, today.month, today.day)
print(today.hour, today.minute, today.second)

print('------------------------')

data = '9809292214532'
print(data[0:2])
print(data[6:8])

print('------------------------')

birth = data[0:2]
print(birth)

gender = data[6:8]
print(gender)
print('첫번째는 {b} 마지막은{g}'.format(b=birth,g=gender))

print('------------------------')

sn = input('주민번호 13자리 입력~~ ')

year = sn[0:2] #나이 계산해보자
sex = sn[6]

if sex =='1' or sex =='3': #if sex in ('1','3'): 이렇게 써도 된다.
    print(year)
    print('남자')
else:
    print(year)
    print('여자')

print('------------------------')

print(year)

year2 = int(year)+1900 #int(),float(),float(),str(),tuple(),list()등 타입을 바꿀 수 있다.
print(year2)

age = today.year-year2+1
print('나이는~~: ',age)