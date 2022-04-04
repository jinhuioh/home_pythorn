import re
s = 'aaa@xxx.com'
m = re.match(r'[a-z]+@[a-z]+.[a-z]+', s)
# 시스템을 돌리셔도 됩니다.
print(type(m))
# a = 'The   quick  brown  fox  jumps   over  the  lazy dog'
# test_a = ''.join(a)
# test_a = re.sub(r'[,\s]+',' ', test_a)
# print(test_a)
