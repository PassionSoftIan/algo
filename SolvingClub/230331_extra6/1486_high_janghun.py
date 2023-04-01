import sys
sys.stdin = open('1486_high_janghun_input.txt')


def backtracking(depth, s):
    global count, result, max_result

    if result > B:
        if max_result == 0:
            max_result = result
            return

        if max_result - B > result - B:
            max_result = result
            return

    for i in range(s, N):
        if visited[i] == 0:
            visited[i] = 1
            result += staff[i]

            if result == B:
                max_result = result
                break

            if result - B > max_result - B and max_result != 0:
                result -= staff[i]
                visited[i] = 0
                continue

            else:
                backtracking(depth + 1, i)
                result -= staff[i]
                visited[i] = 0

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N, B = map(int, input().split())

    staff = list(map(int, input().split()))
    visited = [0] * N
    result = 0
    max_result = 0

    backtracking(0, 0)

    print(f'#{tc} {max_result - B}')