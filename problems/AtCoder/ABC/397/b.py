S = input()

original_length = len(S)
i = 0
while i != len(S):
    if i % 2 == 0: # 偶数番目
        if S[i] == 'o':
            S = S[:i] + 'i' + S[i:]
            i += 1

    else: # 奇数番目
        if S[i] == 'i':
            S = S[:i] + 'o' + S[i:]
            i += 1
    i += 1

if len(S) % 2 == 1:
    S += 'o'
print(len(S) - original_length)