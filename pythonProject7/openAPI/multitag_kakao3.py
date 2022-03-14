import sys  # 파이썬 인터프리터가 제공하는 시스템 특화된 함수나 변수를 제공해줌.
import argparse  # api 수정이 필요한 기능을 지원한다.
from tkinter import messagebox
import requests  # 알트+엔터(cmd+1)
from collections import Counter  # 순위 매길때 쓸거.

# kakao연결 + 신청해놨던 키.
API_URL = 'https://dapi.kakao.com/v2/vision/multitag/generate'
MAPPER_KEY = 'a4ea34842d567247008295eb355add44'


def multi_tag(image_url):
    header = {'Authorization': 'KakaoAK %s' % MAPPER_KEY}  # 포멧팅
    img_data = {'image_url': image_url}
    response = requests.post(API_URL, headers=header, data=img_data)
    # print(response)

    json_result = response.json()
    print(json_result)
    result = json_result['result']
    print('result는>>> ', result)
    label_kr = result['label_kr']
    print('label_kr는>>>> ', label_kr)
    return label_kr  # 리스트
    # ['사람', '여러사람']
    # ['사람', '여러사람', '남성']
    # ['사람', '여러사람', '남성']

    # get은 text를 보낼 때 값이 주소에(header에) 따라붙어 있음
    # //post는 로그인할때 아이디 패스워드 노출 안되도록 주소에 따라갈 수 없게 함(body에 붙음


if __name__ == '__main__':
    img_list = [
        'https://th.bing.com/th/id/R.0eb3b7cfab6de87c18f86f9135a701d9?rik=3jfD9bjujQ2xuw&riu=http%3a%2f%2fimg.ezmember.co.kr%2fcache%2fboard%2f2020%2f12%2f22%2fa3a76cf6c8a895a2a7b5743b2cdd1b38.jpg&ehk=YC3fXOK8KE5o3CFrLpc9IbpmWg5U%2fltOCioGcnzcPnw%3d&risl=&pid=ImgRaw&r=0'
        , 'https://file.mk.co.kr/meet/neds/2020/04/image_readtop_2020_430099_15877714854176921.jpg'
        , 'https://newsimg.hankookilbo.com/cms/articlerelease/2017/01/24/201701241967044909_1.jpg'
        , 'https://th.bing.com/th/id/OIP.OoK5lgd-u03ap7P_NOkjQwHaHa?pid=ImgDet&w=600&h=600&rs=1'
        , 'https://th.bing.com/th/id/OIP.OoK5lgd-u03ap7P_NOkjQwHaHa?pid=ImgDet&w=600&h=600&rs=1'
        ,
        'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20130307_122%2Flee_hong1_1362641107335AqRvr_JPEG%2F1%25B9%25DA.jpg&type=a340'
        ,
        'https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F5353%2F2021%2F10%2F21%2F0000780312_001_20211021133202444.jpg&type=a340'
        ,
        'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjAyMTRfMTQy%2FMDAxNjQ0NzcyODA2NTIy.n812ij7qeNjRplvcaRMdk7hHyAGb9dWDYN_FWsYI0wsg.ebWyMejI9gkzjQGv3uui8X2hXYF0iggpeiQxgVH_CbQg.JPEG.quswjddk625%2FVideoCapture%25A3%25DF20220214%25A3%25AD011748.jpg&type=l340_165'
        ,
        'https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F111%2F2017%2F03%2F03%2F1488509306487_1_114946_99_20170303133303.jpg&type=a340'
        ,
        'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxNzAzMjZfOTkg%2FMDAxNDkwNTE0MzYxNTUw.BASFdatZXdK5s2PXe6uaaJQMp9rtCaHyUVYXwHAAilAg.PxWMrYung8nuGxP7ujX-Dq-eKQcC3WVD2QsseatB09Qg.PNG.youngahs74%2Fnoname101.png&type=a340'
        ,'https://i.ytimg.com/vi/eUG-YshYozo/maxresdefault.jpg'
        ,'https://www.bing.com/images/blob?bcid=S.Sv2BAjBO0DqxcxoNWLuD9SqbotqVTdP7g'
        ,'https://image.chosun.com/sitedata/image/201902/10/2019021001722_0.jpg'
        ,'https://th.bing.com/th/id/OIP.LVEffhzLh-cUypWBvLo1DwHaE8?pid=ImgDet&rs=1'
        ,'https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F109%2F2022%2F03%2F13%2F0004571683_001_20220313232603665.png&type=a340'
        ,'https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F5415%2F2022%2F03%2F13%2F0000172793_001_20220313201202829.png&type=a340'
        ,'https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F609%2F2021%2F10%2F04%2F202110031627510010_1_20211004055332761.jpg&type=l340_165'
        ,'https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F5604%2F2019%2F10%2F13%2F0000015063_001_20191013174606042.jpg&type=l340_165'
        ,'https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F052%2F2020%2F06%2F29%2F202006291004117181_d_20200629100704972.jpg&type=a340'
        ,'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA2MjBfMTQ3%2FMDAxNjI0MTI5OTE3NDI3.dxNXqvZGU7QVhH9S8oOhPlQvqIAP7KQDp4-HyT3a_qog.j07MBAUcDuEz547OWgybmuQALN3ThKp9BNTK8zNdG6kg.JPEG.kyongil1228%2Fbandicam_2021-06-20_02-01-54-229.jpg&type=l340_165'
        ]

    result_list = []
    for img in img_list:
        label_result = multi_tag(img)
        result_list += label_result  # 리스트를 하나로 뭉치기!!
    print('리스트를 하나로 뭉치면 >>> ', result_list)

    Count_result = Counter(result_list)
    # print(Count_result)
    # print(Count_result.get('사람')) # 사람 몇 번 나왔는지 세기
    # print(Count_result.most_common(3))
    # [('사람', 3), ('여러사람', 3), ('남성', 2)]
    order_5 = Count_result.most_common(5)  # 5위까지 순위나옴.
    print('튜플을 분리해서 많이 나온 단어 프린트', order_5[0])  # 튜플을 분리해서 1번쩨 많이 나온 단어 프린트
    # print(order_5[2])
    # ('사람', 3)
    order_1 = order_5[0]
    order_2 = order_5[1]
    print('제일 빈도수가 높은 단어는', order_1[0], '빈도수는', order_1[1])
    # print('그 다음으로 빈도수가 높은 단어는', order_1[2], '빈도수는', order_1[3])
    # 제일 빈도수가 높은 단어는 사람 빈도수는 x

    advertise = ''
    if (order_1[0] == '남성' or order_1[0] == '스포츠') and (order_2[0] == '남성' or order_2[0] == '스포츠'):
        advertise = '운동용품 추천'
    elif (order_1[0] == '남성' or order_1[0] == '바지') and (order_2[0] == '남성' or order_2[0] == '바지'):
        advertise = '남성복 추천'
    else:
        advertise = '일반 광고 추천'
        messagebox.showinfo('추천>>', '당신에게' + advertise + '를 추천합니다.')
