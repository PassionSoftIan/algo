import sys
sys.stdin = open('example2_BFS_input.txt')

def BFS(S, N):              # BFS함수 생성
    visited = [0] * (N+1)   # visited 생성
    q = [S]                 # 큐 생성
                            # 시작점 인큐
    visited[S] = 1          # 시작점 인큐 표시
    while q:                # 큐가 비어있지 않으면
        t = q.pop(0)        # 디큐
        print(t, end = ' ') # t에서 처리할 일
        for S in adjL[t]:
            if visited[S] == 0:
                q.append(S) # 인큐
                visited[S] = visited[t] + 1 # S 인큐 되었음 표시
                # v 인큐
    # visited 생성
    # 큐 생성
    # 시작점 인큐
    # 시작점 인큐표시
V, E = map(int, input().split())
arr = list(map(int, input().split()))
print(arr)
adjL = [[] for _ in range(V+1)]
print(adjL)
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjL[n1].append(n2)
    adjL[n2].append(n1)
print(adjL)

BFS(1, V) # 1은 시작 정점, V는 마지막 정점