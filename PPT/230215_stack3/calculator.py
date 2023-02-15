import sys
sys.stdin = open('cal_input.txt')

Test_case = int(input())

for tc in range(1, Test_case+1):
    example = int(input())
    for ec in range(example):
        cal = input()
        # print(cal)
        stack = [] # 연산자들을 담아둘 stack
        result = '' # 최종 결괏값
        #전체 식 순회
        for char in cal:
            # 연산자들이라면
            if char in '+-*/()':
                # print(char)
                # 연산자들의 우선순위에 맞춰서 값들을 Stack 에 넣는 과정
                if char in '(':
                    stack.append(char)
                elif char in '*/':
                    while stack and stack[-1] in '*/':
                        result += stack.pop()
                    stack.append(char)
                elif char in '+-':
                    while stack and stack[-1] in '*/':
                        result += stack.pop()
                    stack.append(char)
                elif char in ')':
                    while stack and stack[-1] != '(':
                        result += stack.pop()
                    stack.pop()
            else:
                result += char
        while stack:
            result += stack.pop()
        print(result)
        # print(stack)