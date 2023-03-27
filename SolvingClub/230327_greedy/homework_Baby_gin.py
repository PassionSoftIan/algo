import sys
sys.stdin = open('homework_Baby_gin_input.txt')

def backtracking(depth):
    global char
    if depth == 6:
        if result[0] == result[1] == result[2] or result[0] == result[1]-1 == result[2]-2:
            if result[3] == result[4]-1 == result[5]-2 or result[3] == result[4] == result[5]:
                char = 'True'
                return
        return

    for i in range(6):
        if visited[i] == 0:
            result.append(lst[i])
            visited[i] = 1
            backtracking(depth + 1)
            visited[i] = 0
            result.pop()


Test_case = int(input())
for tc in range(Test_case):
    lst = list(map(int, input()))
    visited = [0] * 6
    result = []

    char = ''

    backtracking(0)
    if char == '':
        print('False')
    else:
        print(char)