import function.cal.device as cal
# 함수의 반환값이 있을 때만! print(함수 호출!)
print(cal.add(100, 200))
print(cal.minus(100, 200))
print(cal.mul(100, 200))
print(cal.div(100, 200))

#반환값이 있는 경우 변수에 넣어둘 수 있다.
result = cal.add(1000, 200)
print(result)

result2 = cal.add(x = 333, y = 222)
print(result2)

result3 = cal.add(200)#default y = 555
print(result3)
#def add(x, y=555): #=>실행, x, y => 매개변수(파라메터)
#    return x + y
#이렇게 y값을 지정해버렸기 때문에 result3이 잘 실행된다.
