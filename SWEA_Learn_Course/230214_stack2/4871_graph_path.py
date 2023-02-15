import sys
sys.stdin = open('4871_graph_path_input.txt')

def DFS(start):
    # 첫 시작 위치 아무튼 방문함
    visited[start] = 1
    stack = [start]
    while stack:
        start = stack.pop()
        # print(stack, end=' ')
        if start == G: # 현재 조사 대상이 도착지점인지 체크
            # 그럼 더 조사하지 말고 break
            return 1


        for next in range(1, V+1):
            if data[start][next] and not visited[next]:
                visited[next] = 1
                stack.append(next)
    return 0

Test_case = int(input())

for tc in range(1, Test_case+1):
    V, E = map(int, input().split())
    data = [[0]*(V+1) for _ in range(V+1)]
    # 방문 표시용 리스트
    visited = [0] * (V+1)
    # 간선 정보 입력 받기
    for i in range(E):
        x, y = map(int, input().split())
        # print(x, y)
        data[x][y] = 1
        data[y][x] = 1
    # 시작지점 S, 도착지점 G
    S, G = map(int, input().split())

    print('ans : ',DFS(S))