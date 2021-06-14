"""
최대공약수와 최소공배수
- 문제 : https://programmers.co.kr/learn/courses/30/lessons/12940
- 입출력 예
n	m	return
3	12	[3, 12]
2	5	[1, 10]
"""

def solution(n, m):
    return cal_lcm(n, m)

def cal_gcd(a, b): # 유클리드 호제법
    while (b > 0):
        temp = b
        b = a % b
        a = temp
    return a

def cal_lcm(a, b): # 최대공약수와의 관계 이용
    gcd = cal_gcd(a, b)
    return [gcd, int((a * b) / gcd)]

if __name__ == "__main__":
    n, m = 3, 12
    result = solution(n, m)
    print(result)