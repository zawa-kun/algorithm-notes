A, B, C = map(int, input().split())

# Yesになるパターン（全４種）
if A + B == C:
    print("Yes")
    exit()
if A + C == B:
    print("Yes")
    exit()
if C + B == A:
    print("Yes")
    exit()
if A == B and B == C:
    print("Yes")
    exit()

print("No")