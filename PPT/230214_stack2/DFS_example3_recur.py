import sys
sys.stdin = open('DFS_example3_input.txt')


def DFS(start):
    visited[start] = 1
    print(start, end=' ')

    # 다음 조사 가능 위치 찾기
    for next in range(1, V+1):
        # 인접해있고, 방문 한 경험이 없는 곳
        if G[start][next] and not visited[next]:
            # 조사를 한다는 행위
            DFS(next)


# V = Voltex = 노드
# E = Edge = 간선
V, E = map(int, input().split())
# 간선 정보
data = list(map(int, input().split()))
# 방문 표시용 배열 생성
visited = [0] * (V+1)

# 위 내용을 통해 이동 가능 정보를 담은 2차원 배열 만들 것
# 0부터시작하니 +1개를 해야 V숫자 만큼 만들어진다
G = [[0]*(V+1) for _ in range(V+1)]

# 인접 행렬 그리기
for i in range(E): # 간선의 개수 만큼 그리기
    # 두개의 노드가 이어져 있는 정보
    n1, n2 = data[i*2], data[i*2+1]
    G[n1][n2] = 1   # n1에서 n2로 갈 수 있다.
    G[n2][n1] = 1   # 양방향으로 이동 가능하므로

print(data)
for i in range(0, len(data), 2):
    print(data[i], data[i+1])

for mat in G:
    print(mat)

DFS(1)