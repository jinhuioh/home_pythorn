#debugger: 중지점을 만들어 단계별로 실행하면서 애러를 수정할 수 있다.
# breakpoint:여러번 잡을 수 있다.
#attach한 프로잭트라서 실행시키면 오류남!!! 따로 빼서 해야함.
b = 10
a = b + 1
print(a)
a = 200
b = 30
print(a)

for x in range(3):
    a = 333 + x
    b = 333 + x
    print(a,b)
