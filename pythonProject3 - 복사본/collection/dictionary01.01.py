#20:에서 저녁의 '티비'을 프린트 해보자. 아래 순서대로 해야함!!
hobby = [
    {10:{'아침':'game','점심':'요리','저녁':'공부'}},
    {20:{'아침':'운동','점심':'낮잠','저녁':'티비'}}
]
hobby1 = hobby[1]#list개수가 여러개이므로 우선 2번째 리스트를 꺼내준다.
print(hobby1)
hobby10 = hobby1[20]#2번째 리스트에서 {}의 값을 꺼내준다.
print(hobby10)
hobby100 = hobby10['저녁']#{}의 값에서 '저녁'에 해당하는 value값을 꺼내준다.
print(hobby100)

#10대의 취미 목록을 프린트
#20대의 취미 목록을 프린트,카운트
hobby2 = {10:['picture', 'swim'], 20:['sleep', 'cook', 'run']}
hobby20 = hobby2[10]
print(hobby20)#10대의 취미 목록을 프린트

hobby200 = hobby2[20]
print(hobby200)#20대의 취미 목록을 프린트

print(len(hobby200))#20대의 취미 목록을 카운트!!#배열의 길이를 알 면 되므로 len사용!!!

food = {'아침':'한정식','점심':'고기','저녁':'마카롱'}
food['아침'] = '커피'
print(food)

for x in food:
    print(x)#for문으로 돌리면 key 값만 가져온다.

for x in food:
    print(x,':',food[x])#food[key값] 하면 value가 프린트 된다.

food_list = food.keys()
print(food_list)
print('아침' in food)#key 값들 중에서 아침이 있니?: 결과가 bool(true,false)
print(100 in food)#key 값들 중에서 100이 있니?: 결과가 bool(true,false)

if '점심' in food:
    print('key 값으로 점심이 존재')
else :
    print('key 값으로 점심이 없음!!')