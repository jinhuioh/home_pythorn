n1 = int(input('숫자 입력 '))
n2 = int(input('숫자 입력 '))
x = input('사직연산 입력 ')
if x=='+':
    print(n1+n2)
elif x=='*':
    print(n1*n2)
elif x=='-':
    print(n1-n2)
elif x=='/':
    print(n1/n2)
else :
    print('다른 사칙연산을 골라주세요')

print('--------------------')

name = input('이름을 입력해주세요~ ')
age = input('나이를 입력해주세요~ ')
print(name,'의 나이는', age,'입니다.')

if int(age)>100 :
    print("나이가 많으시군요~")
else:
    print('아직 어리시군요!')

print('--------------------')

hobby = input('어떤 운동을 했나요? ')
time = int(input('몇시간 운동했나요? '))

print(hobby,'를', time,'시간 했습니다.')

if hobby =='달리기' and time>10 :
    print('오늘 달리기는 충분!')
else :
    print('어떤 운동이든 시작하세요!')

print('--------------------')

# 논리형 연산자 and

buy = []
buy.append('옷')
buy.append('핸드폰')
buy.append('빵')
buy.append('화장품')
buy.append('컴퓨터')

for x in buy:
    print('내가 갖고싶은것은~ ',x)

print('--------------------')

for x in[1,2,3,4] :
    print(x)