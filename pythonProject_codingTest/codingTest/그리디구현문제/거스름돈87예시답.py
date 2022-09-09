# 이거 좀 이상함...다시 봐야할듯? 책
N = 1260
count = 0
# 큰 단위 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += N #count = count+N

    N %= coin # N = N%coin 퍼센트는 나머지
print(count)