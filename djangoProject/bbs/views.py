from django.http import HttpResponse
from django.shortcuts import render

# member 메뉴와 관련된 컨트롤러 역할.
# urls.py에 요청된 주소별로 함수가 지정되어있어야함.
# 요청된 주소 하나당 함수 하나!
# 요청된 주소에 따른 함수를 views.py를 정의
import bbs.models


def start(request):#request라는 내장 객체를 넣어줘야함.
    #리턴을 해주어 브라우저에서 출력해보자.
    return render(request, 'bbs/bbsIndex.html')

def insert(request):#request라는 내장 객체를 넣어줘야함.
    return render(request, 'bbs/insert.html')

def insert2(request):#request라는 내장 객체를 넣어줘야함.
#post방식으로 서버로 전달된 데이터를 받아야한다.
    data=request.POST
    print(data)
    #객체 생성해서 save()호출
    one = bbs.models.Bbs(no=data['no'], title=data['title'],
                         content=data['content'],)
    one.save()
    return HttpResponse('ok~')

def update1(request):#request라는 내장 객체를 넣어줘야함.
    return render(request, 'bbs/update1.html')

def update2(request):#request라는 내장 객체를 넣어줘야함.
#post방식으로 서버로 전달된 데이터를 받아야한다.
    data=request.POST
    print(data)
    #객체 생성해서 save()호출
    one = bbs.models.Bbs
    one.save()
    return HttpResponse('ok~')
# Create your views here.
