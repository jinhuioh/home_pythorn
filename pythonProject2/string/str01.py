data = '감자고구마양파'
print(len(data))
print(type(data))
#인덱싱,슬라이싱을 해보자!
last = data[6]
print('마지막 글자는 %s %s' % (last, last))
first = data[0]
print('마지막 글자는 %s 첫번째 글자는 %s' % (last, first))
print('마지막 글자는 {l} 첫번째 글자는 {f}'.format(l=last,f=first))
our = (last, first) #tuple(list랑 같다 readOnly)
#포멧팅해보자~
print('마지막 글자는 {o[0]} 첫번째 글자는 {o[1]}'.format(o=our))

print('------------------------------------')

print(data[0:2])#0번부터2번까지 값 가져올때는 2보다 1작은수까지 가져옴
print(data[:2])#첫번째자리 생략가능. 마지막자리도 생략가능
print(data[2:5])
print(data[5:7])
print(data[5:])

print('------------------------------------')

data2 = '생수커피'
data3 = data + data2
print(data3)
