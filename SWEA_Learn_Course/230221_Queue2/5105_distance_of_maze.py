import sys
sys.stdin = open('5105_distance_of_maze_input.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    stack = []
    visited = [[0] * N for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    result = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                stack.append([i, j])
    count = 0
    result_fin= 0
    while stack:
        i, j = stack.pop(0)
        for k in range(4):
            nx, ny = j + dx[k], i + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[ny][nx] == 3:
                    result += 1
                    print(result_fin)
                    break

                if arr[ny][nx] == 0 and visited[ny][nx] != 1:
                    stack.append([ny, nx])
                    count += 1
                    visited[ny][nx] = 1
        if count > 0:
            result_fin += 1

        else:
            if result == 1:
                break