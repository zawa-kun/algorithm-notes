N, M, Q = map(int, input().split())
querys = [list(map(int, input().split())) for _ in range(Q)]

admin_list = [{-1} for _ in range(N+1)]
# print(admin_list)
for query in querys:
    type_query = query[0]
    # クエリの種類で処理を分類
    if type_query == 1:
        admin_list[query[1]].add(query[2])
    elif type_query == 2:
        admin_list[query[1]].add(0) # 0は全ページの権限を持つ
    elif type_query == 3:
        if 0 in admin_list[query[1]] or query[2] in admin_list[query[1]]:
            print("Yes") # 全権限を持つ OR　指定したページの権限を持つ時
        else:
            print("No") 
    