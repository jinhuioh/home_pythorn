# member.txt에 member정보를 3명 넣으세요
# file2.py에서 member.txt를 읽어온 후
# 다음과 같이 출력되도록 해보세요
# 이름   나이      연락처
# -------------------
# jin    22      01046935721
try:
    file = open('member.txt', 'r')
    lines = file.readlines()
    print('이름\t나이\t연락처')
    print('-----------------------')
    # for _ in range(len(lines)):
    for line in lines:
        one =line.split(',')
        print(one[0].strip()+'\t'+#strip하면 글자 양쪽 공백 사라짐.
              one[1].strip()+'\t'+
              one[2].strip()
              )

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
