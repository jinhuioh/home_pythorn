import sys

import argparse
from tkinter import messagebox

import requests #알트+엔터(cmd+1)
from collections import Counter
from PIL import  Image, ImageDraw, ImageFont
from io import BytesIO

#kakao연결 + 신청해놨던 키.
API_URL = 'https://dapi.kakao.com/v2/vision/multitag/generate'
MYAPP_KEY = 'e6159dd670c238e3c722998d129c9375'

# get:내가 사이트에 입력한 값이 주소에 붙어서 같이감.(노출이 됨).주소로(header부분에 붙어서) 전달되는 값이 따라감.
#post: 로그인할 때,이미지 데이터 등 입력값이 노출되면 안되는 것들은 body부분에 붙어서 감.
def multi_tag(image_url):
    header = {'Authorization':'KakaoAK %s' % MYAPP_KEY}#제이슨으로 만들어주면 됨.{}가 제이슨
    img_data = {'image_url': image_url}
    response = requests.post(API_URL, headers=header, data=img_data)#get과 post방식 차이는
    # print('http응답', response)
    json_result = response.json()#json을 써줘야 스트링 값(response)을 key,value형태로 구분해 컴퓨터가 인식할 수 있다.
    # print(json_result)
    result = json_result['result']
    # print(result)
    label_kr = result['label_kr']#json_result에서 label_kr key의 value를 꺼내온다.
    print(label_kr)
    return label_kr#리스트 리턴
    # ['사람', '여러사람', '여성', '남성', '바지']
    # ['사람', '여러사람', '실내']
    # ['사람', '여러사람', '남성', '바지']

if __name__ == '__main__':#여러이미지넣기
    img_list = [('https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjAyMTFfMTM3%2FMDAxNjQ0NTQxMzUzMzEy.ihz9DF1aDBi7OvqsxMWjTvwAfD5sgymT2d0kT9BKFzUg.U70Z8i2BTJeHBjz5n4wXNEadE8Z0hkrnDLny718ybyYg.JPEG.ameliepink%2FIMG_9694.jpg&type=a340')
                ,'https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F311%2F2021%2F12%2F13%2F0001384541_001_20211213071101419.jpg&type=l340_165'
                ,'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA1MzFfMjA4%2FMDAxNjIyNDM3NzI3NTcx.gvsHEFKlgxzzxs-w08lvtCYuq9HjAqYHbhaVS7RNPAAg.aRLlptmGZlLysw2OOlkxLNQ7_hsRBfIE7Ftw1MV2qPog.JPEG.quswjddk625%2F2021%25A3%25AD05%25A3%25AD31%25A3%25AD12%25A3%25AD37%25A3%25AD48.jpg&type=l340_165'
                ]

    result_list = []
    for img in img_list:
        label_result = multi_tag(img)
        result_list +=label_result#3개의 리스트를 하나로 뭉쳐
    print(result_list)#서 프린트!

    count_result = Counter(result_list)
    print(count_result.get('여러사람'))#딕셔너리에서 여러사람이 몇 번 나왔는지 get을 이용해 가져오기
    print(count_result.most_common(4))#1~4등까지 많이 나온 단어 가져오기 (most_common)
    #[('사람', 3), ('여러사람', 3), ('남성', 2), ('바지', 2)]. 튜플로 묶여서 나옴.
    order_4 = count_result.most_common(4)
    print('튜플을 분리! >> ',order_4[0])
    order_1 = order_4[0]
    print('제일 빈도수가 높은 단어는~~ ',order_1[0],
          '빈도수는>> ',order_1[1],)

    tour = ''
    if order_1[0] == '사람':
        tour = '제주도'
    elif order_1[0] == '남성':
        tour = '등산'
    else:
        tour = '놀이공원'
    messagebox.showinfo('추천','당신에게'+
                        tour+'를 추천합니다.')