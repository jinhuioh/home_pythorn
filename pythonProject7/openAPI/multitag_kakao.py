import sys

import argparse
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
    print('http응답', response)
    json_result = response.json()#json을 써줘야 스트링 값(response)을 key,value형태로 구분해 컴퓨터가 인식할 수 있다.
    print(json_result)
    result = json_result['result']
    print(result)
    label_kr = result['label_kr']#json_result에서 label_kr key의 value를 꺼내온다.
    print(label_kr)

if __name__ == '__main__':
    multi_tag('https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjAyMTFfMTM3%2FMDAxNjQ0NTQxMzUzMzEy.ihz9DF1aDBi7OvqsxMWjTvwAfD5sgymT2d0kT9BKFzUg.U70Z8i2BTJeHBjz5n4wXNEadE8Z0hkrnDLny718ybyYg.JPEG.ameliepink%2FIMG_9694.jpg&type=a340')
