import sys
sys.stdin = open('1244_max_prize_input.txt')

def check(start):
    max_result = 0
    idx_max = 0

    for n in range(start, len(num)):
        if max_result <= num[n]:
            max_result = num[n]
            idx_max = n

    if idx_max == start:
        max_result = 0
        check(start+1)
        return

    if idx_max > start:
        num[idx_max], num[start] = num[start], num[idx_max]


Test_case = int(input())

for tc in range(1, Test_case+1):
    N, M = map(str, input().split())
    M = int(M)
    num = []
    for number in N:
        num.append(int(number))


    for i in range(M):
        check(i)

    print(f'#{tc} ', *num, sep='')