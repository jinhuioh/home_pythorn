n,m,k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()# 입력받은 수 정렬
first = data[n-1]#가장 큰 수
second = data[n-2]#두번째로 큰 수
result = 0

while True:
    for i in range(k):
        if m ==0:
            break
        result += first#큰 수 k번 더하기
        m -= 1
    if m==0:
        break
    result += second
    m -= 1
print(result)