from django.contrib import admin

# Register your models here.
from member.models import Question, Test

admin.site.register(Question)#임포트:알트+엔터
admin.site.register(Test)