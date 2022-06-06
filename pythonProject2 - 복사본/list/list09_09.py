#시작과 끝 값을 입력받아 두 수 사이에 있는 값들의 길이(차이)를 계산
#각 사이 수들의 합과 평균을 구해보자
first,end = input('2개의 수를 입력해보세요! ').split(',')
#각 수들의 합구하기! for문을 돌려서 합해주자
first2 = int(first)#input은 str이므로 꼭!!int값으로 바꿔줘야하낟.
end2 = int(end)
sum = 0
for x in range(first2, end2+1):
    sum +=x
print('사이수들의 합은 %d' % sum)
print('두 수 차이는 %d' % (end2 - first2))
print('평균은 %0.1f' % (sum/len(range(first2, end2+1))))
