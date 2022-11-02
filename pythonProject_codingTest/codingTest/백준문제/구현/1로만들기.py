# # 문제
# # 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
# #
# # X가 3으로 나누어 떨어지면, 3으로 나눈다.
# # X가 2로 나누어 떨어지면, 2로 나눈다.
# # 1을 뺀다.
# # 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
# #
# # 입력
# # 첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.
# #
# # 출력
# # 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
# 
# 예제 입력 1 
# 2
# 예제 출력 1 
# 1
# 예제 입력 2 
# 10
# 예제 출력 2 
# 3
# 힌트
# 10의 경우에 10 -> 9 -> 3 -> 1 로 3번 만에 만들 수 있다.
n = int(input())
# 연산횟수가 들어갈 리스트
d = [0] * (n+1)

for i in range(2, n+1):#숫자를 한개씩 계산
    # 다음 숫자는 이전숫자에 +1을 한것이므로 연산횟수도 +1
    d[i] = d[i-1] + 1
    # 만약 3으로 나누어진다면
    # 이전값에 +1한 연산횟수와, 3으로 나눈 값에 +1한 연산횟수를 비교
    if i%3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 위에 동일하게 연산
    if i%2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
# n번째 숫자에 대한 값을 출력
print(d[n])
