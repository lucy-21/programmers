"""
x만큼 간격이 있는 n개의 숫자
- 문제 : https://programmers.co.kr/learn/courses/30/lessons/12954
- 입출력 예
x	n	answer
2	5	[2,4,6,8,10]
4	3	[4,8,12]
-4	2	[-4, -8]
"""

def solution(x, n):
    return [x + (x * idx) for idx in range(n)]

if __name__ == "__main__":
    x = -4
    n = 2
    result = solution(x, n)
    print(result)