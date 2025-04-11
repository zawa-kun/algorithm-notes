S = input()
fix = []
for i, s in enumerate(S):
    if i % 2 == 1 and s != 'o':
        fix.append(i)
    elif i % 2 == 0 and s != 'i':
        fix.append(i)

if len(fix) == 0:
    if len(S) % 2 == 0:
        print(0)
        exit()
    else:
        print(1)
        exit()

if len(fix) + len(S) % 2 == 1:
    print(len(fix) + 1)
else:
    print(len(fix))
