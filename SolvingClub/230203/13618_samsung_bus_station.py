import sys
sys.stdin = open('s_input.txt')

Test_case = int(input()) # 테스트케이스 갯수
#
# Bus_line = int(input()) # N개 버스 노선
#
# Bus_number = list(map(int, input().split())) # Ai,Bi
#
# Bus_station = int(input())   # P개의 버스 정류장

for i in range(Test_case):
    Bus_line = int(input())
    Temp_list = [0] * 5000

    for j in range(Bus_line):
        Bus_number = list(map(int, input().split()))
        for m in range(Bus_number[0], Bus_number[1]+1):
            Temp_list[m] += 1


    for k in range(1):
        Bus_station = int(input())
        Final = []
        for l in range(1, Bus_station+1):
            Station_num = int(input())
            Final.append(Temp_list[Station_num])

    # for i in Final:
    #     print(i,end= " ")

    print(f'#{i+1}', *Final)