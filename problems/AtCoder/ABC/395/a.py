N = int(input())
A = [int(i) for i in input().split()]

for i in range(N-1): #配列外参照しないように,N-1まで.
    #1つでも増加していないものがあったら、即Ｎｏ。終了。
    if A[i] >= A[i+1]:
        print("No")
        exit()

print("Yes")