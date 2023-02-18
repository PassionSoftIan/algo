import sys
sys.stdin = open('1217_power_input.txt')

def power(N, M):
    if M == 1:
        return N
    else:
        return N * power(N, M-1)

for tc in range(1, 11):
    tc_num = int(input())
    N, M = map(int, input().split())

    print(f'#{tc} {power(N, M)}')