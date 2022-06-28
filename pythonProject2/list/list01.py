food = []#ArrayList = new arrayList랑 같은거.
#food[0] = '커피'  <=food에 인덱스가 없으므로 [] 0을 넣으면 오류남
food.append('커피')
food[0] = '라떼'
food.append('라면')
food.append('짜장면')
print(len(food))
food[2] = '짬뽕'
print(food)
# del food[1]
# print(food)
# food.remove('라떼')
# print(food)

food.reverse()
print(food)

# del food[len(food) -1]
# food.pop()#pop:마지막에 넣은 값 빼버리기.
# print(food)
#
# food.pop()
# print(food)

for x in food: #for ~ in :하나씩 값을 꺼내오기
    print(x, end=' ')

print()
for i in range(len(food)):
    print(food[i], end=' ')