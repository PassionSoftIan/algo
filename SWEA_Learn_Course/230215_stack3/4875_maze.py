import sys
sys.stdin = open('4875_maze_input.txt')

def BT(start):
    # 조사를 시작할 좌표를 stack에 넣음
    stack = [start]
    # stack이 true 일 동안 무한 반복
    while stack:
        start = stack.pop() # 조사를 하려면 좌표가 필요하니 시작 점 좌표 pop으로 뽑아 낸다
        # 오른쪽 아래 왼쪽 위 4방향으로 조사할꺼니 4번 돌려주는 for문 작성
        for k in range(4):
            nx, ny = dx[k] + start[1], dy[k] + start[0] # nx, ny 즉, 4 방향을 조사하는 식별자 단순화(start 넣은 것은 시작 좌표)
            if 0 <= nx < N and 0 <= ny < N: # 조사하는 좌표가 마이너스가 되거나 한정된 공간을 벗어나면 행렬 공간을 벗어나니까 그렇게 되지 않게 범위 설정
                if arr[ny][nx] == 3: # 조사한 값이 3이면
                    return 1 # 1 출력
                if arr[ny][nx] == 0: # 조사한 값이 0이면
                    stack.append([ny, nx]) # 스택에 집어넣고
                    arr[ny][nx] += 1 # 스택 지나온 것 지나왔다는 표시
    return 0 # while 문을 다 마쳤는데도 3을 못찾았다면 0 출력

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    stack = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2: # start 좌표 찾는 식
                start = [i, j] # start 좌표
                break
    print(f'#{tc}', BT(start))





