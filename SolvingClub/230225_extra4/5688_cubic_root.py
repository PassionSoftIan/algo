import sys, copy
sys.stdin = open('5688_cubic_root_input.txt')

def root(N):
    if N <= 0:
        return -1
    x = 1
    while True:
        if x ** 3 == N:
            return x
        elif x ** 3 > N:
            return -1
        else:
            x+=1



Test_case = int(input())

for tc in range(1, Test_case + 1):
    N = int(input())
    print(f'#{tc} {root(N)}')