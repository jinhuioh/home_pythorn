# def intro(name):
#     print('hellow my name is %s' %name)
#     intro('jini')
# intro('jini')#재귀함수

#일반적인 함수
x =1
y=2
def add(a,b):
    return a+b
print(add(x,y))#3

#입력값이 없는 함수
def say():
    return 'hi~~~!'#hi~~~!
a=say()
print(a)

#결과값이 없는 함수
def add1(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))#3, 4의 합은 7입니다.
a = add1(3, 4)
print(a)#결과값으로 None을 돌려준다.

#입력값도 결과값도 없는 함수
def say1():
    print('hi')#hi
say1()
