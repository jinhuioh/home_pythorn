# a = input("3개의 숫자 입력")
# b = input("3개의 숫자 입력")
# c = input("3개의 숫자 입력")
#
# def print_max(a,b,c):
#     return max(a,b,c)
# print(max(a,b,c))

# a = list(map(int,input().split()))
# def print_max(a):
#     a = max(a)
#     return a
# a = print_max(a)
# print(a)

#
#
# def print_max():
#     for i in range(3):
#         a = int((input("값입력",i)))
#     a = max(a)
#     return a
#
# print_max()


#
# a = input("숫자 입력")
# b = input("숫자 입력")
# c = input("숫자 입력")
# def print_max(a, b, c) :
#     max_val = 0
#     if a > max_val :
#         max_val = a
#     if b > max_val :
#         max_val = b
#     if c > max_val :
#         max_val = c
#     print(max_val)
# print_max(a, b, c)


#
print("세 정수의 최댓값을 구해봅시다~")
a = input("1번째 수를 입력: ")
b = input("2번째 수를 입력: ")
c = input("3번째 수를 입력: ")
def print_max():
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    print("세 정수의 최댓값은", max, "입니다.")
print_max()

#for문 종류 2가지.
#1. index 이용
fruits = ['apple','banana','pineapple','melon']
for i in range(0,len(fruits)):
    f = fruits[i]
    print(f)

#2. (str)배열자체를 이용
for fruit in fruits:
    print(fruit)


