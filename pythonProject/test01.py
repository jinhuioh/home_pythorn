a=1
def add(b):
    b = b+1
    return b
a=add(a)#add(a)가 2가 되어 a=2가 된다.
print(a)#2가 출력된다.
#
def kw(**kw):
    print(kw)
kw( age = 3, name = 'foo')

# print('-------------------------------------')
# def say(name, man = True, old):
#     print("나의이름은 %s입니다."% name)
#     print("나이는 %d 살입니다."% old)
#     if man:
#         print("man")
#     else:
#         print("여자")
# say("박응용",27)
# say("박응용",27,28)
# say("박응용",True,27)
import sys
args = sys.argv[1:]
for arg in args :
    print(arg)
