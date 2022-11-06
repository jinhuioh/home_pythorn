# line = 'aabbbc'
line = 'wonderful'
def solution(line):
    answer = ''
    line = '*'+line

    for i in range(1,len(line)):
        if line[i]==line[i-1]:
            if answer[-1] == '*':
                continue
            else:
                answer += '*'

        else:
            answer += line[i]
            # print('else',answer)

    return answer

print(solution(line))
