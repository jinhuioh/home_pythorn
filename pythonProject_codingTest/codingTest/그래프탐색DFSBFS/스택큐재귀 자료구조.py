# 스택 자료구조
# 선입후출 자료구조로 먼저 들어온 데이터가 나중에 나간다.
# 입구와 출구가 동일한 형태로 스택을 시각화할 수 있다.

# 큐 자료구조
# 선입선출로 먼저 들어온 데이터가 먼저 나가는 형식.
# 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화 할 수 있다. (미로문제)

# 재귀함수
# 자기 자신을 다시 호출하는 함수를 의미
# 재귀함수를 호출하는데 깊이 제한이 있기 때문에 별다른 설정없이 아래 코드를 실행시키면
# 어느 순간 이후에 오류메세지가 뜨는 것을 볼 수 있다.
# def recursive_function():
#     print('재귀함수 호출')
#     recursive_function()
# recursive_function()

def recursive_function(i):
    if i == 100:
        return
    print(i,'번째 재귀함수에서', i+1 ,'재귀함수 호출')
    recursive_function(i+1)
recursive_function(1)

# 1부터 n까지의 곱셈 출력
def du(n):
    if n <= 1:
        return 1
    return n * du(n-1)
print(du(5))

# 최대 공약수 계산(유클리드 호제법)
# 두 자연수 a,b에 대해(a>b) a를 b로 나눈 나머지를 R이라고 하자.
# 이때 a와 b의 최대공약수는 b와 R의 최대공약수와 같다.
def gcd(a,b):
    if a%b ==0:
        return b
    else:
        return gcd(b, a%b)#gcd()를 return하므로 최대공약수가 나올 때까지 재귀적으로 함수를 도는것을 확인할 수 있다.
print(gcd(192,162))

# 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓임.
# 그래서 스택을 사용해야 할 때 구현상 스택 라이브러리 대신에 재귀 함수를 이용하는 경우가 많다.