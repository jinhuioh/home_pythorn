# 문제
# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
#
# 입력
# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
#
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
# 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
#
# 출력
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

# 풀기
# 입력할 테스트 케이스의 수 C 객체 생성
# for문을 돌려 학생의 수 N 객체 생성
# 객 줄에 대해 숫자 N개를 입력받고 평균을 구함
# 평균을 넘는 학생수를 count한 후 전체로 나누어줘 비율 측정
# 비율을 반올림하여 소수점 셋째 자리까지 출력 print()

# filter함수를 적용시켜보자.
# filter(function, iterator)
# 첫 번째 매개변수로는 필터링을 적용시킬 함수가 오고두 번째 매개변수로는 반복 가능한 값들이 들어오게 됩니다.
# 출처: https://blockdmask.tistory.com/532

# 입력할 테스트 케이스의 수 C 객체 생성
C = int(input())
list1 = []
for i in range(C):
    # 학생의 수 N 객체 생성
    list1 = map(int, input().split(" "))
    if list1[0] == (range(list1)-1):
        list2 = sum((list1-list[0])/len(list1))
    print(list2)
    # N = int(input())
    # for i in range(N):
    #     n = int(input())
    #     list2 = list1.append(n)
        # 평균 구하기
        # list3 = sum(list2)/len(list2)
