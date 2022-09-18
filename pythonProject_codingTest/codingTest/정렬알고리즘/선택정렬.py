# 주어진 리스트안의 숫자를 오름차순으로 정렬해보자.
array = [7,5,9,0,3,1,2,4,8]
# 각 숫자를 비교하여 자리를 바꿔주자

for i in range(len(array)):
    #i번째까지 오름차순으로 정렬했으므로 i+1부터 마지막까지의 숫자만 for문을 돌려 앞 수보다 작은지 큰지 판별한다.
    for j in range(i+1,len(array)):
        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i]

print(array)



for i in range(len(array)):
    min_index = i#가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):#0번째 인덱스를 제외하고 0번째와 나머지 인덱스를 비교하여 그 다음 큰 수를 찾기
        if array[min_index] > array[j]:
            # 그 다음 작은 원소를 min_index에 넣어준다.
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]#스와이프
print(array)