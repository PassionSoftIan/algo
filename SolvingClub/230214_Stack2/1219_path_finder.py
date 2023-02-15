import sys
sys.stdin = open('1219_path_finder_input.txt')

def DFS(start):
    stack = [start]
    visited = [0] * (V)
    while stack:
        start = stack.pop()
        visited[start] = 1
        if visited[99] == 1:
            return 1
        for next in range(0, V):
            if G[start][next] == 1 and visited[next] == 0:
                stack.append(next)

    return 0


for tc in range(1, 11):
    Test_case, E = map(int, input().split())
    V = 100
    data = list(map(int, input().split()))
    # print(data)
    G = [[0] * (V) for _ in range(V)]

    for i in range(E):
        G[data[i*2]][data[i*2+1]] = 1

    print(f'#{tc}',DFS(0))