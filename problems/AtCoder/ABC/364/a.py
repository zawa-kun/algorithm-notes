N = int(input())
flag = False
dishes = [str()] * N

for i in range(N):
    dishes[i] = str(input())

for i in range(N-2):
    if dishes[i] == "sweet" and dishes[i] == dishes[i+1]:
        flag = True
        break

if flag:
    print("No")
else:
    print("Yes")
