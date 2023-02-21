import sys
sys.stdin = open('1224_calculator3_input.txt')

def cal(word, stack):
    for i in word:
        if i not in '*+()':
            stack.append(int(i))
        else:
            x = stack.pop()
            y = stack.pop()
            if i == '*':
                stack.append(y * x)
            elif i == '+':
                stack.append(y + x)
    return stack[-1]




for tc in range(10):
    Tl = int(input())
    word = input()
    # print(word)
    result = ''
    stack = []
    for i in word:
        if i in '*+()':
            if not stack:
                stack.append(i)
            elif i in '(':
                stack.append(i)
            elif i in '*':
                while stack and stack[-1] == '*':
                    result += stack.pop()
                stack.append(i)
            elif i in '+':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(i)
            elif i in ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
        else:
            result += i
    while stack:
        result += stack.pop()
    # print(result)
    print(f'#{tc+1}', cal(result, []))