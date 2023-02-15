import sys
sys.stdin = open('4874_Forth_input.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    arr = input().split()
    stack = []
    try:
        count = 0
        if arr[-1] != '.':
            print(f'#{tc} error')
            break
        else:
            if count == 0:
                for i in arr:
                    if i not in '*+-/.':
                        stack.append(int(i))

                    if i == '*':
                        x = stack.pop()
                        y = stack.pop()
                        stack.append(x * y)

                    if i == '+':
                        x = stack.pop()
                        y = stack.pop()
                        stack.append(x + y)

                    if i == '/':
                        x = stack.pop()
                        y = stack.pop()
                        stack.append(y // x)

                    if i == '-':
                        x = stack.pop()
                        y = stack.pop()
                        stack.append(y - x)

                    if i == '.':
                        count += 1
                        if count > 1:
                            stack.pop()
                            stack.append('error')

    except:
        print(f'#{tc} error')
        continue
    if len(stack) > 1:
        for i in range(len(stack)):
            stack.pop()
        stack.append('error')
    print(f'#{tc}', *stack)