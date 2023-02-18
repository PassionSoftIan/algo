import sys
sys.stdin = open('1234_password_input.txt')

for tc in range(10):
    N, word = map(int,input().split())
    word_str = [i for i in str(word)]
    # print(word_str)
    stack = []
    for i in word_str:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    result = int(''.join(stack))

    print(f'#{tc+1} {result}')