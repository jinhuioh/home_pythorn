data_values= [{'title': '다이렉트<b>자동차</b>보험비교 견적사이트 / 특약 내용 정리'},
 {'title': '<b>자동차</b>보험다이렉트비교사이트 살펴보기'}]

titles = []

def del_b(x):
    x = x.replace('<b>','')
    return x

def del_b1(x):
    x = x.replace('</b>','')
    return x
#title 키의 b태그 없애기
for i in range(0, len(data_values), 1):
    mdfy_title = (data_values[i]['title'])
    mdfy_title = del_b(mdfy_title)
    mdfy_title = del_b1(mdfy_title)
    titles.append(mdfy_title)
print(titles)
#파괴함수로 만드는 과정.
# data_values[0]['title'] = data_values[0]['title'].replace('<b>','')
# result = data_values[0]['title'].replace('</b>', '')
# print(result)

#문제:
# 아래 코드는 리스트에 b태그를 제거하여 출력하는 코드이다.
# 아래 코드의 replace('</b>','')를 함수로 모듈화 해보세요.
# data_values= [{'title': '다이렉트<b>자동차</b>보험비교 견적사이트 / 특약 내용 정리'},
#  {'title': '<b>자동차</b>보험다이렉트비교사이트 살펴보기'}]
#
# titles = []
#
# for i in range(0, len(data_values), 1):
#     data_values[i]['title'] = (data_values[i]['title']).replace('<b>','')
#     mdfy_title = (data_values[i]['title']).replace('</b>','')
#     titles.append(mdfy_title)
#
# print(titles)

#
# def func_replace(data_values):
#     for i in range(0, len(data_values), 1):
#         data_values[i]['title'] = (data_values[i]['title']).replace('<b>', '')
#         mdfy_title = (data_values[i]['title']).replace('</b>', '')
#         titles.append(mdfy_title)
#     return titles
#
#
# data_values = [{'title': '다이렉트<b>자동차</b>보험비교 견적사이트 / 특약 내용 정리'}, {'title': '<b>자동차</b>보험다이렉트비교사이트 살펴보기'}]
# titles = []
# titles = func_replace(data_values)
# print(titles)