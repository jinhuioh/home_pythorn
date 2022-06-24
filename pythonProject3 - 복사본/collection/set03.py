#1학기 점수
title = ['영어','수학','국어','컴퓨터']
term1 = [100, 99, 88 ,77]
#2학기 점수는 1학기와 거의 동일
#국어점수만 66점으로 되었다.
term2 = term1.copy()
term2[2] = 66
print('1학기 성적은~: ', term1)
print('2학기 성적은~: ', term2)
#1학기보다 성적이 떨어진 과목은?
for i in range(len(term1)):#2개의 list값을 비교하려면 index역할하도록 range len을 사용
    if term1[i] > term2[i]:
        print(title[i])
#1,2학기 점수가 동일한 과목은?
for i in range(len(term1)):#2개의 list값을 비교하려면 index역할하도록 range len을 사용
    if term1[i] == term2[i]:
        print(title[i], end=' ')