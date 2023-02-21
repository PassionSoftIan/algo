import sys
sys.stdin = open('10966_water_play_input.txt')

def check(start):
    stack = [start]
    start = stack.pop()
    max_result = 0
    for k in range(4):
        ny, nx = n + dy[k] + start[1], m + dx[k] + start[0]
    while arr[ny][nx] != 2:
        count = 0
        result = 0
        visited = [[0] * M for _ in range(N)]
        if 0 <= ny < N and 0 <= nx < M:
            if arr[ny][nx] == 0 and visited[ny][nx] != 1:
                if arr[ny][nx] == 2 and result == 0:
                    count += 1
                    result = count
                    break
                if arr[ny][nx] == 2 and result != 0:
                    count += 1
                    if result > count:
                        result = count
                        break
                if arr[ny][nx] == 0:
                    stack.append([ny,nx])
                    visited[ny][nx] = 1
                    count += 1
        result += max_result
    return max_result


Test_case = int(input())

for tc in range(1, Test_case + 1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                arr[i][j] = 2
            elif arr[i][j] == 'L':
                arr[i][j] = 0
    # print(arr)
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    # print(visited)
    result_fin = 0
    for n in range(N):
        for m in range(M):
            if arr[n][m] == 0:
                start = [n, m]
                break
    print(check(start))