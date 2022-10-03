# 문제
# 요세푸스 문제는 다음과 같다.
#
# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다.
# 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
# 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다.
# 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
#
# N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 1,000)
#
# 출력
# 예제와 같이 요세푸스 순열을 출력한다.

# 7 3
# <3, 6, 2, 7, 5, 1, 4>
comb = []# 답을 넣을 리스트
allnum = []# n개의 숫자를 넣을 리스트
n,k = map(int,input().split())
for i in range(1,n+1):
    # 0번째 인덱스는 필요 없으므로 1부터 n까지 생성
    allnum.append(i)
# 1부터 n까지의 값을 담은 allnum리스트의 길이가 0이 될 때까지 실행
while True:
    if len(allnum) == 0:
        break
    for m in range(k-1):#k번째 인덱스의 숫자는 없애야하므로 k-1까지 실행
        #0번째 인덱스 값을 빼서 마지막에 append
        allnum.append(allnum.pop(0))
    # k번째 인덱스의 값은 삭제시키고 comb리스트에 append해준다.    
    comb.append(allnum.pop(0))
comb = ', '.join(str(s) for s in comb)#리스트로 된 comb객체를 문자열로 ,로 구분하여 변경
print('<{}>'.format(comb))# '~~~{}'.format({}안에 입력할 변수) 를 이용하여 '<','>' 사이의 공백을 제거해줌

# 주의할 점!!
# 처음 pop()을 이용하여 문제를 풀때는 allnum.append(allnum.pop(0))을 하고 allnum.pop(0)을 해야
# 첫번째 값을 마지막에 붙이고 첫번째 값을 삭제하는 줄 알았는데,
# allnum.append(allnum.pop(0))를 실행시키면 pop이 실행되어 0번째 인덱스 값을 빼서 allnum 마지막 인덱스에 append해준다는 것을 알았다.
# 따라서 allnum.append(allnum.pop(0))을 하고 allnum.pop(0)을 하면 첫번째 인덱스 값은 꺼내져서 마지막에 붙고 두번째 인덱스를 또 지우는 오류가 발생한다.