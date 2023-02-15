import sys
sys.stdin = open('input.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    bracket = input()
    stack = []
    # print(bracket)
    result = 1
    for char in bracket:
        # print(char)
        if char == '(':
            stack.append(char)
            # print(stack)
        else:
            if stack:
                stack.pop()
            else:
                result = -1
                break
    else:
        if stack:
            result = -1
    print(result)
    # print(stack)