from typing import List
def get_midpoint(coordinate:List[int]) -> List[int]:
    midpoint = [0] * 3
    for i in range(3):
        midpoint[i] = (coordinate[i] + coordinate[i+3]) / 2
    return midpoint

def get_distance2(A: List[int], B: List[int]) -> int:
    print(A, B)
    return (A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2 + (A[2] - B[2]) ** 2




if __name__ == "__main__":
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    midpoint_distance2 = get_distance2(get_midpoint(A), get_midpoint(B)) * 8
    half_distance_A_diagonal = get_distance2(A[:3], A[3:])
    half_distance_B_diagonal = get_distance2(B[:3], B[3:])
    print(half_distance_A_diagonal, half_distance_B_diagonal, midpoint_distance2)
    if midpoint_distance2 < half_distance_B_diagonal + half_distance_A_diagonal:
        print("Yes")
    else:
        print("No")