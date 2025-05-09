from typing import List
def get_midpoint(coordinate:List[int]) -> List[int]:
    midpoint = [0] * 3
    for i in range(3):
        midpoint[i] = (coordinate[i] + coordinate[i+3]) / 2
    return midpoint




if __name__ == "__main__":
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(get_midpoint(A))
    print(get_midpoint(B))

    
