#시작과 끝 값을 입력받아 두 수 사이에 있는 값들의 길이(차이)를 계산
#각 사이 수들의 합과 평균을 구해보자
start, end = input('시작과 끝 값 입력!  ').split(',')
start2 = int(start)
end2 = int(end)

length = len(range(start2,end2+1))
print(length)

sum =0
for x in range(start2,end2+1):
    sum +=x
print('사이 수들의 합은 %d' % sum)
print('평균은~~ %0.1f' % (sum/length))
print('----------------------')

