#반복문은 2가지 경우에 사용
#1.횟수를 세기 위해서
#2. 반복하면서 어떤처리를 하기 위해
import datetime

for _ in range(5):#[0,1,2,3,4] count 용으로만 쓰려면 _를 해준다.
    print('환영합니다')

sum = 0
for n in range(1, 6):#1~5까지 더하기
    sum = sum + n
    print(sum)


#문제풀어보자
#1.감자 고구마 양파를 순서대로 입력받아 food 리스트에 넣으세요.
#1)고구마프린트,감자고구마 프린트,고구마 양파 프린트,감자를 라면으로 수정, 수정된 내용 프린트
print('--------------------')
# food = ['감자','고구마','양파']
# print(food[1])
# print(food[0:2])
# print(food[1:3])

food = []
for _ in range(3):#3번 입력받기
    data = input('음식을 입력!! ')
    food.append(data)

print(food[1])
print(food[0:2])
print(food[1:])
food[0] = '라면'
print(food)

#2.month = 10입니다. 계절을 프린트
#3~5:봄,6~8:여름,9~11:가을 1~2:겨울
today = datetime.datetime.today()
print(today.month)
mon = input('몇월인가요?')
print(mon)
if mon=='[3:6]':
    print('봄입니다.')
else:
    print('겨울입니다.')

# 3.10부터 20까지 더한 값을 프린트
for n1 in range(10, 21):
    sum = n1 + sum
    print(sum)

#5. 시작값, 끝 값을 입력받아 시작과 끝 사이의 개수를 구하고, 합계를 구하고, 평균을 구하시오

fn = input('첫번째 숫자를 입력하세요 ')
ln = input('두번째 숫자를 입력하세요 ')
for n2 in range(fn, ln+1):
    sum = n2 + sum
    print(sum)




