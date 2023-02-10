import sys
sys.stdin = open('diamond_input.txt')

Test_case = int(input())

for tc in range(Test_case):
    char = input()
    temp = [[0] * ((len(char) * 4) + 1) for _ in range(5)]
    for i in range(5):
        for j in range((len(char) * 4) +1):
            if i == 0 and j < len(char) * 4 - 1 and temp[i][j] == 0 and temp[i][j+1]:
                temp[i][j+2] = '#'

    print(temp)