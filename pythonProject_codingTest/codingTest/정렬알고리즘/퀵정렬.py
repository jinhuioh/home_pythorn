# 짱 빠름(보통 삽입정렬이나 선택정렬은 n^2복잡도라면 퀵은 n*logn 복잡도임
# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꿈

# 피벗 데이터 한개를 정해서(하나의 원소를 정해서) 그 원소를 기준으로 앞으로 한 칸씩 이동하면서
# 피벗보다 큰 데이터가 있는지 확인
# 피벗 데이터 기준 뒤에서 부터(마지막부터) 탐색하면서 피벗보다 작은 값이 있는지 확인
# 위에 말한 두 값의 위치를 변경
# 만약 앞,뒤로 가는 인덱스가 겹치는 경우

# 일반적인 방법
array = [7,5,9,0,3,1,2,4,8]
def quick(array, start, end):
    if start >= end:#원소가 1개인 경우 종료
        return
    pivot = start
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -=1
        if(left > right): #엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:#엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
     # 분할 이후 피벗을 중심으로 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
     # 재귀함수를 이용하여 정렬
    quick(array, start, right-1)#피벗보다 작은 수들을 모아놓은 list
    quick(array, right+1, end)#피벗보다 큰 수를 모아놓은 list
quick(array, 0, len(array)-1)
print(array)

# 간결한 방법
array = [7,5,9,0,3,1,2,4,8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0]#피벗은 첫번째 원소
    tail = array[1:]#피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]#분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]#분할된 왼쪽 부분
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
print(quick_sort(array))