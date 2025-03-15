S = input()

# 最後は|であるから,len(S)-1まで.
for i in range(len(S)-1):
    # |が来たら,次の|の-までの-の数を数える.
    if S[i] == "|":
        j = i + 1
        count = 0 # 連続している-の数 
        while S[j] != "|" :
            count += 1
            j += 1
        print(count, end=" ")

