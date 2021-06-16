"""
정수 내림차순으로 배치하기
- 문제 : https://programmers.co.kr/learn/courses/30/lessons/12933
- 입출력 예
n	return
118372	873211
"""

def solution(n):
    return int("".join(sorted(str(n), reverse=True)))

if __name__ == "__main__":
    input_data = 118372
    result = solution(input_data)
    print(result)