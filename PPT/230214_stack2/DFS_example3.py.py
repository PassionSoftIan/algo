import sys
sys.stdin = open('DFS_example3_input.txt')

# 조사 시작하는 노드의 번호
def DFS(start): # 문제에서는 1번 노드에서 출발
    stack = [start] # 시작지점
    visited = [0] * (V+1) # 이전에 방문한 곳은 다시 가지 않도록
    # 언제까지 조사 할거냐
    while stack:    # stack에 값이 있는 동안
        start = stack.pop() # 다음 조사 대상 꺼내기
        # 방문 표시
        # 이전 번에 방문한 적 없다면
        if visited[start] == 0:
            visited[start] += 1
            print(start, end=' ')
            # 현재 위치 start를 기준으로,
            # 0부터 V+1번 노드까지 모두 조사 가능한지 탐색
            for next in range(1, V+1):
                if G[start][next] == 1 and visited[next] ==0:
                    # 다음 조사 대상에 next를 집어 넣는다.
                    stack.append(next)
                    print()
                    print(stack)

# V = Voltex = 노드
# E = Edge = 간선
V, E = map(int, input().split())
# 간선 정보
data = list(map(int, input().split()))
print(data)
# 위 내용을 통해 이동 가능 정보를 담은 2차원 배열 만들 것
# 0부터시작하니 +1개를 해야 V숫자 만큼 만들어진다
G = [[0]*(V+1) for _ in range(V+1)]

for i in range(E): # 모든 간선의 길이 만큼 반복
    '''
    matrix[1][2] = 1
    matrix[2][1] = 1
    이동 가능 정보를 담은 matrix의 인덱스는 각 노드 번호를 의미한다.
    간선 정보 data의 0번째 -> 첫 번째 출발 노드
    간선 정보 data의 1번째 -> 첫 번째 도착 노드를 의미
    
    matrix[data[0]][data[1]] = 1
    matrix[data[1]][data[0]] = 1
    
    matrix[data[2]][data[3]] = 1
    matrix[data[3]][data[2]] = 1
    
    i*2, i*2+1
    i == 0
    i*2 = 0
    i*2+1 = 1
    
    i == 1
    i*2 = 2
    i*2+1 = 3
    '''
    G[data[i * 2]][data[i * 2 + 1]] = 1
    G[data[i * 2 + 1]][data[i * 2]] = 1
print()
for i in range(V+1):
    print(G[i])
# print(V, E, data)
DFS(1)