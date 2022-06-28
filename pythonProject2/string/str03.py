today = '오늘은 목요일 입니다. 코로나 검사 해야합니다.'
print(today.find('목요일')) #해당글자가 시작하는 인덱스가 print.
print(today.find('독감'))#-1은 값이 없다 라는 의미
print(today.count('니다'),'번 있다.')
print(today.count('코로나'),'번 있다.')

print('----------------------------')
#뉴스기사를 가져와서 글자수를 찾아보자~
news = '''

영국 왕실은 20일(현지시간) 여왕이 코로나19로 경증이면서 감기 같은 증상을 겪고 있으며 이번 주에 윈저성에서 가벼운 업무를 계속할 것으로 예상된다고 밝혔다.

왕실은 여왕이 치료를 계속 받고 모든 적절한 지침을 따를 것이라고 말했다.

여왕은 지난해 10월 부스터샷을 완료한 것으로 알려졌다고 BBC와 스카이뉴스 등 영국 언론들이 보도했다.

여왕은 이달 초 코로나19에 재감염된 찰스 왕세자와 접촉했다.

73세인 찰스 왕세자는 10일 정기 검사에서 코로나19 양성 판정을 받은 뒤 자가격리를 했고, 지금은 활동을 재개한 상태다.

여왕과는 확진 이틀 전 윈저성에서 대면한 것으로 알려졌다. 당시 왕실은 여왕의 코로나19 감염 여부를 공개하지 않았다.

찰스 왕세자의 부인인 커밀라 파커 볼스(74)도 처음엔 음성 판정을 받았으나 14일에는 결국 자가격리에 들어갔다.

윈저성 직원들 사이에서도 코로나19 확진자가 여럿 나온 것으로 알려졌다.

'''

print(len(news),'글자입니다.')
print(news.find('볼스'),'번째 인덱스에 해당 글자 시작!')
print(news.count('했다'))

#거꾸로 인덱스로 값 가져오기.
print(today[-3])
print(today[-2])

today2 = ','.join(today)
print(today2)

print('----------------------')

food = ['감자','고구마','양']
food2 = ' '.join(food)
print(food2)
print(type(food2))
print(len(food2))

#대소문자 구분없이 모두를 대문자, 소문자로 바꾸어 처리해보자.
id = 'root'
id2 = 'Root'

print(id.upper() == 'ROOT') #모두 대문자로
print(id.lower() == 'root') #모두 소문자로

#공백없애기
id3 = 'root '
print(len(id3.lstrip())) #왼쪽 공백 없애고 길이 프린트
print(len(id3.rstrip())) #오른쪽 공백 없애기
print(len(id3.strip())) #양쪽 공백 없애기

count = []
i=0
while i>-1:
    i = news.find('볼스',i)
    if i>-1:
        count.append(i)
        i +=len('볼스')
print('볼스 위치 ', count)
print('=======================')

#특정한 글자 바꾸기
news2 = news.replace('볼스', '진희')
print(news2)

news2 = news.split()
print(len(news2))
print(type(news2))
print(news2) #split으로 str으로 끊어서 print

for one in news2:#news2에 글자들을 하나씩 가져와바
    print(one)
print('-----------------------------------------')
print('-----------------------------------------')

count = 0
ju_list = []
for i in range(0, len(news2), 1):  #for(int i=0;i<10;i++)랑 비슷한 의미. 인덱스가 필요하면 위에꺼 말고 아래꺼 써야한다.
    #print(news2[i])
    if(news2[i].startswith('볼스')):#startwith 사용하면 원하는 글자로 시작하는 줄 다 찾음.
        # ==를 사용하려면..news2[i] =='받았으나' 이런식으로 해당 줄에 있는 문장 다 써야함
        print('찾음!>> ',i)
        ju_list.append(i)
        count += 1

print('최종 볼스 개수는', count)
print('최종 볼스 위치는', ju_list)




















