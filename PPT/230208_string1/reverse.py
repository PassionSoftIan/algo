import sys
sys.stdin = open('reverse.txt')


Test_case = int(input())

# for tc in range(Test_case):
#     word = input()
#
#     print(f'#{tc+1} {word[::-1]}')

for tc in range(Test_case):
    word = list(map(str, input()))

    for i in range(len(word)//2):
        word[i], word[-i-1] = word[-i-1], word[i]

    print(''.join(word))