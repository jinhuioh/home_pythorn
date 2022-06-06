#for문 종류 2가지.


#for문 종류 2가지.
#1. index 이용
fruits = ['apple','banana','pineapple','melon']
for i in range(0,len(fruits)):
    f = fruits[i]
    print(f)

#2. (str)배열자체를 이용
for fruit in fruits:
    print(fruit)


#스플릿 사용하기.
#1. index 이용
fruits = [['app,le','ba,nana','pineapple','melon'],['12','213']]
# for i in range(0,len(fruits)):
#     f = fruits[i].split(',')
#     f2 = fruits[2]#문자열
#     print(f2)
#     print(f)

# 2. (str)배열자체를 이용
# for fruit in fruits: