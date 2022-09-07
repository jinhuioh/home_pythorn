## 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다.
# 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에,
# 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
# 예룰 둘어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.

# 20분
# 입력조건: 첫째 줄에 하나의 문자열 S가 주어집니다.(1<=S의 길이<=10000)
# 출력조건: 첫째 줄에 문제에서 요구하는 정답 출력.

s = list(input())
print(s)
num_plus = 0
st_list = []
# K1KA5CB7
for s_one in s:
    if s_one.isalpha():
        st_list.append(s_one)
        print('s',s)
        print('stlist',st_list)
    else:
        num_plus = num_plus + int(s_one)
print('stlist',st_list)
# 오름차순으로 정렬
st_list.sort()#정렬
st_list.append(str(num_plus))#숫자 합 append
# Join함수는 리스트로 되어 있는 문자열 데이터들을 설정한 구분자(separator)로 구분하여 문자열 형태로 반환하는 내장 함수이다.
# 따라서 리스트안에 int값이 있는경우(문자열 외에 값) 오류가 발생한다!
print(''.join(st_list))#join을 쓸 경우 str과 int가 리스트 안에 같이 있으면 사용 불가하다.