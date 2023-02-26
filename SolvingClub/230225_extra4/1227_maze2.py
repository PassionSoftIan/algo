import sys
sys.stdin = open('1227_maze2_input.txt')

def BFS(start):
    stack = [start]
    while stack:
        i, j = stack.pop(0)
        for k in range(4):
            nx, ny = j + dx[k], i + dy[k]
            if 0 <= nx < 100 and 0 <= ny < 100:
                if arr[ny][nx] == 0:
                    stack.append([ny, nx])
                    arr[ny][nx] = 1
                if arr[ny][nx] == 3:
                    return 1
    return 0


for tc in range(1, 11):
    Test_case = int(input())
    arr = [list(map(int, input())) for _ in range(100)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(1, 100):
        for j in range(1, 100):
            if arr[i][j] == 2:
                start = [i, j]
    print(f'#{tc} {BFS(start)}')