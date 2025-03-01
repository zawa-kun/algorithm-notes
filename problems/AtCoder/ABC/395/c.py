def getDuplicateNumbers(a: list[int]) -> list[int]:
    b = a.copy()
    b.sort()
    values = [] #重複のある数字.

    for i in range(len(b)):
        if b.count(b[i]) >= 2:
            values.append(b[i])
    
    return set(values)

if __name__ == '__main__':
    N = int(input())
    a = [int(i) for i in input().split()]

    duplicates = getDuplicateNumbers(a) #重複している要素.
    #重複している要素が無ければ終了.
    if len(duplicates) == 0:
        print(-1)
        exit()

    minimum = len(a)
    # 重複している数字のインデックスを取得し、その差から最短の要素数を探す.
    for duplicate in duplicates: #重複している要素を１つ１つ見ていく.
        indexes = [i for i, num in enumerate(a) if num == duplicate]
        
        # 最小要素の更新.
        if minimum > indexes[-1] - indexes[0] + 1:
            minimum = indexes[-1] - indexes[0] + 1 #最短距離の計算.     

    print(minimum)