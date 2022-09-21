## 동빈이는 두개의 배열 a,b를 가지고 있다.
# 두 배열은 n개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수
# 동빈이는 최대 k번의 바꿔치기 연산을 수행할 수 있는데, 바꿔치기 연산이란 배열 a에 있는 원소 하나와
# 배열 b에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말한다.
# 동빈이의 최종 목표는 배열 a의 모든 원소의 합이 최대가 되도록 하는 것이다.
# n,k와 배열 a,b가 주어졌을 때, 최대 k번의 바꿔치기 연산을 수행하여 만들 수 있는
# 배열 a의 모든 원소의 합의 최대값을 출력하는 프로그램을 작성하세요
# 입력조건: 첫번째 줄에 n,k가 공백을 기준으로 구분되어 입력됨
# 두번째 줄에 배열 a의 원소들이 공백을 기준으로 구분되어 입력됨 모든 원소는 10,000,000보다 작은 자연수
# 세번째 줄에 배열 b의 원소들이 공백을 기준으로 구분되어 입력됨 모든 원소는 10,000,000보다 작은 자연수
# 출력조건: 최대 k번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 a의 모든 원소의 합이 최대값을 출력합니다.
# ##

n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
print(a)
print(b)
for i in range(k):
    if a[i] < b[i]:
        a[i] = b[i]
        print(a)
print(sum(a))


# n개의 원소와 바꿀 수 있는 수 k를 입력받자
n,k = map(int, input().split())
# n개만큼 배열들을 입력받자
a = list(map(int,input().split()))
b = list(map(int,input().split()))
# k만큼 큰 수부터 차례로 바꿔치기 수행
# a의 가장 작은 수와 b의 가장 큰 수를 바꿔주자
for j in range(k):
    if b[j] == max(b):
        maxB = max(b)
        print('maxB',maxB)
for m in range(k):
    if a[m] == min(a):
        minA = min(a)
        print('minA',minA)
    b[j], a[m] = minA ,maxB
    print(b[j], a[m])
#     바꾼 원소를 덮어씌어주기
print('a', a)
# a배열 원소의 합 출력
print('sum_a', sum(a))


# 예시 답============================================
n,k = map(int, input().split())
# n개만큼 배열들을 입력받자
a = list(map(int,input().split()))
b = list(map(int,input().split()))

# 오름차순 내림차순 정렬
a.sort()
b.sort(reverse=True)
for i in range(k):
    if a[i]< b[i]:
        a[i],b[i] = b[i],a[i]
    else:
        break
print(sum(a))