# n = int(input('나이?'))
# def input_age(n):
#     if 0 <= n <= 120:
#         return n
#     else:
#         return -1
#
# if input_age(n) == -1:
#     print('나이를 판별할 수 없습니다.')
# else:
#     print(f'당신의 나이는 {n}입니다.')

a,b,c = input('세자리수입력:')
# n = int(input('한자리정수 입력:'))
def read_single_digit(n):
    if n == 1:
        return '일'
    elif n == 2:
        return  '이'
    elif n == 3:
        return  '삼'
    elif n == 4:
        return  '사'
    elif n == 5:
        return  '오'
    elif n == 6:
        return  '육'
    elif n == 7:
        return  '칠'
    elif n == 8:
        return  '팔'
    elif n == 9:
        return  '구'
    elif n == 0:
        return  '영'
    else:
        return False

# print(read_single_digit(n))

def read_number(a,b,c):
    print(read_single_digit(int(a)), read_single_digit(int(b)), read_single_digit(int(c)))

read_number(a,b,c)