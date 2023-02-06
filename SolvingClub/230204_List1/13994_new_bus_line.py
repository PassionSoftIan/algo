import sys
sys.stdin = open('bus_input.txt')

Test_case = int(input())

for i in range(Test_case):
    Bus_line = int(input())
    Temp = [0] * 101
    one, two, three_result = [], [], []
    for j in range(Bus_line):
        Bus_line_number = list(map(int, input().split()))
        if Bus_line_number[0] == 1:
            if Bus_line_number[1] < Bus_line_number[-1]:
                one = [k for k in range(Bus_line_number[1], Bus_line_number[-1] + 1)]
            elif Bus_line_number[1] > Bus_line_number[-1]:
                one = [k for k in range(Bus_line_number[-1], Bus_line_number[1] + 1)]
            print(one)

        elif Bus_line_number[0] == 2:
            if Bus_line_number[1] < Bus_line_number[-1]:
                two = [k for k in list(range(Bus_line_number[1], Bus_line_number[-1] + 1))[0 : -1 : 2] + [Bus_line_number[-1]]]
            elif Bus_line_number[1] > Bus_line_number[-1]:
                two = [k for k in list(range(Bus_line_number[-1], Bus_line_number[1] + 1))[0 : -1 : 2] + [Bus_line_number[-1]]]
            print(two)

        elif Bus_line_number[0] == 3:
            if Bus_line_number[1] < Bus_line_number[-1]:
                three = [k for k in list(range(Bus_line_number[1], Bus_line_number[-1] + 1))]
            elif Bus_line_number[1] > Bus_line_number[-1]:
                three = [k for k in list(range(Bus_line_number[-1], Bus_line_number[1] + 1))]

            if three[0] % 2 == 0:
                three = [l for l in three if l == three[0] or l == three[-1] or l % 4 ==0]
            elif three[0] % 2 != 0:
                three = [l for l in three if l == three[0] or l == three[-1] or l % 3 == 0 and l % 10 != 0]
            print(three)
    final = []
    if one and two and three:
        final = one + two + three
    print(final)
    result_max = Temp[0]
    for m in final:
        Temp[m] += 1
        for n in range(1, len(Temp)):
            if result_max < Temp[n]:
                result_max = Temp[n]
    print(f'#{i+1} {result_max}')

# Test_case = int(input())
#
# for i in range(Test_case):
#     Bus_line = int(input())
#     Temp = [0] * 101
#     for j in range(Bus_line):
#         Bus_line_number = list(map(int, input().split()))
#         if Bus_line_number[0] == 1:
#             one = [k for k in range(Bus_line_number[1], Bus_line_number[-1] + 1)]
#         elif Bus_line_number[0] == 2:
#             two = [k for k in list(range(Bus_line_number[1], Bus_line_number[-1] + 1))[0 : -1 : 2] + [Bus_line_number[-1]]]
#         elif Bus_line_number[0] == 3:
#             three = [k for k in list(range(Bus_line_number[1], Bus_line_number[-1] + 1))]
#             if three[0] % 2 == 0:
#                 three_result = [l for l in three if l == three[0] or l == three[-1] or l % 4 ==0]
#             elif three[0] % 2 != 0:
#                 three_result = [l for l in three if l == three[0] or l == three[-1] or l % 3 == 0 and l % 10 != 0]
#             final = one + two + three_result
#             count = 1
#             for m in final:
#                 Temp[m] += 1
#             result_max = Temp[0]
#             for n in range(1, len(Temp)):
#                 if result_max < Temp[n]:
#                     result_max = Temp[n]
#             print(f'#{i+1} {result_max}')


# Test_case = int(input())
#
# for i in range(Test_case):
#     Bus_line = int(input())
#     Temp = [0] * 101
#     for j in range(Bus_line):
#         Bus_line_number = list(map(int, input().split()))
#         if Bus_line_number[0] == 1:
#             if Bus_line_number[1] < Bus_line_number[-1]:
#                 one = [k for k in range(Bus_line_number[1], Bus_line_number[-1] + 1)]
#             elif Bus_line_number[1] > Bus_line_number[-1]:
#                 one = [k for k in range(Bus_line_number[-1], Bus_line_number[1] + 1)]
#             # print(one)
#
#         elif Bus_line_number[0] == 2:
#             if Bus_line_number[1] < Bus_line_number[-1]:
#                 two = [k for k in list(range(Bus_line_number[1], Bus_line_number[-1] + 1))[0 : -1 : 2] + [Bus_line_number[-1]]]
#             elif Bus_line_number[1] > Bus_line_number[-1]:
#                 two = [k for k in list(range(Bus_line_number[-1], Bus_line_number[1] + 1))[0 : -1 : 2] + [Bus_line_number[-1]]]
#
#             # print(two)
#         elif Bus_line_number[0] == 3:
#             if Bus_line_number[1] < Bus_line_number[-1]:
#                 three = [k for k in list(range(Bus_line_number[1], Bus_line_number[-1] + 1))]
#             elif Bus_line_number[1] > Bus_line_number[-1]:
#                 three = [k for k in list(range(Bus_line_number[-1], Bus_line_number[1] + 1))]
#
#             if three[0] % 2 == 0:
#                 three_result = [l for l in three if l == three[0] or l == three[-1] or l % 4 ==0]
#             elif three[0] % 2 != 0:
#                 three_result = [l for l in three if l == three[0] or l == three[-1] or l % 3 == 0 and l % 10 != 0]
#             # print(three_result)
#             final = one + two + three_result
#             # print(final)
#             count = 1
#             for m in final:
#                 Temp[m] += 1
#             # print(Temp)
#             result_max = Temp[0]
#             for n in range(1, len(Temp)):
#                 if result_max < Temp[n]:
#                     result_max = Temp[n]
#             # print(result_max)
#             print(f'#{i+1} {result_max}')