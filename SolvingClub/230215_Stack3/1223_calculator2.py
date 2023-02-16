import sys
sys.stdin = open('1223_calculator2_input.txt')

def check(char, stack):
    for i in char:
        if i not in '+/*-':
            stack.append(int(i))
        else:
            x = stack.pop()
            y = stack.pop()
            if i == '+':
                stack.append(x + y)
            elif i == '*':
                stack.append(x * y)
            elif i == '-':
                stack.append(y - x)
            elif i == '/':
                stack.append(y / x)
    return stack[-1]



for tc in range(1, 11):
    char_len = int(input())
    char = input()
    stack = []
    result = ''
    for i in char:
        if i in '*+':
            if not stack:
                stack.append(i)
            elif i in '*':
                while stack and stack[-1] == '*':
                    result += stack.pop()
                stack.append(i)
            elif i in '+':
                while stack:
                    result += stack.pop()
                stack.append(i)
        else:
            result += i
    while stack:
        result += stack.pop()

    result = check(result, [])
    print(f'#{tc} {result}')