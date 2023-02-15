import sys
sys.stdin = open('4866_bracket_check_input.txt')

Test_case = int(input())

for tc in range(1, Test_case + 1):
    word = input()
    # print(word)

    # 최종 결괏값
    result = 1
    stack = []
    for char in word:
        # print(stack, char)
        if char == '(' or char == '{':
            stack.append(char)
        else:
            if char == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                    pass
                elif not stack: # 스택이 비었는데
                    result = 0
                    # 한 번 이라도 실패하면 더 이상 조사 필요 없음
                    break
                elif stack[-1] != '(':
                    result = 0
                    break
            if char == '}':
                if not stack or stack[-1] != '{':
                    result = 0
                    pass
                else:
                    stack.pop()
    if stack:
        result = 0
    print(f'#{tc} {result}')