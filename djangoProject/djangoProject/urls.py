"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import bbs.views
import member.views#파일까지 임포트(.views)
#주소하나당 함수 하나
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', member.views.index),
    path('member/', member.views.start),
    path('member/index1', member.views.index1),
    path('member/index2', member.views.index2),
    #member요청이 들어오면 member 아래에 views아래에 start함수를 실행하겠어! 라는 의미이다.
    path('member/index3', member.views.index3),
    path('bbs/', bbs.views.start),#알트+엔터
    path('bbs/insert', bbs.views.insert),#입력화면요청
    path('bbs/insert2', bbs.views.insert2),#요청받는주소
    path('bbs/update1', bbs.views.update1),#업데이트 브라우저에 보여주는 부분
    path('bbs/update2', bbs.views.update2)#업데이트 받은거 호출하여 db처리 구현 부분
]

