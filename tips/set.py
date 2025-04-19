s_list = [{1,2}, {3,4}, {1}]

i = 0
while i != len(s_list):
    s_list[i].discard(1)
    print(s_list)
    print(i)
    i += 1
print(s_list)