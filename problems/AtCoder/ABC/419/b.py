class Hukuro:
    def __init__(self):
        self.nums = []

    def solution(self, query_type, x = None) :    # x : qurey_typeが1であるときしか使わないため、デフォルト（－１）を設定
        if query_type == 1:
            self.nums.append(x)
            self.nums.sort(reverse=True) # popで取り出しても遅くならないように降順ソート
            return

        elif query_type == 2:
            if len(self.nums) == 0:
                return
            
            print(self.nums.pop())
            return


if __name__ == "__main__":
    Q = int(input())
    bag = Hukuro()
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            bag.solution(query[0], query[1])
        else:
            bag.solution(query[0])