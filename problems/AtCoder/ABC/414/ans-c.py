# 指定された基数(base)に基づいてnが回文であるかを判定
def is_palindrome_base_A(n: int, base: int) -> bool:
    digits = []
    temp_n = n
    while temp_n > 0:
        digits.append(temp_n % base)
        temp_n //= base
    
    # 回文であるかを判定していく
    left, right = 0, len(digits) - 1
    while left < right:
        if digits[left] != digits[right]:
            return False
        left += 1
        right -= 1
    return True

def solve():
    A = int(input())
    N = int(input())

    total = 0
    for i in range(1, 10):
        if i > N:
            break
        if is_palindrome_base_A(i, A):
            total += i
    
    # 10進数回文を生成
    for x in range(1, 10**7):
        s = str(x)

        """偶数桁の回文生成"""
        rs = s[::-1]
        s_palindrome_even = s + rs
        num_palindrome_even = int(s_palindrome_even)

        if num_palindrome_even > N:
            break

        if is_palindrome_base_A(num_palindrome_even, A):
            total += num_palindrome_even
        
        """奇数桁の回文生成"""
        for mid_digit in range(10): # 中央の桁を0～9まで試す
            s_palindrome_odd = s + str(mid_digit) + rs
            num_palindrome_odd = int(s_palindrome_odd)
        
            if num_palindrome_odd > N:
                break

            if is_palindrome_base_A(num_palindrome_odd, A):
                total += num_palindrome_odd
        
    print(total)

if __name__ == "__main__":
    solve()
