# 순차 탐색: 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
# 이진 탐색: 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
#           시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정한다.

# 이진탐색소스코드로 구현(재귀적 구현)
# 입력조건: 첫번째 줄에 원소의 개수n와 찾고자하는 숫자k를 공백으로 입력받는다.
#          두번째 줄에 원소n개를 입력한다.
# 출력조건: 원소가 위치해있는 인덱스를 출력한다.

# 원소의 개수n와 찾고자하는 숫자target를 공백으로 입력
n, target = map(int, input().split())

# 원소n개를 리스트로 입력받기
array = list(map(int, input().split()))

# 이진 탐색 함수 만들기
# 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정해야하므로 함수안에 총 4가지 객체를 넣어줘야함.
def binary_search(array, target, start, end):
    if start > end:#시작점이 끝점보다 크다면 return None
        return None
#     중간지점 객체 생성
    mid = (start+end)//2
#     mid값이 target과 같다면 return mid
    if array[mid] == target:
        return mid
#     중간값(mid)이 찾으려하는 target보다 작다면 오른쪽 확인. 재귀함수 사용
    if array[mid] < target:
        return binary_search(array, target, mid+1, end)
#      중간값이 찾으려하는 target보다 크다면 왼쪽 확인
    else :
        return binary_search(array, target, start, mid-1)

# 이진탐색 수행결과 출력
result = binary_search(array, target,0, n-1)
if result == None:
    print("찾는원소가 없습니다.")
else:
    print(result+1)#인덱스가0부터 시작하므로 +1을 해주어 1부터 시작하는것으로 바꿔주자.