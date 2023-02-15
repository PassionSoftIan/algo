import sys
sys.stdin = open('sample_input.txt')

Test_case_num = int(input())


for i in range(0, Test_case_num):
    card_number = int(input())
    card_num_list = list(map(int, input()))
    temp_list = [0] * 10
    for num in card_num_list:
        temp_list[num] += 1
        result_max = temp_list[0]
        result_index = 0
        for number in range(1, len(temp_list)):
            if result_max <= temp_list[number]:
                result_max = temp_list[number]
                result_index = number


    print(f'#{i+1} {result_index} {result_max}')






