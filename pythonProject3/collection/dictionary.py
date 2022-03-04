#20:에서 저녁의 'tour'을 프린트 해보자. 아래 순서대로 해야함!!
hobby3 = [
    {10: {'아침':'game','저녁':'picture'}},
    {20: {'아침': 'coffee', '저녁': 'tour'}}
]
hobby30 = hobby3[1]#list값을 먼저 가져옴.0,1번 순서중 두번째 꺼
print(hobby30)
hobby300 = hobby30[20]#두번째 줄을 지정
print(hobby300)
hobby3000 = hobby300['저녁']#두번째줄에서 저녁key값을 빼옴
print('저녁일정은 ',hobby3000)


hobby = {10 : ['game','picture'], 20: ['tour','run','baking']}
#10대의 취미 목록을 프린트
#20대의 취미 목록을 프린트,카운트
print('10대의 취미는~~ ',hobby[10])
print('20대의 취미는~~ ',hobby[20])
s20 = hobby[20]
print('20대 취미 개수는~~ ',len(s20))

hobby2 = {10 : {'아침':'game','저녁':'picture'}, 20: ['tour','run','baking']}
s100 = hobby2[10]
print(s100)
s1000 = s100['저녁']
print(s1000)

food = {'아침':'토스트','점심':'한정식','저녁':'스프'}#key value형태로 넣음(dictionary)
print(food['아침'])#값을 확인할 때 :딕셔너리이름[키]
food['아침'] = '커피'# 값 수정
print(food)
food['간식'] = '쿠키'#값을 추가
print(food)

del food['간식']
print(food)

print('---')
#dic을 아래와 같이 for-each문으로 돌렸을때는 key만 가지고 온다.
for x in food:
    print(x)#실행해보면 key만 온다.

print('---')
for key in food:
    print(key, ':', food[key])#실행해보면 key만 온다.

dict1 = {100 : 'hong', 200 : 'kim'}
print(dict1[100])

for key in dict1:
    print(key, ':', dict1[key])

key_list = dict1.keys()
print('key목록만 가져오기1! ',key_list)
key_list2 = list(key_list)
print('list로 바꿔서 대괄호 값만 가져오기! ',key_list2)

value_list = dict1.values()
print(value_list)

#print(dic1[100])이랑 똑같음
print(dict1.get(100))
print(100 in dict1)#key 값들 중에서 100이 있니?: 결과가 bool(true,false)

#회원 명단 중에서 500이 있나요?
if 500 in dict1:
    print('500번 회원이 존재합니다.')
else:
    print('존재하지 않습니다.')