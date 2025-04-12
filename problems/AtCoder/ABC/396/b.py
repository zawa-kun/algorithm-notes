Q = int(input())
card = [0] * 100
result = []
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        card.append(query[1])
    else:
        result.append(card.pop())

for c in result:
    print(c)
        