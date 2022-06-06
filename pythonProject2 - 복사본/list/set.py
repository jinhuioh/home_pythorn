#중복을 제거하고 싶을 때
import random

food_list = ['감자','감자','고구마']
food_list2 = set(food_list)
print(food_list2)
food_list3 = list(food_list2)
print(food_list3)

food_list4 = set()
food_list4.add('coffee')
food_list4.add('coffee')#중복 제거되어 프린트하면 커피가 한개만 나옴
food_list4.add('water')
print((food_list4))
print('--------')
food_list5 = list(food_list4)
print(food_list5)

number_list = set()
for _ in range(1000):
    number_list.add(random.randint(1, 1001))
print(number_list)#중복되지 않은 값들 프린트
print(len(number_list))#중복된 값 빼고 중복되지 않은 값들의 길이