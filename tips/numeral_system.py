# 10進数 -> 2進数
def convert_to_binary_number(num: int) -> str:
    if num == 0:
        return '0'
    
    binary_number = ''
    while num >= 2:
        binary_number += str(num % 2)
        if num % 2 == 0:
            num //= 2
        else:
            num = (num - num % 2) // 2
    
    binary_number += str(num)
    binary_number = binary_number[::-1]

    return binary_number

if __name__ == '__main__':
    print(convert_to_binary_number(10))