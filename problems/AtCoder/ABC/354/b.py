N = int(input())
SC = [input().split() for _ in range(N)]


users_names = []
for user in SC:
    users_names.append(user[0])
users_names_sorted = sorted(users_names)

id_set = {} # IDを管理するセット
for id, name in enumerate(users_names_sorted):
    id_set[id] = name

# print(id_set)

"""勝敗ジャッジ"""
total_rate = 0
for user in SC:
    total_rate += int(user[1])
# print(total_rate)

winner_id = total_rate % N
print(id_set[winner_id])
