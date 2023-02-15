import sys
sys.stdin = open('1219_path_finder_input.txt')

for ten in range(10):
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))

    V = len(arr) // 2
    adjM = [[0] * (V + 1) for _ in range(V + 1)]
    adjL = [[] for _ in range(V + 1)]

    for i in range(E):
        v1, v2 = arr[i * 2], arr[i * 2 + 1]
        adjM[v1][v2] = 1
        adjM[v2][v1] = 1

    adjL[v1].append(v2)
    adjL[v2].append(v1)

    print(V)