import sys
sys.stdin = open('input.txt')

Test_case = int(input())

for i in range(0, Test_case):
    Test_case_num = int(input())

    number = list(map(int, input().split()))

    if Test_case_num == len(number):

        result_min = number[0]
        for num in number[1:]:
            if result_min > num:
                result_min = num
        result_max = number[0]
        for num in number[1:]:
            if result_max < num:
                result_max = num
        result = result_max - result_min
        print(f'#{i+1} {result}')


    elif Test_case_num != len(number):
        print('입력 개수 오류입니다.')