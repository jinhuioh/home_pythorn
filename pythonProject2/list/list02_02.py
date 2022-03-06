# #1.감자 고구마 양파를 순서대로 입력받아 food 리스트에 넣으세요.
# #1)고구마프린트,감자고구마 프린트,고구마 양파 프린트,감자를 라면으로 수정, 수정된 내용 프린트
import datetime
#
# food = []
# for _ in range(3): #count를 셀 때는 변수대신 _를 사용한다.
#     data = input('음식을 입력')
#     print(data)
#     food.append(data)
# print(food)
# print(food[1])
# print(food[0:2])
# print(food[0:])
# print(food[:3])
# food[0] = '라면'
# print(food)

#2.month = 10입니다. 계절을 프린트
#3~5:봄,6~8:여름,9~11:가을 12~2:겨울

# today = datetime.datetime.today()
#
# print(today.month)
# mon = input('계절을 입력해줘~ ')
# if mon == '[3:6]':
#     print('봄!')
# elif mon =='[6:9]':
#     print('여름!')
# elif mon =='[9:12]':
#     print('가을!')
# else :
#     print('겨울!')

#5. 시작값, 끝 값을 입력받아 시작과 끝 사이의 개수를 구하고, 합계를 구하고, 평균을 구하시오
start = int(input('시작 값을 입력~ '))
finish = int(input('끝 값을 입력~ '))

leng = len(range(start, finish+1))
print('시작과 끝 사이의 개수는~ ',leng)
sum = 0
for x in range(start, finish+1):
    sum = x + sum
    #sum += x
print('합계는 ',sum)
print('평균은 avg %0.2F' %(sum/leng))
