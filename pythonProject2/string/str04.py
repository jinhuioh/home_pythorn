#신문기사 카테고리 중 국제 타이틀 10개를 가지고와서
#하나의 String으로 만드세요.
#그 중 '러시아'라는 단어가 몇 번 나오는지 카운트

# news = '''
# 러시아 헬기·전투기, 일본·스웨덴 영공 침범
# 골드만삭스 “서방 제재로 올해 러시아 경제 7% 역성장”
# 러 매체 “우크라이나군, 친러 반군 통제하는 동부 포격”
# 푸틴에 명예박사 수여한 용인대…누리꾼 “전쟁 용인 안돼, 학위 박탈하라”
# ‘개 껴안고 강추위 버텨’ 러시아 소녀, 실종 18시간만에 구조
# 새끼 북극곰 형제가 은인 찾아 수백㎞ 걸은 사연
# 12㎏ 거구 고양이, 개로 오해받는 사연…‘너무 커 안기도 힘들겠네~’
# 러시아서 코로나19·독감 동시 예방 백신 개발 중
# WP 러시아 내년 초 17만5000명 동원해 우크라이나 침공할 수도
# 러시아, 코로나19 급증세 지속…하루 1075명 사망
# '''
# print('러시아 단어 개수', news.count('러시아'))
# news2 = news.split() #띄어쓰기 기준 한 문장씩 끊기(split)
# print(news2) #split으로 str으로 끊어서 print
# print('----------------------------------!!!!-------')
#
# for one in news2:#news2에 글자들을 하나씩 가져와바
#     print(one)
# print('-----------------------------------------')
#
#
# count = 0 #러시아의 개수 찾기.
# ne_list = [] #러시아 글자 위치 채크해보기.
#
# for i in range(0, len(news2), 1) :
#     if(news2[i].startswith('러시아')) :
#         ne_list.append(i)
#         count +=1
#
# print('러시아로 시작하는 str 개수', count)
# print('러시아 글자 위치', ne_list)



news = '''
러시아 헬기·전투기, 일본·스웨덴 영공 침범
골드만삭스 “서방 제재로 올해 러시아 경제 7% 역성장”
러 매체 “우크라이나군, 친러 반군 통제하는 동부 포격”
푸틴에 명예박사 수여한 용인대…누리꾼 “전쟁 용인 안돼, 학위 박탈하라”
‘개 껴안고 강추위 버텨’ 러시아 소녀, 실종 18시간만에 구조
새끼 북극곰 형제가 은인 찾아 수백㎞ 걸은 사연
12㎏ 거구 고양이, 개로 오해받는 사연…‘너무 커 안기도 힘들겠네~’
러시아서 코로나19·독감 동시 예방 백신 개발 중
WP 러시아 내년 초 17만5000명 동원해 우크라이나 침공할 수도
러시아, 코로나19 급증세 지속…하루 1075명 사망
'''
print('러시아 단어 개수', news.count('러시아'))
news2 = news.split() #띄어쓰기 기준 한 문장씩 끊기(split)
print(news2) #split으로 str으로 끊어서 print
print('----------------------------------!!!!-------')
ne_list = [] #러시아 글자 위치 채크해보기.

for i in range(0, len(news2), 1) :
    if(news2[i].startswith('러시아')) :
        ne_list.append(i)
print('러시아가 나온 단어들의 위치는 {0}'.format(ne_list))

war_list=[]
for i in range(0,len(news2),1):
    if(news2[i].startswith('침범')):
        war_list.append(news2[i])
print('러시아로 시작하는 str 개수는 {0}'.format(len(war_list)))
print(war_list)