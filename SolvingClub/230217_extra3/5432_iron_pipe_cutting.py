import sys
sys.stdin = open('5432_iron_pipe_cutting_input.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    pipe = input()
    print(pipe)
    stack = []
    count = 0
    result = 0
    for i in range(len(pipe)):
        if pipe[i] in '(':
            count += 1
        elif pipe[i] in ')' and pipe[i-1] == ')':
            result += count
            count -= 1
        elif pipe[i] in ')':
            count -= 1
            result += count
    print(f'#{tc} {result}')
