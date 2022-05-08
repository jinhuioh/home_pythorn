jumsu_1 = {100, 99, 88, 77}
jumsu_2 = {90, 99, 88, 66}

#두 학기 내내 동일한 성적인 점수는? 과목 수는?
#result = jumsu_1 & jumsu_2#집합연산자 사용. intersection과 &와 같음
result =jumsu_1.intersection(jumsu_2)
print(result)
print(len(result))
#두 학기를 비교했을 때 1 학기 성적 중 2학기와 다른 성적은?
result2 = jumsu_1.difference(jumsu_2)
print(result2)
#두 학기 동안 내가 획득한 전체 점수 목록은?
result3 = jumsu_1.union(jumsu_2) #a또는b의미 |:버티컬 바
print(result3)
#정렬하고 싶어요!
result33 = list(result3)#list한 결과, 비파괴형 함수,list로 캐스팅하여 정렬!
#!중요! result3을 list로 바꿔도 원본result3이 바뀐것은 아니다.(비파괴형)
print('result3을 list 로 바꿔도 타입은 set입니다. ',type(result3))
print('------------------------')
result33.sort()#void,파괴형 함수,list로 바꿨으므로 sort라는 함수를 쓸 수 있다.
#!중요! result33을 sort로 바꾸면 원본result33의 type까지 sort로 바꿔진다.(데이터를 바꿔버리는 파괴형 함수)
print('파괴형 함수',result33)
result33.reverse()
print(result33)
print(type(result33))
#1학기 성적에 음악점수 50점 추가
jumsu_1.add(50)
print(jumsu_1)#순서없음. 있게 하려면 list로 바꿔야함
#2학기 성적에 음악 77,컴퓨터 100점 추가
jumsu_2.update({77, 100})#77,100 순서없이 아무곳에서 집어넣음
print(jumsu_2)
#1학기 성적 모두 삭제
jumsu_1.clear()
print(jumsu_1)