S = input()

A_idx = S.find('A')
Z_idx = S.find('Z')

total = 0
if A_idx < Z_idx:
    for i in range(A_idx, Z_idx):
        total += abs((ord(S[i+1])-ord('A')) - (ord(S[i])-ord('A')))
else:
    # only right ver
    # S = S[A_idx:] + S[:Z_idx+1] 
    # print(S)
    S = S[:A_idx+1]
    S_reversed = ''.join(list(reversed(S)))
    print(S_reversed)
    A_idx = S_reversed.find('A')
    Z_idx = S_reversed.find('Z')
    for i in range(A_idx, Z_idx):
        total += abs((ord(S_reversed[i+1])-ord('A')) - (ord(S_reversed[i])-ord('A')))

print(total)