import sys
sys.stdin = open('caculator_input.txt')

Test_case = int(input())

for tc in range(1, Test_case+1):
    cal = input()
    print(cal)
    stack = []
    result = 0
    for char in cal:
        if char not in '+-*/':
            stack.append(char)
        else:
            x = int(stack.pop())
            y = int(stack.pop())
            if char == '+':
                stack.append(y + x)
            elif char == '-':
                stack.append(y + x)
            elif char == '*':
                stack.append(y + x)
            elif char == '/':
                stack.append(y + x)
    print(stack[-1])
    result = stack.pop()
    print(result)
