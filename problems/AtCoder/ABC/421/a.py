N = int(input())
names = []
for _ in range(N):
    names.append(input())

target = input().split()

for i, x in enumerate(names):
    if x == target[1] and i + 1 == int(target[0]):
        print("Yes")
        exit()

print("No")