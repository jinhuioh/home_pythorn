# 문제
# 예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.
# 
# 크로아티아 알파벳	변경
# č	c=
# ć	c-
# dž	dz=
# đ	d-
# lj	lj
# nj	nj
# š	s=
# ž	z=

# 예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다.
# 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
# 
# dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 
# 위 목록에 없는 알파벳은 한 글자씩 센다.
# 
# 입력
# 첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.
# 
# 단어는 크로아티아 알파벳으로 이루어져 있다. 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.
# 
# 출력
# 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
# 
# 예제 입력 1 
# ljes=njak
# 예제 출력 1 
# 6
# 8:40
alp = input()
count = 0
croa = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in croa:
    if i in alp:
        print('alp.count(i)',i,'를 카운트',alp.count(i))
        count += alp.count(i)
        alp = alp.replace(i," ")
        print('문자 삭제',i,alp)
        print('count',count)
    else:
        pass
for i in alp:
    if i == " ":
        # 공백인 경우 continue
        continue
    else:
        count += alp.count(i)
        alp = alp.replace(i," ")
        print('알파벳만 ',i,'해당 알파벳 카운트',alp,'전체카운트',count)
print(count)


alp = input()
count = 0
croa = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in croa:
    if i in alp:
        count += alp.count(i)
        alp = alp.replace(i," ")
    else:
        pass
for i in alp:
    # 공백인 경우 continue
    if i == " ":
        continue
    else:
        count += alp.count(i)
        alp = alp.replace(i," ")
print(count)


# str = input()
# ans = 0
#
# croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
#
# for i in croatia:
#     ans += str.count(i)
#     str = str.replace(i, "")
#
#
# ans += len(str)
# print(ans)
#
#
