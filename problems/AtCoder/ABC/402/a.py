S = input()
S_ord = []

for c in S:
    if ord(c) <= 96:
        S_ord.append(c)

# S_ord.sort()
for s in S_ord:
    print(s, end='')