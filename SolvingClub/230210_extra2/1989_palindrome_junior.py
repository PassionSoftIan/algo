import sys
sys.stdin = open('palindrome_input.txt')

Test_case = int(input())

for tc in range(Test_case):
    char = list(input())
    for i in range(len(char)):
        count = 0
        if char[:] == char[::-1]:
            count += 1

    print(f'#{tc+1} {count}')