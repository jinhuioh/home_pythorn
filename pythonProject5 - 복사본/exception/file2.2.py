try:
    file = open('member1.txt','r')
    lines = file.readlines()
    print('이름\t나이\t연락처')
    for line in lines:
        # print(line)
        one = line.split(',')# 문자열을 ,로 자르고 출력(,뺀 상태로)
        # one = line.split( )# 공백 기준으로 출력
        print(one[0].strip()+'\t'+one[1].strip()+'\t'+one[2].strip())
except:
    print('오류~~~~~~~~~~~~~~')