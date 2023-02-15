import sys
sys.stdin = open('fastest_string_typing_input.txt')

Test_case = int(input())

for tc in range(Test_case):

    str = input().split()
    l = len(str[1])
    count = 0
    # for i in range(len(str[0]) - len(str[1])+1):
    #         if str[0][i] == str[1][]
    if str[1] in str[0]:
        count += 1

    print(count)

    # print(len(str[0]) - len(str[1])*count + count)