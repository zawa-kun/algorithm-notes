# 階乗(iterative version)
def factorial(n: int) -> int:
    factorial_ans = n 
    while n != 1:
        n -= 1
        factorial_ans *= n    
    return factorial_ans

# 階乗（再帰で実装ver)
def fact_recursive(n: int) -> int:
    if (n == 1): return 1
    return n*fact_recursive(n-1)

if __name__ == '__main__':
    x = int(input())
    # xが2の時,2!=2であるため,
    # 出力: 2
    if x == 2: print(2)

    # 2! ~ x! まで計算.
    # x == n!となるnを出力.
    for n in range(2, x-1):
        if x == factorial(n):
            print(n)
            exit()



