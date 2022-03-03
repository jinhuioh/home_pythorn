#tuple은 read_only한 리스트를 만들고 싶을 때

food_list = ['coffee','water','orange']
food_list2 = tuple(food_list)
#food_list2[0]= 'icecream'
#실행하면 오류남!!! tuple은 값을 바꿀 수 없는데 0번째에 icecream 을 넣었기 때문.

def yes():#def는javascript에서function이랑 같다.
    x = 100
    y = 200
    return(x, y)

result = yes()
print(result)#()소가로로 묶여서 오면 튜플이다.
result2 = list(result)#이렇게 list로 바꿔주면 값 변경 가능!