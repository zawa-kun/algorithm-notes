N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
nums = A + B
nums.sort()
# print("nums:", nums)
A_indexes = []

for i, x in enumerate(nums):
    if x in A:
        A_indexes.append(i)
# print("A_indexes:", A_indexes)

# Aの要素が連続しているか確認
for i in range(len(A_indexes)-1):
    # print("i:", A_indexes[i], "i+1", A_indexes[i+1])
    if A_indexes[i+1] - A_indexes[i] == 1:
        print("Yes") # 連続していたらYesを出力。処理終了。
        exit()

print("No")
