def remove_ver(A, B):
    for b in B:
        if b in A:
            A.remove(b)  
    return A


if __name__ == "__main__":
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(*remove_ver(A, B))
