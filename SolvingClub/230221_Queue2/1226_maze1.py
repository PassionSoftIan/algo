import sys
sys.stdin = open('1226_maze1_input.txt')

for tc in range(1, 11):
    Test_case = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    stack = []
    visited = [[0] * 16 for _ in range(16)]
    result = 0

    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                stack.append([i,j])
    while stack:
        i, j = stack.pop(0)
        for k in range(4):
            nx, ny = j + dx[k], i + dy[k]
            if arr[ny][nx] == 0 and visited[ny][nx] != 1:
                visited[ny][nx] += 1
                stack.append([ny, nx])
            if arr[ny][nx] == 3:
                result += 1
                break
        else:
            if result == 1:
                break
    print(f'#{tc} {result}')