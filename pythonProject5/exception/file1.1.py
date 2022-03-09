# member.txt에 member정보를 3명 넣으세요
# # file2.2.py에서 member.txt를 읽어온 후
# # 다음과 같이 출력되도록 해보세요
# # 이름   나이      연락처
# # -------------------
# # jin    22      01046935721
try:
    file = open('member1.txt','w')

    for _ in range(2):
        name = input('이름은? ')
        age = input('나이는? ')
        cal = input('연락처는? ')
        data = name+', '+age+', '+cal+'\n'
        file.write(data)

except FileNotFoundError:
    print('파일을 찾을 수 없습니다.')
except IOError:
    print('IOError가 발생')
except:
    print('예상치 못 한 오류가 발생했습니다.')
finally:
    try:
        file.close()
    except:
        print('파을을 처리하는데 문제가 발생')