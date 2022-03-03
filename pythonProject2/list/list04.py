#2.month = 10입니다. 계절을 프린트
#3~5:봄,6~8:여름,9~11:가을 1~2:겨울
import datetime
import random

today = datetime.datetime.today()
month = today.month#3월 
if month ==12 or 1 <= month <=2:
    print('겨울')
elif 3<= month <=5:
    print('봄')
elif 6 <= month <= 8:
    print('여름')
elif 9 <= month <= 11:
    print('가을')
else:
    print('해당계절이 없습니다.')


#4.target = 55임
target = random.randint(1,100)
cnt = 0

while True:
    number = int(input('숫자를 입력~~~ '))
    cnt += 1
    if number != target:
        if(number>target):
            print('too big')
        else:
            print('too small')
    else:
        print('correct!!')
        break
