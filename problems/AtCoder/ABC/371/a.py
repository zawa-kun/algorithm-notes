S = input().split()

if S[0] == '<':
    if S[1] == '<':
        if S[2] == '<':
            K = ['A', 'B', 'C']
        else:
            K = ['A', 'C', 'B']
    else:
        K = ['C', 'A', 'B']
else:
    if S[1] == '<':
        K = ['B', 'A', 'C']
    else:
        if S[2] == '<':
            K = ['B', 'C', 'A']
        else:
            K = ['C', 'B', 'A']

print(K[1])