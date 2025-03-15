"""
括弧の対応を調べるプログラム
入力："(",")","{",","}","[","]"で構成された文字列.
出力：括弧が対応しているか(Yes/No)
"""
def bracket_checker(s):
    check = [] # 終わり括弧を格納するリスト.
    for i in range(len(s)):
        # 始まり括弧確認
        if s[i] == "(":
            check.append(")")
        elif s[i] == "{":
            check.append("}")
        elif s[i] == "[":
            check.append("]")
        # 閉じ括弧確認.
        # 処理終了の条件
        # ・終わり括弧が出てきたのに、checkに一致する終わり括弧がない.
        # ・終わり括弧が出てきたのに、checkに何もない.
        elif s[i] == ")":
            if len(check) == 0 or ")" not in check: 
                print("No") 
                exit()
            check.remove(")")
        elif s[i] == "}":
            if len(check) == 0 or "}" not in check: 
                print("No")
                exit()
            check.remove("}")
        elif s[i] == "]":
            if len(check) == 0 or "]" not in check:
                print("No")
                exit()
            check.remove("]")

    if len(check) == 0:
        return "Yes"
    else:
        return "No"
    
if __name__ == '__main__':
    test_cases = input()
    print(f"{bracket_checker(test_cases)}")