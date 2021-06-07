""" 
로또의 최고 순위와 최저 순위
- 문제 : https://programmers.co.kr/learn/courses/30/lessons/77484
- 입출력 예
lottos	win_nums	result
[44, 1, 0, 0, 31, 25]	[31, 10, 45, 1, 6, 19]	[3, 5]
[0, 0, 0, 0, 0, 0]	[38, 19, 20, 40, 15, 25]	[1, 6]
[45, 4, 35, 20, 3, 9]	[20, 9, 3, 45, 4, 35]	[1, 1]
[1, 2, 3, 4, 5, 6]	[7, 8, 9, 10, 11, 12]	[6, 6]
"""

def solution(lottos, win_nums):
    # 매칭 수 구하기
    zero_count, match_count = 0, 0
    
    for lotto in lottos:
        if lotto == 0: zero_count += 1
        elif lotto in win_nums: match_count += 1

    # 순위 구하기
    high_rank = min(7 - match_count - zero_count, 6)
    low_rank = min(7 - match_count, 6)

    return [high_rank, low_rank]

if __name__ == "__main__":
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]
    print(solution(lottos, win_nums))