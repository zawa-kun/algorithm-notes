S = list(input())
len_S = len(S)
T = ["."]*len_S
T[0] = "o"

for i, x in enumerate(S):
    
    if x == "#":
        T[i] = "#"
        if i != len_S-1:
            T[i+1] = "o"

print("".join(T))