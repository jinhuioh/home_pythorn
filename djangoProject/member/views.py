from django.http import HttpResponse
from django.shortcuts import render

# member 메뉴와 관련된 컨트롤러 역할.
# urls.py에 요청된 주소별로 함수가 지정되어있어야함.
# 요청된 주소 하나당 함수 하나!
# 요청된 주소에 따른 함수를 views.py를 정의
def index(request):#request라는 내장 객체를 넣어줘야함.
    print('홈페이지 시작화면입니다.')
    #리턴을 해주어 브라우저에서 출력해보자.
    # return HttpResponse('내가 시작하는 첫 페이지..')
    return render(request, 'index/index.html')

def start(request):#request라는 내장 객체를 넣어줘야함.
    print('시작페이지 호출 됨')
    #리턴을 해주어 브라우저에서 출력해보자.
    return HttpResponse('내가 리턴되는 내용임.')

def index1(request):#request라는 내장 객체를 넣어줘야함.
    print('홈페이지 시작화면입니다.')
    #리턴을 해주어 브라우저에서 출력해보자.
    # return HttpResponse('내가 시작하는 첫 페이지..')
    return HttpResponse(
        "<body bgcolor=blue>" +
        "<h3>index1페이지입니다.</h3><hr color=red>"+
        #href=member/이렇게 쓰면 해당 위치에서 member을 찾기때문에
        #절대적인 경로/member/를 써줘야한다.
        "<a href=/member/>start page로</a><br>"+
        "<a href=/admin/>admin page로</a><br>"+
        "<a href=/member/index2>index2 page로</a><br>"
        "<a href=/>첫페이지 page로</a><br>"
        "</body>"
    )

def index2(request):#request라는 내장 객체를 넣어줘야함.
    print('홈페이지 시작화면입니다.')
    #리턴을 해주어 브라우저에서 출력해보자.
    # return HttpResponse('내가 시작하는 첫 페이지..')
    return HttpResponse(
        "<body bgcolor=pink>" +
        "<h3>index2페이지입니다</h3><hr color=red>"+
        "<a href=/member/>start page로</a><br>"+
        "<a href=/admin/>admin page로</a><br>"
        "</body>"
    )

def index3(request):#request라는 내장 객체를 넣어줘야함.
    #리턴을 해주어 브라우저에서 출력해보자.
    return render(request, 'member1/index3.html')