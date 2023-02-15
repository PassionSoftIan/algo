import sys
sys.stdin = open('4873_repeat_word_remover_input.txt')

# 스택을 활용한 두 번째 풀이
Test_case = int(input())

for tc in range(1, Test_case + 1):
    word = input()
    stack = []
    # print(word)
    for char in word:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
        # print(stack, char)
        # if not stack:
        #     stack.append(char)
        # elif stack and stack[-1] != char:
        #     stack.append(char)
        # elif stack and stack[-1] == char:
        #     stack.pop()

    # print(stack)
    print(len(stack))










# #1번 sol
# def search(word):
#     tmp = '' # 다음 조사 대상이 될 문자열
#     # 조사 대상 문자와 조사 대상 다음 문자가 같은지를 알아 보고
#     # 같으면 다음 조사 대상에서 두 글자 모두 제외
#     # 다르면, 현재 조사 대상인 문자는 다음 조사 대상에 포함
#     # 그리고, 조사 대상을 다음 칸으로 이동
#     # 조사 대상 index
#     idx = 0
#     while idx < len(word) - 1:
#         if word[idx] == word[idx+1]:
#             tmp += word[idx+2:]
#             word = tmp
#             # print(tmp)
#             idx = 0
#             tmp = ''
#             # print(word[idx], word[idx+1], 'True')
#             # break
#         else:
#             tmp += word[idx] # 다음 조사 대상에 현재 문자 추가
#             idx += 1        # 조사 위치 변경
#         # print(tmp, idx)
#     return word
#
# Test_case = int(input())
#
# for tc in range(1, Test_case + 1):
#     word = input()
#     # print(word)
#     print(len(search(word)))



