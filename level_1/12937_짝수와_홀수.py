"""
짝수와 홀수
- 문제 : https://programmers.co.kr/learn/courses/30/lessons/12937
- 입출력 예
num	return
3	"Odd"
4	"Even"
"""

def solution(num):
    return "Even" if num % 2 == 0 else "Odd"

if __name__ == "__main__":
    input_data = 4
    result = solution(input_data)
    print(result)