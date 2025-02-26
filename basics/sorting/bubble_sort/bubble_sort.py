def bubble_sort(arr) -> None:
    len_arr = len(arr)
    for i in range(len_arr):
        limit = len_arr - i - 1 #　未ソート部分の長さ.
        for j in range(limit):
            if arr[j] > arr[j + 1]: #隣り合う要素を比較.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(arr) # [64, 34, 25, 12, 22, 11, 90]
    print('### After sorting ###')
    sorted_arr = bubble_sort(arr)
    print(sorted_arr) # [34, 25, 12, 22, 11, 64, 90]