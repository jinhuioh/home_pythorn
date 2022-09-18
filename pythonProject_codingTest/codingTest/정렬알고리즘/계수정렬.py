# 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘
# 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능합니다.
# 실행 시간 빠름!!(O+N)

# 각 원소의 길이만큼 0으로 된 리스트를 만들고
# 원소 크기 순서대로 count를 세서 0으로 된 리스트의 크기를 1씩 증가
# 증가한 원소를 순서대로 출력
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2, 3]
one = [0]*(max(array)+1)#0번째 인덱스부터 세므로 +1더 큰 수만큼 0으로 이루어진 리스트를 만든다.

for i in range(len(array)):
    # one에 array[i]번째 수에 해당하는 index를 +1
    one[array[i]] += 1
#        one리스트에 있는 인덱스를 인덱스에 있는 숫자만큼 리스트에 담아주자
array_all = []
for k in range(len(one)):
    for m in range((one[k])):
        array_all.append(k)
print(array_all)
#리스트에 있는 원소들을 str로 변환해준 후 스트링으로 출력
result = ' '.join(str(s) for s in array_all)
print(result)



# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2, 3]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)  # 원소 개수와 동일한 0으로 된 리스트 생성

for i in range(len(array)):
    count[array[i]] += 1  # 각 데이터에 해당하는 인덱스 값 증가
    # print('count ', count)
for i in range(len(count)):
    for j in range(count[i]):  # i번째 인덱스의 원소를 센 수가 2이면 원소2번 프린트
        print(i, end=" ")

