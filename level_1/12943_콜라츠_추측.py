"""
콜라츠 추축
- 문제 : https://programmers.co.kr/learn/courses/30/lessons/12943
- 입출력 예
n	result
6	8
16	4
626331	-1
"""

def solution(num):
    return collatz(0, num)

def collatz(idx, num):
    if num == 1: return idx
    elif idx >= 500: return -1

    if num % 2 == 0: return collatz(idx + 1, num / 2)
    else: return collatz(idx + 1, (num * 3) + 1)

if __name__ == "__main__":
    input_data = 626331
    result = solution(input_data)
    print(result)