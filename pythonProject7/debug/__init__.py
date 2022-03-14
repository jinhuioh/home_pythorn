# print("jinhui를 넣으면",bool('jinhui'))
# print("''을 넣으면", bool(''))
# print("공백을 넣으면",bool( ))
# print("아무것도 안 넣으면",bool())
# print("1 을 넣으면",bool(1))
# print("0 을 넣으면",bool(0))
# print("None 을 넣으면",bool(None))
# print("[] 을 넣으면",bool([]))
# print("[1,2,'banana'] 을 넣으면",bool([1,2,"banana"]))
# print("{} 을 넣으면",bool({}))

a=1
def vartest(b):
    b = b + 1
    return b

a = vartest(a)#a가 vartest함수의 결괏값으로 바뀐다.
print(a)#2가 나온다.

