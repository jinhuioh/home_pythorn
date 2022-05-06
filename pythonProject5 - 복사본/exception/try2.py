print('1. 여기가 시작입니다.')
try:
    result = 3/0#에러발생!
    #3번째 줄 아래부터는 실행이 되지 않고,
    #실행이 멈추어버림
    print(result)
# except:
#     print('예외처리 하였음!')

except ZeroDivisionError:
    result = 3/3# result = 3/0를 바꿈
    print(result)
    print('예외처리 하였음!')

print('2. 여기가 중간입니다.')
print('3. 여기가 끝입니다.')