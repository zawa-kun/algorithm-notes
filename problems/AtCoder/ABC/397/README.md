# C

数列を2分割し、各部分の種類数を最大にしたい。

### WA
```Python
max = 0
right_set = {}
left_set = {}
for i in range(N):
    sum = len(set(A[:i])) + len(set(A[i:]))
    if max < sum:
        max = sum

print(max)
```


### 解説