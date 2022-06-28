from django.contrib import admin
from django.urls import path

import member.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', member.views.start),
    path('member/', member.views.index),
    path('member/insert', member.views.insert),
    path('member/insert2', member.views.insert2),
    path('member/delete', member.views.delete),
    path('member/delete2', member.views.delete2),
    path('member/one', member.views.one),
    path('member/one2', member.views.one2),
    path('member/one22/<id>', member.views.one22),
    path('member/up/<id>', member.views.up),#update문에 id를 get방식으로 넘겨주려먼 "/<id>"를 추가해줘야한다.
    path('member/up2', member.views.up2),
    path('member/all', member.views.all),
    path('member/login', member.views.login),#login처리
    path('member/login2', member.views.login2),#login처리
    path('question/', member.views.qindex),
    path('question/write', member.views.write),#앞주소 question/write는 브라우저상의 주소이다.
    path('question/write2', member.views.write2),#write
    path('question/qdelete', member.views.qdelete),#qdelete
    path('question/qdelete2', member.views.qdelete2),#qdelete
    path('question/qup/<question_writer>', member.views.qup),
    path('question/qup2', member.views.qup2),
    path('question/qone', member.views.qone),
    path('question/qone2', member.views.qone2),
    path('question/qone22/<question_writer>', member.views.qone22),
    path('question/qall', member.views.qall)

]
