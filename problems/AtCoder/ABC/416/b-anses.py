# replaceを使い、コード量を抑えている
# 一度の文字列変換であり、b.pyよりもメモリアロケーションが少ない
# こんな風に簡潔にコード書けるようになりたい
def zepp(S):
    s = S.replace("#.", "#o")
    if s[0] == ".":
        s = "o" + s[1:]
    return s


if __name__ == "__main__":
    S = input()
    print(zepp(S))