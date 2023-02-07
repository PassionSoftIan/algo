import sys
sys.stdin = open('binary_input.txt')

Test_case = int(input())

def BinarySearch(N, key):
        start = 1
        end = N
        count = 0
        while start <= end:
            middle = (start + end) // 2
            if middle == key:
                count += 1
                return count
            elif middle > key:
                end = middle
                count += 1
            elif middle < key:
                start = middle
                count += 1

for tc in range(Test_case):
    page, A, B = map(int, input().split())
    if BinarySearch(page, A) > BinarySearch(page, B):
        winner = 'B'
    elif BinarySearch(page, A) < BinarySearch(page, B):
        winner = 'A'
    else:
        winner = 0
    print(f'#{tc+1} {winner}')







    # book = [i for i in range(1, page[0]+1)]
    # # A B가 찾아야 하는 값
    # A = page[1]
    # B = page[2]
    # # 인덱스 처음 시작
    # start = 0
    # # 인덱스의 끝
    # end = page[0] - 1
    # # A B 작업 횟수
    # count_A = 0
    # count_B = 0
    # # 인덱스의 중간 값
    # middle = (start + end) // 2
    # for j in range(2):
    #     while book[middle] != page[j]:
    #         if book[middle] > page[j]:
    #             if j == 1:
    #                 count_A += 1
    #                 end = middle
    #             else:
    #                 count_B += 1
    #                 end = middle
    #         elif book[middle] < page[j]:
    #             if j ==1:
    #                 count_A += 1
    #                 start = middle
    #             else:
    #                 count_B += 1
    #                 start = middle
    # if count_A > count_B:
    #     print('B')
    # elif count_A < count_B:
    #     print('A')
    # elif count_A == count_B:
    #     print(0)





    # if count_A > count_B:
    #     print('B')
    # elif count_A < count_B:
    #     print('A')
    # else:
    #     print(0)








    # print(book)
    # print(A)
    # print(B)