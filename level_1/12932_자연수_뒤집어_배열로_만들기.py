"""
자연수 뒤집어 배열로 만들기
- 문제 : https://programmers.co.kr/learn/courses/30/lessons/12932
- 입출력 예
n	return
12345	[5,4,3,2,1]
"""

def solution(n):
    return list(reversed([int(num) for num in str(n)]))

if __name__ == "__main__":
    input_data = 12345
    result = solution(input_data)
    print(result)