# WA
N = int(input())
A = [int(i) for i in input().split()]

# 要素が2つの時は必ず等比数列.
if len(A) == 2 : 
    print("Yes")
    exit()

# 最初の二つの数の比を取る.
ratio = A[1] / A[0]
for i in range(1, N-1):
    #最初の二つの比と異なる比が一つでもあれば、等比数列ではない.
    if A[i+1] / A[i] != ratio: 
        print("No")
        exit()

print("Yes")