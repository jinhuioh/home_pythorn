from django.shortcuts import render
import ai.mlPredict
from ML.models import Tag


def index(req):
    return render(req, 'ML/index.html')


def insert(req):
    # 1. 입력한 정보를 받아오자.
    # 2. 받은 데이터를 리스트화 하자.
    data = req.POST
    print('입력한 정보 >> ', data)
    one = Tag(week1=data['week1'], week2=data['week2'], hour=data['hour'],
              gender=data['gender'], age=data['age'], size=data['size'],
              tag_click=data['tag_click'])
    one.save()
    return render(req, 'ML/output.html')


# def output(req, result):
#     return render(req, 'ML/output.html')
