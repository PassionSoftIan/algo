import sys
sys.stdin = open('char_number_input.txt')

Test_case = int(input())

for tc in range(Test_case):
    str1 = list(map(str, input()))
    str2 = list(map(str, input()))

    max = 0
    for i in range(len(str2)):
        count = 0
        for j in range(len(str1)):
            if str2[i] == str2[j]:
                count += 1
                if max > count:
                    max = count
        print(max)
    print(f'#{tc+1} {max}')