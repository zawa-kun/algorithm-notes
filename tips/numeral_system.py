# 10進数 -> 2進数
def convert_to_binary_number(num: int) -> str:
    if num == 0:
        return '0'
    
    binary_number = ''
    while num >= 2:
        binary_number += str(num % 2)
        num //= 2
    
    binary_number += str(num)
    binary_number = binary_number[::-1]

    return binary_number

# 10進数 -> n進数 (nは1~10)
def convert_to_n_number(num: int, numeral: int) -> str:
    if num == 0:
        return '0'
    
    binary_number = ''
    while num >= numeral:
        binary_number += str(num % numeral) 
        num //= numeral
    
    binary_number += str(num)
    binary_number = binary_number[::-1]

    return binary_number


if __name__ == '__main__':
    print('-----convert_to_binary_number()-----')
    print(convert_to_binary_number(10))
    print('-----convert_to_n_number()-----')
    print(convert_to_n_number(10, 4))
    