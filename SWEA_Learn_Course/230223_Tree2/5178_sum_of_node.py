import sys
sys.stdin = open('5178_sum_of_node_input.txt')

def order(node):
    if node > 1:
        edge[node//2] += edge[node]
        order(node-1)



Test_case = int(input())

for tc in range(1, Test_case + 1):
    V, M, L = map(int, input().split())
    edge = [0] * (V+1)
    for i in range(M):
        n, c = map(int, input().split())
        edge[n] = c

    order(V)
    print(f'#{tc} {edge[L]}')
