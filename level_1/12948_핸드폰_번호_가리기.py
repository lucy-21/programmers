"""
핸드폰 번호 가리기
- 문제 : https://programmers.co.kr/learn/courses/30/lessons/12948
- 입출력 예
phone_number	return
"01033334444"	"*******4444"
"027778888"	"*****8888"
"""

def solution(phone_number):
    return '*' * (len(phone_number) - 4) + phone_number[-4:]

if __name__ == "__main__":
    phone_number = "01033334444"
    result = solution(phone_number)
    print(result)