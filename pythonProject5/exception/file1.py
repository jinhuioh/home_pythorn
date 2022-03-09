# member.txt에 member정보를 3명 넣으세요
# # file2.py에서 member.txt를 읽어온 후
# # 다음과 같이 출력되도록 해보세요
# # 이름   나이      연락처
# # -------------------
# # jin    22      01046935721

try:
    file = open('member.txt', 'w')  # 포문을 돌리면member.txt 자동생성!! a:어팬드 w:실행될때마다 기존에 있던 내용 없앰.

    for _ in range(3):
        name = input('당신의 이름은 ')
        age = input('당신의 나이는 ')
        tel = input('당신의 연락처는')
        data = name + "," + age + "," + tel + "\n"
        one = data.split(', ')
        file.write(data)
        print('--------------------------')
except FileNotFoundError:
    print('해당파일을 찾을 수 없음')
except IOError:
    print('읽고쓰는데 문제가 생김')
except:
    print('파일을 처리하는데 문제가 생김')
finally:
    try:
        file.close()
    except:
        print('파일을 closing하는데 문제가 생김')
