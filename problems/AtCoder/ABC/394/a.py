def beside_2_delete(s: str) -> str:
    beside_2_index = [] # 2以外のインデックスを格納するリスト.

    #2以外の数字のインデックスを取得.
    for i, c in enumerate(s):
        if c != "2":
            beside_2_index.append(i)

    #取得したインデックスを基に数字を削除
    # 削除する数字が無ければ終了.
    if len(beside_2_index) == 0: return s

    #最初の"2以外"削除.
    delete_index = beside_2_index.pop() # 削除するインデックス.
    s = s[:delete_index] + s[delete_index+1:] # スライスで要素を削除.
    delete_index -= 1

    #2番目以降の"2以外"を削除.
    while len(beside_2_index) > 0:
        delete_index = beside_2_index.pop()
        s = s[:delete_index] + s[delete_index+1:] # スライスで要素を削除.
        delete_index -= 1
    
    return s

if __name__ == "__main__":
    s = str(input())
    # s = "20250222"      # テスト用.
    print(beside_2_delete(s))
