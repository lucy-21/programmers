"""
제일 작은 수 제거하기
- 문제 : https://programmers.co.kr/learn/courses/30/lessons/12935
- 입출력 예
arr	return
[4,3,2,1]	[4,3,2]
[10]	[-1]
"""

def solution(arr):
    if len(arr) > 1: 
        arr.remove(sorted(arr)[0])
        return arr
    else:
        return [-1]      

if __name__ == "__main__":
    input_data = [4,3,2,1]
    result = solution(input_data)
    print(result)