# 주어진 리스트안의 숫자를 오름차순으로 정렬해보자.
array = [7,5,9,0,3,1,2,4,8]
for i in range(len(array)):
    min_index = i#가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):#0번째 인덱스를 제외하고 0번째와 나머지 인덱스를 비교하여 그 다음 큰 수를 찾기
        if array[min_index] > array[j]:
            # 그 다음 작은 원소를 min_index에 넣어준다.
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]#스와이프
print(array)