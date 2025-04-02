# 高熱：１
# 発熱：２
# 普通：３

X = float(input())

if X >= 38.0:
    print('1')
    exit()
elif X < 37.5:
    print('3')
    exit()
print('2')