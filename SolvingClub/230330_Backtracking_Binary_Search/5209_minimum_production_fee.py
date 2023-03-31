import sys
sys.stdin = open('5209_minimum_production_fee_input.txt')

def backtracking(depth):
    global max_result

    result = 0
    if depth == N:
        if max_result < result:
            max_result = result
        return

    if result <


Test_case = int(input())

for tc in range(1, Test_case+1):
    N = int(input())
    percent = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]
    visited = [0] * N
    print(percent)
    print(visited)
    max_result = 0

    backtracking(0)