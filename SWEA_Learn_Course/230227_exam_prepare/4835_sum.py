import sys
sys.stdin = open('4835_sum.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    max_result = 0
    min_result = 10000000000
    for i in range(N-M+1):
        result = 0
        for j in range(M):
            result += num[i+j]
        if max_result < result:
            max_result = result
        if min_result > result:
            min_result = result


    print(f'#{tc} {max_result - min_result}')