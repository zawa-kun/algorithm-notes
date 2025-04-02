S = input()
T = input()

len_search = min(len(S), len(T))
for i in range(len_search):
    if S[i] != T[i]:
        print(i+1)
        exit()


if len(S) != len(T):
    print(len_search+1)
    exit()

print(0)