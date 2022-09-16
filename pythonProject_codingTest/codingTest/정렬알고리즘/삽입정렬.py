# 주어진 리스트안의 숫자를 오름차순으로 정렬해보자.
array = [7,5,9,0,3,1,2,4,8]

for i in range(1,len(array)):
    for j in range(i, 0, -1):#인덱스를 i부터0까지 1씩 감소
        if array[j] < array[j-1]:#앞에 인덱스와 비교하여 앞이 더 크면 스와이프
            array[j], array[j-1] = array[j-1], array[j]
        else:#앞 인덱스가 더 작으면 멈추기
            break

print(array)