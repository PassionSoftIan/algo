import sys
sys.stdin = open('2817_partition_sum_input.txt')

def backtracking(depth, start):
    global count, result

    if result == K:
        count += 1
        return

    for i in range(start, N):
        if visited[i] == 0:
            visited[i] = 1
            result += num[i]

            if result > K:
                result -= num[i]
                visited[i] = 0
                continue

            else:
                backtracking(depth+1, i)
                result -= num[i]
                visited[i] = 0

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N, K = map(int, input().split())
    num = list(map(int, input().split()))

    visited = [0] * N
    result = 0
    count = 0

    backtracking(0, 0)

    print(f'#{tc}', count)