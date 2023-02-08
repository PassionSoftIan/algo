import sys
sys.stdin = open('Ladder_input.txt')


# 하, 좌, 우
dx = [1, 0, 0]
dy = [0, -1, 1]

def search(x,y):
    visited = [[0] * 100 for _ in range(100)]
    # 첫 출발 지점이무엇인지 미리 기록
    original_y = y
    visited[x][y] = 1

    while x != 99: # 가장 아래층까지 도착하기 전까지
        # 조사 방향? 3방향 : 아래, 좌, 우
        for i in range(3):
            # 다음 지역 x 좌표 = 현재 x + 다음 방향
            nx = x + dx[i] # [1, 0, 0]
            ny = y + dy[i] # [0, -1, 1]

            # 범위를 벗어나지 않고, 다음 조사 대상이 1이면이동
            if 0 <= nx < 100 and 0 <=ny < 100 and data[nx][ny] == 1 and visited[nx][ny] == 0:
                # 위 조건을 만족했으니 이동
                visited[nx][ny] = 1
                x, y = nx, ny

    if data[x][y] == 2:
        return original_y
    else:
        return 0







        # 조사를 끝냈는데 result가 0이 아니다? 답을 찾았다.