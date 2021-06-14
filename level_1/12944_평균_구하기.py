"""
평균 구하기
- 문제 : https://programmers.co.kr/learn/courses/30/lessons/12944
- 입출력 예
arr	return
[1,2,3,4]	2.5
[5,5]	5
"""

def solution(arr):
    return sum(arr) / len(arr)

if __name__ == "__main__":
    input_data = [1,2,3,4]
    result = solution(input_data)
    print(result)