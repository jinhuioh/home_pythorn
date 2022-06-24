#기본형 복사. 변수에 값이 들어가 있기 때문에 대입연산자로도 복사가 잘 된다.
x = 100
y = x
print('기본형복사--------')
print(x)
print(y)
y=200
print(x)
print(y)#y=200으로 업데이트가 잘 되었다.

print('--------')
#얕은 복사, 깊은 복사
#참조형 복사.아래처럼 주소가 들어있는 변수를 복사. 함수를 사용해야한다.!!
jumsu_1 = [10,20,30]#배열의 개수는 4개 10,20,30,jumsu_1
                    #자바는 5개 생성.배열을 만들면  length(3)이 readOnly로 자동생성됨.
jumsu_2 = jumsu_1
print(jumsu_2)
print(jumsu_1)

print('얕은복사--------')
jumsu_2[0] = 99
print(jumsu_2)
print(jumsu_1)#jumsu_1도 99로변경되어버림.
#얕은 복사
# [10,20,30] 1개의 리스트에 변수가 2개 jumsu_1, jumsu_2이므로
#변수 한개의 값을 변경하면 다른 변수의 값도 자동 변경 된다.

print('깊은복사--------')
#깊은복사
#copy()함수를 사용해 복사해보자.
jumsu_3 = jumsu_1.copy()
jumsu_3[0]=55
print(jumsu_1)
print(jumsu_3)