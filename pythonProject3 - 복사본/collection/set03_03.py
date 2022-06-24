#1학기 점수
title = ['영어','수학','국어','컴퓨터']
term1 = [100, 99, 88 ,77]
#2학기 점수는 1학기와 거의 동일
#국어점수만 66점으로 되었다.
term2 = term1.copy()#copy를 이용해 깊은복사를 해야 term2를 바꿀 때, term1이 바뀌지 않는다.
term2[2] = 66
print(term2)

#1학기보다 성적이 떨어진 과목은?
for i in range(len(term1)):
    if term1[i] > term2[i]:
        print('점수가 떨어진 과목은~: ', title[i])
        print(i)#i는 인덱스
    if term1[i] == term2[i]:
        print('점수가 같은 과목은~: ', title[i])
        print(i)


#1,2학기 점수가 동일한 과목은?
