from collections import deque


def solve(query, A): 
    if query[0] == 1:                    # クエリ１
        A.append([query[2], query[1]])
    elif query[0] == 2:                  # クエリ２
        # 削除する部分の取り出し
        del_cnt = query[1]  # 削除する値の個数
        total = 0           # 削除した値の合計
        while del_cnt > 0:
            if del_cnt >= A[0][1]:
                del_cnt -= A[0][1]
                total += A[0][0]*A[0][1] 
                A.popleft()
            else:
                A[0][1] -= del_cnt # 個数調整
                total += del_cnt*A[0][0]
                del_cnt = 0
        
        print(total)
                
                

            
            

if __name__ == "__main__":
    Q = int(input())
    querys = []
    for _ in range(Q):
        querys.append(list(map(int, input().split())))
    A = deque() # A[i]　: [値、連続している個数]で格納
    for query in querys:
        solve(query, A)