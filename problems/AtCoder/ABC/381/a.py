N = int(input())
S = [str(c) for c in input()]

if N % 2 == 0:
    print("No")
    exit()

middle = (N+1)//2
# if S[middle-1] != '/':
#     print("No")
#     exit()

# check 1
for i in range(middle-1):
    # print(S[i]) # debug
    if S[i] != "1":
        print("No")
        exit()

# check 2
for i in range(middle,N):
    # print(S[i]) # debug
    if S[i] != "2":
        print("No")
        exit()

print("Yes")

# # 偶数の場合は11/22になり得ない.
# # 出力：No
# if N % 2 == 0:
#     print("No")
#     exit()

# if N == 1:
#     print("Yes")
#     exit()

# if S.count("/") != 1:
#     print("No")

# middle = (N+1)//2 - 1
# left = set(S[:middle])
# right = set(S[middle+1:])
# # print(left,right)

# if len(left) == 1 and len(right) == 1 and "1" in left and "2" in right:
#     print("Yes")
# else:
#     print("No")