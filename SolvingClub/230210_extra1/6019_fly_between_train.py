import sys
sys.stdin = open('fly_input.txt')

Test_case = int(input())

for tc in range(Test_case):
    number = list(map(int, input().split()))

    A = number[0]/(number[1] + number[2])
    print(f'#{tc+1} {A * number[3]}')