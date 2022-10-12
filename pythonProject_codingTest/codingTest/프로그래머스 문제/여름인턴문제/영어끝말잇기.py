# 문제 설명
# 1부터 n까지 번호가 붙어있는 n명의 사람이 영어 끝말잇기를 하고 있습니다. 영어 끝말잇기는 다음과 같은 규칙으로 진행됩니다.
#
# 1번부터 번호 순서대로 한 사람씩 차례대로 단어를 말합니다.
# 마지막 사람이 단어를 말한 다음에는 다시 1번부터 시작합니다.
# 앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
# 이전에 등장했던 단어는 사용할 수 없습니다.
# 한 글자인 단어는 인정되지 않습니다. <---이게 의미하는게 건너뛴다는 의미인가?
# 다음은 3명이 끝말잇기를 하는 상황을 나타냅니다.
#
# tank → kick → know → wheel → land → dream → mother → robot → tank
#
# 위 끝말잇기는 다음과 같이 진행됩니다.
#
# 1번 사람이 자신의 첫 번째 차례에 tank를 말합니다.
# 2번 사람이 자신의 첫 번째 차례에 kick을 말합니다.
# 3번 사람이 자신의 첫 번째 차례에 know를 말합니다.
# 1번 사람이 자신의 두 번째 차례에 wheel을 말합니다.
# (계속 진행)
# 끝말잇기를 계속 진행해 나가다 보면, 3번 사람이 자신의 세 번째 차례에 말한 tank 라는 단어는 이전에 등장했던 단어이므로 탈락하게 됩니다.
#
# 사람의 수 n과 사람들이 순서대로 말한 단어 words 가 매개변수로 주어질 때,
# 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지를 구해서 return 하도록 solution 함수를 완성해주세요.
#
# 제한 사항
# 끝말잇기에 참여하는 사람의 수 n은 2 이상 10 이하의 자연수입니다.
# words는 끝말잇기에 사용한 단어들이 순서대로 들어있는 배열이며, 길이는 n 이상 100 이하입니다.
# 단어의 길이는 2 이상 50 이하입니다.
# 모든 단어는 알파벳 소문자로만 이루어져 있습니다.
# 끝말잇기에 사용되는 단어의 뜻(의미)은 신경 쓰지 않으셔도 됩니다.
# 정답은 [ 번호, 차례 ] 형태로 return 해주세요.
# 만약 주어진 단어들로 탈락자가 생기지 않는다면, [0, 0]을 return 해주세요.

# 풀이 순서
# 0. 사람순서 list, 몇바퀴째인지 list, 가장 작은 인덱스의 정답을 출력할 list, 정답들어가는 list 생성
# 1. 단어의 길이가 1일 때, pass
# 2. 이전단어의 마지막 단어와 다음단어의 첫번째 단어가 다를 때
# 3. 같은 단어 말했을 때
# 4. 각 경우에 대해 인덱스를 minList에 append한 후 최소 인덱스 값을 answer에 넣어준다.
# 5. 만약 끝말잇기가 끝이 안난다면 answer=[0,0]을 리턴

#
#
n = 3
# words = ["hello", "one", "even", "never", "now", "world", "draw"]
words =["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
# words = ["hello", "observe","effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]

def solution(n, words):
    answer = []#정답들어가는 list
    people = []#사람순서 list
    index = []#몇바퀴째인지 list
    minList = []#가장 작은 인덱스의 정답을 출력할 list
    kIndex=0
    # 사람순서
    for i in range(n):
        people.append(i+1)
    for i in range(n,len(words)):
        people.append(people[i-n])
    # 인덱스
    k = 0
    for i in range(1, len(words) + 1):
        if i == len(words)+1:
            break
        if i > n and i % n == 1:
            k += 1
        index.append(1 + k)

    #1. 단어의 길이가 1일 때, pass
    for i in range(len(words)):
        if len(words[i])==1:
            minList.append(i)
            break

    #2. 이전단어의 마지막 단어와 다음단어의 첫번째 단어가 다를 때
    for i in range(1, len(words)):
        # print('words[i][0]',i,words[i])
        if words[i][0] != words[i - 1][-1]:
            minList.append(i)
            break

    #3. 같은 단어 말했을 때
    for i in range(len(words)-1):
        wordsI = words[i]
        # print('i와 wordsI',i,wordsI)
        for k in range(i+1,len(words)):
            # print('k i+1,words[k]','k',k,'i',i,words[k])
            if words[k] == wordsI:
                minList.append(k)
                break
    if len(minList) == 0:
        answer = [0,0]
        # return print(answer)
    else:
        minIndex = min(minList)
        # 가장 작은인덱스 어펜드
        answer.append(people[minIndex])
        answer.append(index[minIndex])
        # return print(answer)
    return answer
solution(n,words)