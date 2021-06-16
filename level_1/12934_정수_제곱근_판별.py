"""
정수 제곱근 판별
- 문제 : https://programmers.co.kr/learn/courses/30/lessons/12934
- 입출력 예
n	return
121	144
3	-1
"""

def solution(n):
    import math
    sqrt_n = math.sqrt(n)
    return int(pow(sqrt_n + 1, 2)) if sqrt_n.is_integer() else -1

if __name__ == "__main__":
    input_data = 121
    result = solution(input_data)
    print(result)