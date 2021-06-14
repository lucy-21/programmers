"""
하샤드 수
- 문제 : https://programmers.co.kr/learn/courses/30/lessons/12947
- 입출력 예
arr	return
10	true
12	true
11	false
13	false
"""

def solution(x):
    return x % sum([int(num) for num in str(x)]) == 0

if __name__ == "__main__":
    x = 13
    result = solution(x)
    print(result)