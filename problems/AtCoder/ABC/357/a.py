N, M = map(int, input().split())
H = list(map(int, input().split()))

cnt = 0
for hands in H:
    M -= hands
    if M >= 0:
        cnt += 1
    else:
        break

print(cnt)