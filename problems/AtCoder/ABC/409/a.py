N = int(input())
T = input()
A = input()

for i in range(N):
    if T[i] == A[i] and T[i] == "o":
        print("Yes")
        exit()

print("No")