import sys
sys.stdin = open('1959_two_numbers.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    N, M = map(int, input().split())
    Aj = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    A = len(Aj)
    B = len(Bj)
    T = 0
    max_result = int(0)
    if len(Aj) <= len(Bj):
        T = len(Aj)
        for j in range(abs(A - B)+1):
            result = 0
            for i in range(T):
                result += Aj[i] * Bj[i + j]
            if result > max_result:
                max_result = result
    else:
        T = len(Bj)
        for j in range(abs(A - B)+1):
            result = 0
            for i in range(T):
                result += Aj[i + j] * Bj[i]
            if result > max_result:
                max_result = result
    print(f'#{tc} {max_result}')