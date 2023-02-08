import sys
sys.stdin = open('comparision_input.txt')

Test_case = int(input())

for tc in range(Test_case):
    checker = input()
    char = input()
    if checker in char:
        print(f'#{tc+1} 1')
    else:
        print(f'#{tc+1} 0')