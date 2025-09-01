from collections import deque

N = int(input())
S = list(input())

A_idxs = deque()
B_idxs = deque()

for i, x in enumerate(S):
    if x == "A":
        A_idxs.append(i)
    elif x == "B":
        B_idxs.append(i)

prev = A_idxs.popleft()
p
