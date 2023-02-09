import sys
sys.stdin = open('string_pattern_input.txt', encoding = 'utf-8')

# for tc in range(10):
#     tc = int(input())
#     pattern = input()
#     target = input()
#     M = len(pattern)
#     N = len(target)
#
#     count = 0
#     for i in range(N-M+1):
#         for j in range(M):
#             if target[i+j] != pattern[j]:
#                 break
#         else:
#             count += 1
#
#     print(f'#{tc} {count}')


# 패턴 내의 패턴이 존재하는지 그리고 그 정보를 담기 위한 리스트 만드는 함수
def make_lps(pattern):
    # 중계 리스트
    lps = [0] * len(pattern)
    # lps의 각 인덱스에 이전 패턴정보를 담기 위한 인덱스
    lps_idx = 0
    for i in range(1, len(pattern)):
        # 이전번 글자와 지금 조사하는 글자가 같다면
        if pattern[lps_idx]== pattern[i]:
            lps[i] = lps_idx + 1
            lps_idx += 1
        else:
            # 다를 때 0으로 초기화 시켜서 패턴의 0번째와 다시 비교
            lps_idx = 0
            if pattern[i] == pattern[lps_idx]:
                lps[i] = lps_idx + 1
    return lps


def KMP(pattern, target):
    lps = make_lps(pattern)
    # 조사 시작은 Brute Force 방법과 동일하게 시작
    p_idx = 0
    t_idx = 0
    count = 0
    while t_idx < len(target):
        if pattern[p_idx] == target[t_idx]:
            t_idx += 1
            p_idx += 1
        else:
            if p_idx == 0:
                t_idx += 1
            else:
                p_idx = lps[p_idx - 1]
        if p_idx == len(pattern):
            count += 1
            p_idx = 0
    return count

#보이어무어

def search(pattern, char):
    # 어디까지 동일한 값을 가지고 있는지 확인
    for i in range(len(pattern)-2, -1, -1):
        # 동일한 값이 있다면
        if pattern[i] == char:
            # 그 위치까지 이동하도록 index 번호 넘겨주기
            return len(pattern) - i - 1
    # 없으면
    return len(pattern)

def boyer_moor(pattern, target):
    count = 0
    t_idx = 0

    # 조사 범위가 조금 다르다.
    # 조사 대상 idx가 전체 길이 - 패턴길이를 넘기 전까지
    while t_idx <= len(target) - len(pattern):
        # 뒤에서부터 조사
        p_idx = len(pattern) - 1
        # p_idx가 0이 되기 전까지
        while p_idx >= 0:
            # 두 조사 대상이 같지 않을 때
            if pattern[p_idx] != target[t_idx + p_idx]:
                # 다음 조사 위치로 이당하기 위한 값을 만들어야 한다.
                next = search(pattern, target[t_idx + len(pattern) - 1])
                break
            p_idx -= 1
        if p_idx == -1: # 패턴의 끝까지 조사했다면
            count += 1
            t_idx += 1
        # 아니면?
        else:
            t_idx += next
    return count


for _ in range(10):
    tc = int(input())
    pattern = input()
    target = input()